from multiprocessing import Pool
import cv2 as cv
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
from datetime import datetime, timedelta
import time


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


def blink_counter(cap):
    detector = FaceMeshDetector(maxFaces=1)
    plot_y = LivePlot(640, 360, [20, 50])
    facial_landmark_list = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
    ratioList = []
    blink_counter: int = 0
    threshold = 30
    ratio_average = 0
    counter = 0
    minute_average = [12, 12, 12]  # loaded with sample data
    skip = 0

    while True:
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
            print(skip)
            print(minute_average)

        # If the condition is true, it means that the video has reached its end, and the code is resetting the frame
        # position to 0
        if cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT):
            cap.set(cv.CAP_PROP_POS_FRAMES, 0)

        success, img = cap.read()

        img, faces = detector.findFaceMesh(img, draw=False)

        # If faces are detected, find the first face and draw circles around the eyes
        if faces:
            face = faces[0]
            for i in facial_landmark_list:
                cv.circle(img, face[i], 5, (255, 0, 255), cv.FILLED)

            # Calculate the eye aspect ratio and store it in a variable
            left_upper_eye = face[159]
            left_lower_eye = face[23]
            left_eye_left_side = face[130]
            left_eye_right_side = face[243]

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

            # Update the plot with the average eye aspect ratio
            plot_image = plot_y.update(ratio_average)

            # If the eye aspect ratio falls below a threshold, increment the blink counter
            if ratio_average < 35 and counter == 0:
                blink_counter += 1
                counter = 1
            if counter != 0:
                counter += 1
                if counter > 10:  # After 10 frames
                    counter = 0

            # Display the blink counter on the image
            cvzone.putTextRect(img, "Blink Count : " + str(blink_counter), (50, 100))

        # Resize the image for display and show it
        img = cv.resize(img, (640, 360))
        cv.imshow("Image", img)
        cv.imshow("ImagePlot", plot_image)

        # Wait for a short period and check if the user has pressed 'q' to quit
        if cv.waitKey(25) & 0xFF == ord('q'):
            # save_data_to_textfile(minute_average)
            cv.destroyAllWindows()
            return minute_average
