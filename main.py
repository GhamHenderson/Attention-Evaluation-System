import cv2
import blinkscript
import iris_position_estimation

# Webcam
# cap = cv2.VideoCapture(0)

# Video with good lighting
cap = cv2.VideoCapture('./vid/WIN_20230215_15_08_52_Pro.mp4')

blinkscript.blink_counter(cap)
# iris_position_estimation.iris_position(cap)
