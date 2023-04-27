import cv2

from irisConfig import iris_position
from attention_eval import attention_tracker
from Attention_score import attention_score
from GUI import intro


def main():
    name = intro.get_username()  # Get Users Name
    blink_stream = cv2.VideoCapture('./media/iris.mp4')  # Get The Location of Video Stream
    iris_threshold_coords = iris_position(blink_stream)  # Open GUI Window and begin user configuration
    iris, blinks, yawn_total = attention_tracker(blink_stream, iris_threshold_coords)  # Run Attention Script
    attention_score(iris, blinks, yawn_total, name)  # Run Algorithm to calculate scores.


if __name__ == '__main__':
    main()
