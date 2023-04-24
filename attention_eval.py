import time
from datetime import datetime
import cv2 as cv
import cvzone
import keyboard
import numpy as np
import mediapipe as mp
from cvzone.FaceMeshModule import FaceMeshDetector
import tkinter as tk


def save_data_to_textfile(minute_average):
    # Get current date and time
    now = datetime.now()

    # Create filename using current date and time
    filename = now.strftime("blink_records/blinkrate_%m-%d_%H.txt")

    # Use filename to create new file
    with open(filename, 'w') as f:
        f.write("\n\n{}\n[\n".format(now))
        for i, item in enumerate(minute_average):
            if i == len(minute_average) - 1:
                f.write("   {{ Minute:{}, Blink Rate: {}}}\n] \n".format(i, item))
            else:
                f.write("   {{ Minute:{}, Blink Rate: {}}}, \n".format(i, item))
    f.close()


def attention_tracker(input_stream, iris_threshold):
    mp_face_mesh = mp.solutions.face_mesh
    detector = FaceMeshDetector(maxFaces=1)

    left_eye_landmarks = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
    right_eye_landmarks = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
    blink_counter: int = 0
    left_iris_landmarks = [474, 475, 476, 477]
    right_iris_landmarks = [469, 470, 471, 472]
    ratioList = []
    i = 0
    threshold = 30
    ratio_average = 0
    counter = 0
    minute_average = [12, 12, 12]  # loaded with sample data
    skip = 0
    iris_data = [0, 0]
    off_screen_count = 0
    mouth_open = False
    count = 0

    while True:
        with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, ) as face_mesh:
            while True:

                # read a frame from the input stream
                img, frame = input_stream.read()
                root = tk.Tk()
                root.withdraw()
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                frame = cv.resize(frame, (screen_width, screen_height))

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
                    cvzone.putTextRect(frame, "Blink Count : " + str(blink_counter), (50, 100))
                    cvzone.putTextRect(frame, "Times Looked Off Screen : " + str(off_screen_count), (50, 150))
                    cv.imshow('img', frame)

                ''' Blink Feature '''

                '''
                Every Minute Take total blinks and add to  array containing total.
                '''
                timer = datetime.now().second
                # Timer To count blinks every 60 seconds, exclude first minute for accuracy reasons
                if timer == 59:
                    if skip != 0:
                        minute_average.append(blink_counter)
                        blink_counter = 0
                        time.sleep(1)
                    else:
                        time.sleep(1)

                    skip += 1

                distance_top_bottom, _ = detector.findDistance(left_upper_eye, left_lower_eye)
                distance_hor, _ = detector.findDistance(left_eye_left_side, left_eye_right_side)

                cv.line(img, left_upper_eye, left_lower_eye, (0, 200, 0), 3)
                cv.line(img, left_eye_left_side, left_eye_right_side, (0, 200, 0), 3)

                ratio = distance_top_bottom / distance_hor * 100

                # Keep track of the last few eye aspect ratios and calculate their average
                ratioList.append(ratio)
                if len(ratioList) > 5:
                    ratioList.pop(0)
                    ratio_average = sum(ratioList) / len(ratioList)

                # If the eye aspect ratio falls below a threshold, increment the blink counter
                if ratio_average < 35 and counter == 0:
                    blink_counter += 1
                    counter = 1
                if counter != 0:
                    counter += 1
                    if counter > 10:  # After 10 frames
                        counter = 0

                    ''' Iris Feature '''

                    left_iris_threshold = iris_threshold[0]
                    right_iris_threshold = iris_threshold[1]
                    up_iris_threshold = iris_threshold[2]
                    down_iris_threshold = iris_threshold[3]

                    # Check If User is looking left or right using threshold values.
                    print(distance_left_center)
                    if distance_left_center > left_iris_threshold:
                        print("Looking Right")
                    elif distance_left_center < right_iris_threshold:
                        print("Looking Left")

                    # Check If User is looking off-screen using threshold values
                    if distance_left_center < left_iris_threshold - 3 or distance_left_center > right_iris_threshold + 3:
                        print("Looking Off Screen")
                        off_screen_count += 1

                    # Check If User is looking up or down using threshold values.
                    if distance_lower_from_center > up_iris_threshold:
                        print("Looking Up")
                    elif distance_lower_from_center < down_iris_threshold:
                        print("Looking Down")

                        ''' Yawn Detection '''

                    if ratio_average < 35 and mouth_open:
                        count += 1
                        if count > 5:
                            print("Yawn Detected")
                            mouth_open = False

                    if cv.waitKey(25) & 0xFF == ord('q'):
                        input_stream.release()
                        cv.destroyAllWindows()
                        return iris_data, minute_average
