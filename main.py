import cv2
from blinkscript import blink_counter
from iris_position_estimation import iris_position
from multiprocessing import Pool, Process
import threading
import cv2


def main():
    wencam_stream = cv2.VideoCapture(0)  # Webcam stream
    blink_stream = cv2.VideoCapture('./media/WIN_20230215_15_08_52_Pro.mp4')  # Video with good lighting
    iris_stream = cv2.VideoCapture('./media/iris.mp4')  # video looking in different directions

    iris_position(iris_stream)

    # # create a thread for function1
    # t1 = threading.Thread(target=iris_position, args=(cap,))
    # # create a thread for function2
    # t2 = threading.Thread(target=blink_counter, args=(cap2,))
    #
    # # start both threads
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()


if __name__ == '__main__':
    main()
