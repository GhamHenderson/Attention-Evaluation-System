import tkinter as tk

import customtkinter
import cv2

from blinkscript import blink_counter

i = 0

def button_callback():
    global root
    global label_1
    global i
    if i == 0:
        label_1.config(text="Now look at the top left and click confirm")
        i += 1
    elif i == 1:
        label_1.config(text="Now look at the bottom left and click confirm")
        i += 1
    elif i == 2:
        label_1.config(text="Now look at the bottom right and click confirm")
        i += 1
    else:
        root.withdraw()
        blink_stream = cv2.VideoCapture('./media/WIN_20230215_15_08_52_Pro.mp4')  # Video with good lighting
        blink_counter(blink_stream)


def show():
    global label_1
    global root
    root = tk.Tk()
    root.attributes("-fullscreen", False)

    # Create a canvas widget to draw on
    canvas_width = 1800
    canvas_height = 980
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Define the radius of the circles
    circle_radius = 50

    # Draw circles in the four corners of the canvas
    canvas.create_oval(0, 0, circle_radius * 2, circle_radius * 2, fill="red")
    canvas.create_oval(canvas_width - 2 * circle_radius, 0, canvas_width, circle_radius * 2, fill="red")
    canvas.create_oval(0, canvas_height - 2 * circle_radius, circle_radius * 2, canvas_height, fill="red")
    canvas.create_oval(canvas_width - 2 * circle_radius, canvas_height - 2 * circle_radius, canvas_width, canvas_height,
                       fill="red")

    button_1 = customtkinter.CTkButton(master=canvas, command=button_callback)
    button_1.configure(text="Confirm")
    button_1.place(relx=0.5, rely=0.5, anchor="center")

    label_1 = tk.Label(master=root, text="Look To the top right circle and click confirm")
    label_1.place(relx=0.5, rely=0.4, anchor="center")
    # Start the main event loop
    root.mainloop()
