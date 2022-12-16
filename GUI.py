import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("600x480")
app.title("Attention Evaluation System")


def button_callback():
    label_2.configure(text="Program Will Run")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
label_1.configure(text="Please Click Button Below When you are ready to start your study session")
label_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.configure(text="Start Study Session")
button_1.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
label_2.configure(text="")
label_2.pack(pady=10, padx=10)

app.mainloop()
