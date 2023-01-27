import os
import time
import cv2
import keyboard


def faceTracking():
    # Object Detection Algorithm used to identify faces in webcam
    face_cascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
    eye_cascade = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_eye.xml'))

    # open video cature stream
    webcam = cv2.VideoCapture(0)
    count = 1

    while True:
        # open image stream
        ret, img = webcam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detects face's in the input image, The detected objects are returned as a list of rectangles
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        # x and y coord of face in image, w and h of face.
        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in eyes:

                # 2 lines below were taken from a helpful tutorial on OpenCV to capture eye rectangle image.
                crop_img = roi_gray[ey: ey + eh, ex: ex + ew]
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                # Save Image
                s1 = 'img/img{}.jpg'.format(count)
                count = count + 1
                cv2.imwrite(s1, crop_img)
                time.sleep(1)
                print(str(s1) + "saved")

        # Close program on spacebar.
        cv2.imshow('img', img)
        if keyboard.is_pressed("space"):
            exit()
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    faceTracking()
