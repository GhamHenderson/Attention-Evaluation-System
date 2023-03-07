import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

ratioAverage = 0
counter = 0
# video for testing
cap = cv2.VideoCapture('./vid/WIN_20230215_15_08_52_Pro.mp4')
# Webcam
# cap = cv2.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640, 360, [20, 50])
Facial_Landmark_List = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
blinkCounter = 0
threshold = 30

while True:
    # If the condition is true, it means that the video has reached its end, and the code is resetting the frame
    # position to 0
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    # If faces are detected, find the first face and draw circles around the eyes
    if faces:
        face = faces[0]
        for i in Facial_Landmark_List:
            cv2.circle(img, face[i], 5, (255, 0, 255), cv2.FILLED)

        # Calculate the eye aspect ratio and store it in a variable
        left_upper_eye = face[159]
        left_lower_eye = face[23]
        left_eye_left_side = face[130]
        left_eye_right_side = face[243]

        distance_top_bottom, _ = detector.findDistance(left_upper_eye, left_lower_eye)
        distance_hor, _ = detector.findDistance(left_eye_left_side, left_eye_right_side)

        cv2.line(img, left_upper_eye, left_lower_eye, (0, 200, 0), 3)
        cv2.line(img, left_eye_left_side, left_eye_right_side, (0, 200, 0), 3)

        ratio = distance_top_bottom / distance_hor * 100

        # Keep track of the last few eye aspect ratios and calculate their average

        ratioList.append(ratio)
        if len(ratioList) > 5:
            ratioList.pop(0)
            ratioAverage = sum(ratioList) / len(ratioList)

        # Update the plot with the average eye aspect ratio
        plot_Image = plotY.update(ratioAverage)

        # If the eye aspect ratio falls below a threshold, increment the blink counter
        if ratioAverage < 35 and counter == 0:
            blinkCounter += 1
            counter = 1
        if counter != 0:
            counter += 1
            if counter > 10:  # After 10 frames
                counter = 0

        # Display the blink counter on the image
        cvzone.putTextRect(img, str(blinkCounter), (50, 100))

    # Resize the image for display and show it
    img = cv2.resize(img, (640, 360))
    cv2.imshow("Image", img)
    cv2.imshow("ImagePlot", plot_Image)

    # Wait for a short period and check if the user has pressed 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
