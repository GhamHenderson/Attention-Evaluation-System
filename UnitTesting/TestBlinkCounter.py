import unittest

import unittest
import cv2
from blinkscript import blink_counter

cap = cv2.VideoCapture('../media/WIN_20230215_15_08_52_Pro.mp4')


def run_all_tests():
    # Create a TestSuite object and add your test cases to it
    suite = unittest.TestSuite()
    suite.addTest(TestBlinkCounter(cap))

    # Create a TestRunner object and run the test suite
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Print the results summary to the console
    print(result)


class TestBlinkCounter(unittest.TestCase):
    # make sure an instance of the window is established.
    def test_blink_counter(self):
        blink_count = blink_counter(cap)
        self.assertIsInstance(blink_count, int)

    def test_ensure_returns_valid_int(self):
        result = blink_counter(cap)
        self.assertIsInstance(result, int)
        # ensure blink counter is greater than 0
        self.assertGreaterEqual(result, 0)

    def test_blink_counter_with_known_blink_video(self):
        # Call the blink_counter function on the test video
        blink_count = blink_counter(cap)

        # Assert that the blink count matches the expected number of blinks
        self.assertEqual(blink_count, 8)

    @unittest.expectedFailure
    def test_fail(self):
        invalid_stream_link = "/invalidfilelocation"
        blink_count = blink_counter(invalid_stream_link)
        self.assertEqual(1, 0, "broken")


if __name__ == '__main__':
    run_all_tests()
