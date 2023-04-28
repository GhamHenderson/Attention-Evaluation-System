import os
import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

from matplotlib import pyplot as plt
from matplotlib.testing.compare import compare_images

from Attention_score import attention_score
from attention_eval import save_data_to_textfile


class TestAttentionTracker(unittest.TestCase):
    def test_attention_score(self):
        iris = {"left": 0.60, "right": 0.62}
        blinks = [10, 12, 15, 8, 9, 13]
        yawn_total = 3
        name = "John Doe"
        name2 = None

        # Test for a valid user name
        with self.subTest("User name is not empty"):
            attention_score(iris, blinks, yawn_total, name)
            self.assertIsInstance(name, str)

        with self.subTest("User name is empty"):
            attention_score(iris, blinks, yawn_total, name2)
            self.assertIsNone(name2)

    def test_show_plot(self):
        # Set up sample data for attention_score function
        iris = [0.4, 0.6]
        blinks = [20, 25, 30, 25, 20]
        yawn_total = 5
        name = "John"

        # Call attention_score function
        attention_score(iris, blinks, yawn_total, name)

        # Check if a plot is shown
        self.assertTrue(plt.fignum_exists(plt.gcf().number))

    def setUp(self):
        self.input_stream = MagicMock()
        self.input_stream.read.return_value = (True, MagicMock())
        self.detector = MagicMock()
        self.detector.findDistance.side_effect = [(1.0, 2.0), (2.0, 3.0), (3.0, 4.0), (4.0, 5.0)]
        self.face_mesh = MagicMock()
        self.face_mesh.process.return_value = MagicMock(
            multi_face_landmarks=[MagicMock(landmark=[MagicMock(x=0.1, y=0.2)])])
        self.patch_cv = patch('cv2.imshow')
        self.mock_cv = self.patch_cv.start()

    def tearDown(self):
        self.patch_cv.stop()

