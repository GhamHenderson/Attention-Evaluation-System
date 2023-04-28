import unittest

import cv2

from attention_eval import attention_tracker


class TestYawn(unittest.TestCase):
    def test_yawn_detection(self):
        # Load test video
        input_stream = cv2.VideoCapture('yawn.mp4')

        # Set iris threshold values for testing values from previous test
        iris_threshold = [28.460498941515414, 49.03060268852505, 49.64876634922564, 45.18849411078001]

        # Call attention_tracker function with test video and iris threshold values
        _, _, yawn_count = attention_tracker(input_stream, iris_threshold)

        # Check if yawn count is greater than zero
        assert yawn_count > 0


if __name__ == '__main__':
    unittest.main()
