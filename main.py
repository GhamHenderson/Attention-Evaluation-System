from blinkscript import blink_counter
from iris_position_estimation import iris_position
import cv2
from GUI.GUI import open_window


def main():
    open_window()

    iris_stream = cv2.VideoCapture('./media/iris.mp4')  # video looking in different directions
    webcam_stream = cv2.VideoCapture(0)  # Webcam stream
    blink_stream = cv2.VideoCapture('./media/WIN_20230215_15_08_52_Pro.mp4')  # Video with good lighting
    iris_right_stream = cv2.VideoCapture('./media/lookingright.mp4')  # video iris looking right
    iris_left_stream = cv2.VideoCapture('./media/lookingleft.mp4')  # video iris looking left
    up_stream = cv2.VideoCapture('./media/up.mp4')

    # iris_position(iris_stream)
    # blink_counter(blink_stream)


if __name__ == '__main__':
    main()
