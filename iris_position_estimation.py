import cv2 as cv
import cvzone
import numpy as np
import mediapipe as mp
from cvzone.FaceMeshModule import FaceMeshDetector


def iris_position(input_stream):
    mp_face_mesh = mp.solutions.face_mesh
    detector = FaceMeshDetector(maxFaces=1)

    left_eye_landmarks = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
    right_eye_landmarks = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]

    left_iris_landmarks = [474, 475, 476, 477]
    right_iris_landmarks = [469, 470, 471, 472]

    while True:
        with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, ) as face_mesh:
            while True:
                # read a frame from the input stream
                img, frame = input_stream.read()

                frame = cv.resize(frame, (700, 500))

                # if we have reached the end of the video stream, reset the stream to the beginning
                if input_stream.get(cv.CAP_PROP_POS_FRAMES) == input_stream.get(cv.CAP_PROP_FRAME_COUNT):
                    input_stream.set(cv.CAP_PROP_POS_FRAMES, 0)

                # convert the color space of the frame from BGR to RGB
                rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

                # get the height and width of the frame
                img_h, img_w = frame.shape[:2]
                # apply the face_mesh processing function to the RGB frame to detect face landmarks
                after_processing = face_mesh.process(rgb_frame)

                # if face landmarks are detected
                if after_processing.multi_face_landmarks:
                    # extract the mesh points from the detected face landmarks and convert them to pixel coordinates
                    facial_landmark_mesh_points = np.array(
                        [np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in
                         after_processing.multi_face_landmarks[0].landmark])

                    # compute the minimum enclosing circle of the left and right iris landmarks
                    (left_x, left_y), left_radius = cv.minEnclosingCircle(
                        facial_landmark_mesh_points[left_iris_landmarks])
                    (right_x, right_y), right_radius = cv.minEnclosingCircle(
                        facial_landmark_mesh_points[right_iris_landmarks])

                    # convert the circle centers to integer coordinates
                    center_right_iris = np.array([left_x, left_y], dtype=np.int32)
                    center_left_iris = np.array([right_x, right_y], dtype=np.int32)

                    # Calculate the eye aspect ratio and store it in a variable
                    left_upper_eye = facial_landmark_mesh_points[159]
                    left_lower_eye = facial_landmark_mesh_points[23]
                    left_eye_left_side = facial_landmark_mesh_points[243]
                    left_eye_right_side = facial_landmark_mesh_points[130]

                    # Calculate the eye aspect ratio and store it in a variable
                    right_upper_eye = facial_landmark_mesh_points[386]
                    right_lower_eye = facial_landmark_mesh_points[374]
                    right_eye_left_side = facial_landmark_mesh_points[398]
                    right_eye_right_side = facial_landmark_mesh_points[359]

                    distance_whole_eye_verticle, _ = detector.findDistance(left_upper_eye, left_lower_eye)
                    distance_whole_eye_horizontal, _ = detector.findDistance(left_eye_left_side, left_eye_right_side)

                    distance_lower_from_center, _ = detector.findDistance(left_lower_eye, left_eye_right_side)
                    distance_right_center, _ = detector.findDistance(left_eye_right_side, center_left_iris)

                    distance_left_center, _ = detector.findDistance(left_eye_left_side, center_left_iris)
                    distance_upper_from_center, _ = detector.findDistance(left_upper_eye, center_left_iris)

                    ratio_left = distance_left_center / distance_whole_eye_verticle * 100
                    ratio_right = distance_right_center / distance_whole_eye_verticle * 100

                    threshold_left = 90
                    threshold_right = 90

                    if ratio_left < threshold_left:
                        cvzone.putTextRect(frame, "Looking Left", (50, 100))
                    elif ratio_right < threshold_right:
                        cvzone.putTextRect(frame, "Looking Right", (50, 100))
                    else:
                        cvzone.putTextRect(frame, "Looking Center", (50, 100))

                    # draw a circle around the left and right iris landmarks on the original frame
                    cv.circle(frame, center_right_iris, int(left_radius - 5), (255, 0, 255), 1, cv.LINE_AA)
                    cv.circle(frame, center_left_iris, int(right_radius - 5), (255, 0, 255), 1, cv.LINE_AA)

                    # draw lines for left eye
                    cv.line(frame, center_left_iris, left_eye_left_side, (0, 200, 0), 3)
                    cv.line(frame, center_left_iris, left_eye_right_side, (0, 200, 0), 3)

                    cv.line(frame, center_left_iris, left_eye_left_side, (0, 200, 0), 3)
                    cv.line(frame, center_left_iris, left_eye_right_side, (0, 200, 0), 3)

                    cv.line(frame, center_left_iris, left_upper_eye, (0, 200, 0), 3)
                    cv.line(frame, center_left_iris, left_lower_eye, (0, 200, 0), 3)

                    # Draw Lines for right eye
                    cv.line(frame, center_right_iris, right_eye_left_side, (0, 200, 0), 3)
                    cv.line(frame, center_right_iris, right_eye_right_side, (0, 200, 0), 3)

                    cv.line(frame, center_right_iris, right_eye_left_side, (0, 200, 0), 3)
                    cv.line(frame, center_right_iris, right_eye_right_side, (0, 200, 0), 3)

                    cv.line(frame, center_right_iris, right_upper_eye, (0, 200, 0), 3)
                    cv.line(frame, center_right_iris, right_lower_eye, (0, 200, 0), 3)

                cv.imshow('img', frame)

                if cv.waitKey(25) & 0xFF == ord('q'):
                    break
        input_stream.release()
        cv.destroyAllWindows()
