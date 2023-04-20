import cv2

from irisConfig import iris_position
from attention_eval import attention_tracker
from Attention_score import attention_score


def main():
    blink_stream = cv2.VideoCapture('./media/iris.mp4')

    iris_threshold_coords = iris_position(blink_stream)  # Open GUI Window and begin user configuration
    iris, blinks = attention_tracker(blink_stream, iris_threshold_coords)
    attention_tracker(iris, blinks)


# './media/iris.mp4'
if __name__ == '__main__':
    main()
