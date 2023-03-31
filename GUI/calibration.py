import tkinter as tk


def show():
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

    # Start the main event loop
    root.mainloop()
