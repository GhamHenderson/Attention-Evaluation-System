import tkinter as tk
import customtkinter
import cv2
from Attention_score import attention_score
from Old_Scripts.blinkscript import blink_counter

i = 0


def button_callback():
    global root
    global label_1
    global i
    blink_stream = cv2.VideoCapture('./media/WIN_20230215_15_08_52_Pro.mp4')

    if i == 0:
        label_1.config(text="Now look at the top left and click confirm")
        i += 1
    elif i == 1:
        label_1.config(text="Now look at the bottom left and click confirm")
        i += 1
    elif i == 2:
        label_1.config(text="Now look at the bottom right and click confirm")
        i += 1
    else:
        root.withdraw()
        blink_stream = cv2.VideoCapture('./media/WIN_20230215_15_08_52_Pro.mp4')  # Video with good lighting
        iris_stream = cv2.VideoCapture('./media/iris.mp4')  # video looking in different directions

        iris_info = iris_position_estimation.attention_tracker(iris_stream)
        blink_ratio_list = blink_counter(blink_stream)  # Blink Detector and Attached Logic returns List of Blinks

        attention_score(iris_info, blink_ratio_list)  # Combine Outputs to Create an Attention Score


def show():
    global label_1, root

    root = tk.Tk()
    root.attributes("-fullscreen", False)

    # Create a canvas widget to draw on
    canvas_width = 1800
    canvas_height = 980
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Define the radius of the circles
    circle_radius = 50

    # Draw circles in the four corners of the canvas
    canvas.create_oval(0, 0, circle_radius * 2, circle_radius * 2, fill="red")
    canvas.create_oval(canvas_width - 2 * circle_radius, 0, canvas_width, circle_radius * 2, fill="red")
    canvas.create_oval(0, canvas_height - 2 * circle_radius, circle_radius * 2, canvas_height, fill="red")
    canvas.create_oval(canvas_width - 2 * circle_radius, canvas_height - 2 * circle_radius, canvas_width, canvas_height,
                       fill="red")

    button_1 = customtkinter.CTkButton(master=canvas, command=button_callback)
    button_1.configure(text="Confirm")
    button_1.place(relx=0.5, rely=0.5, anchor="center")

    label_1 = tk.Label(master=root, text="Look to the top right circle and click confirm", font=("Times New Roman", 16))
    label_1.place(relx=0.5, rely=0.4, anchor="center")

    # Draw an arrow from the center to the top right corner

    center_x = canvas_width / 2
    center_y = canvas_height / 2
    arrow_end_x = canvas_width - circle_radius
    arrow_end_y = circle_radius
    canvas.create_line(center_x, center_y, arrow_end_x, arrow_end_y, arrow=tk.LAST, width=8,
                       arrowshape=(20, 30, 10))

    # Start the main event loop
    root.mainloop()


# def calibrate_iris_threshold(input_stream, position):
#     mp_face_mesh = mp.solutions.face_mesh
#     detector = FaceMeshDetector(maxFaces=1)
#
#     left_eye_landmarks = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
#     right_eye_landmarks = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
#
#     left_iris_landmarks = [474, 475, 476, 477]
#     right_iris_landmarks = [469, 470, 471, 472]
#
#     while True:
#         with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, ) as face_mesh:
#             while True:
#                 # read a frame from the input stream
#                 ret, frame = input_stream.read()
#                 frame = cv.resize(frame, (700, 500))
#
#                 # if we have reached the end of the video stream, reset the stream to the beginning
#                 if input_stream.get(cv.CAP_PROP_POS_FRAMES) == input_stream.get(cv.CAP_PROP_FRAME_COUNT):
#                     input_stream.set(cv.CAP_PROP_POS_FRAMES, 0)
#
#                 # convert the color space of the frame from BGR to RGB
#                 rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
#
#                 # get the height and width of the frame
#                 img_h, img_w = frame.shape[:2]
#                 # apply the face_mesh processing function to the RGB frame to detect face landmarks
#                 after_processing = face_mesh.process(rgb_frame)
#
#                 # if face landmarks are detected
#                 if after_processing.multi_face_landmarks:
#                     # extract the mesh points from the detected face landmarks and convert them to pixel coordinates
#                     facial_landmark_mesh_points = np.array(
#                         [np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in
#                          after_processing.multi_face_landmarks[0].landmark])
#
#                     # compute the minimum enclosing circle of the left and right iris landmarks
#                     (left_x, left_y), left_radius = cv.minEnclosingCircle(
#                         facial_landmark_mesh_points[left_iris_landmarks])
#
#                     (right_x, right_y), right_radius = cv.minEnclosingCircle(
#                         facial_landmark_mesh_points[right_iris_landmarks])
#
#                     # convert the circle centers to integer coordinates
#                     center_right_iris = np.array([left_x, left_y], dtype=np.int32)
#                     center_left_iris = np.array([right_x, right_y], dtype=np.int32)
#
#                     # Calculate the eye aspect ratio and store it in a variable
#                     left_upper_eye = facial_landmark_mesh_points[159]
#                     left_lower_eye = facial_landmark_mesh_points[23]
#                     left_eye_left_side = facial_landmark_mesh_points[243]
#                     left_eye_right_side = facial_landmark_mesh_points[130]
#
#                     # Calculate the eye aspect ratio and store it in a variable
#                     right_upper_eye = facial_landmark_mesh_points[386]
#                     right_lower_eye = facial_landmark_mesh_points[374]
#                     right_eye_left_side = facial_landmark_mesh_points[398]
#                     right_eye_right_side = facial_landmark_mesh_points[359]
#
#
#
#
#             match position:
#                 case 'TR':
#                     print("Top Right")
#                 case 'TL':
#                     print("Top Left")
#                 case 'BL':
#                     print("Bottom Left")
#                 case 'BR':
#                     print("Bottom Right")
#                 case _:
#                     print("error")
