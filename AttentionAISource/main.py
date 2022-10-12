import datetime
import cv2
import keyboard

"""
Code Written by Graham Henderson
"""


def faceTracking():
    # Object Detection Algorithm used to identify faces in webcam
    face_cascade = cv2.CascadeClassifier('CascadeFiles/haarcascade_frontalface_default.xml')
    # eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    # Open Webcam
    cam = cv2.VideoCapture(0)
    # Check if the webcam is opened correctly
    if not cam.isOpened():
        raise IOError("Cannot open webcam")

    # True block to control webcam execution
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 0, 0), 2)

        cv2.imshow('Input', frame)
        cv2.setWindowTitle('Input', 'Eye Tracker')
        closeWindow = cv2.waitKey(1)

        if keyboard.is_pressed('spacebar'):
            img_name = "img/image{}.png".format(1)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            closeWindow
            break

    cam.release()
    cv2.destroyAllWindows()
    return


if __name__ == '__main__':
    faceTracking()
