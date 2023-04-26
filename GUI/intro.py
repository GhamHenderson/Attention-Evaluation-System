import tkinter as tk


def get_username():
    def submit_name():
        nonlocal user_name
        user_name = name_entry.get()
        print("User's name:", user_name)
        root.destroy()

    user_name = ""

    # Create the main window
    root = tk.Tk()
    root.title("Enter Name")

    # Set the window size (width x height)
    root.geometry("600x300")

    info_label = tk.Label(root, text="Welcome to the Attention Evaluation System:")

    # Create a label, entry field, and submit button
    name_label = tk.Label(root, text="Enter your name:")
    name_entry = tk.Entry(root)
    submit_button = tk.Button(root, text="Submit", command=submit_name)

    # Calculate the center position for each widget
    window_width, window_height = 600, 300

    label_width, label_height = name_label.winfo_reqwidth(), name_label.winfo_reqheight()
    entry_width, entry_height = name_entry.winfo_reqwidth(), name_entry.winfo_reqheight()
    button_width, button_height = submit_button.winfo_reqwidth(), submit_button.winfo_reqheight()

    label_x = (window_width - label_width) // 2 - entry_width // 2
    label_y = (window_height - label_height) // 2
    entry_x = (window_width + label_width) // 2 - entry_width // 2
    entry_y = (window_height - entry_height) // 2
    button_x = (window_width - button_width) // 2
    button_y = (window_height + label_height) // 2 + 20

    # Place the widgets in the window using place layout
    info_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    name_label.place(x=label_x, y=label_y)
    name_entry.place(x=entry_x, y=entry_y)
    submit_button.place(x=button_x, y=button_y)

    # Start the main event loop and wait for the window to close
    root.wait_window(root)

    return user_name
