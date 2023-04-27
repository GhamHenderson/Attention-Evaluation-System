import tkinter
import customtkinter
import cv2


def open_window():
    def button_callback():
        blink_stream = cv2.VideoCapture('./media/WIN_20230215_15_08_52_Pro.mp4')  # Video with good lighting
        app.withdraw()

    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = customtkinter.CTk()
    app.geometry("1200x880")
    app.title("Attention Evaluation System")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
    label_1.configure(text="Please Click Button Below When you are ready to start your study session")
    label_1.pack(pady=10, padx=10)

    button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
    button_1.configure(text="Start Calibration")
    button_1.pack(pady=10, padx=10)

    label_2 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
    label_2.configure(text="")
    label_2.pack(pady=10, padx=10)


    app.mainloop()
