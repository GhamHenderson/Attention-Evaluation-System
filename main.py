import cv2

from irisConfig import iris_position


def main():
    blink_stream = cv2.VideoCapture(0)
    iris_position(blink_stream)  # Open GUI Window and begin user configuration

# './media/iris.mp4'
if __name__ == '__main__':
    main()
