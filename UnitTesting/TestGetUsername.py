import unittest
import tkinter as tk
from tkinter import Entry, Label, Button
from unittest.mock import patch

from GUI.intro import get_username, is_valid_name


class TestGetUsername(unittest.TestCase):
    def test_valid_name(self):
        name = "John"
        self.assertTrue(is_valid_name(name))

    def test_name_with_numbers(self):
        name = "John123"
        self.assertFalse(is_valid_name(name))

    def test_name_with_spaces(self):
        name = "John Doe"
        self.assertFalse(is_valid_name(name))

    def test_name_too_short(self):
        name = "Jo"
        self.assertFalse(is_valid_name(name))

    def test_name_too_long(self):
        name = "JohnathanMichaelBartTheSecond"
        self.assertFalse(is_valid_name(name))

    def test_get_username_returns_string(self):
        # Patching the tkinter root window
        with patch.object(tk.Tk, 'wait_window'):
            with patch.object(Button, 'winfo_reqwidth', return_value=80), \
                 patch.object(Button, 'winfo_reqheight', return_value=30), \
                 patch.object(Label, 'winfo_reqwidth', return_value=80), \
                 patch.object(Label, 'winfo_reqheight', return_value=30), \
                 patch.object(Entry, 'winfo_reqwidth', return_value=120), \
                 patch.object(Entry, 'winfo_reqheight', return_value=30):

                # Calling the function and entering a String input
                root = tk.Tk()
                entry = Entry(root)
                entry.pack()
                entry.insert(0, 'Graham')
                result = get_username()
                root.destroy()

        # Check if the output is a string, and we know its valid username from prior function call.
        self.assertIsInstance(result, str)
