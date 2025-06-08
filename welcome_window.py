# =================================Version 03==================================
# welcome_window.py - Welcome screen with logo
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class WelcomeWindow:
    def __init__(self, root, start_callback):
        self.root = root
        self.start_callback = start_callback

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show(self):
        self.clear_window()

        # Main frame setup
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Load and display the logo
        try:
            logo_path = "Northward_House_Publishing-Logo.png"
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((200, 120), resample=Image.LANCZOS)
            logo_photo = ImageTk.PhotoImage(logo_img)

            logo_label = tk.Label(main_frame, image=logo_photo, bg='white')
            logo_label.image = logo_photo
            logo_label.pack(pady=(10, 20))
        except Exception as e:
            print(f"Logo load failed: {e}")

        # Title label
        title_label = tk.Label(main_frame,
                               text="Welcome to The Python Learning App",
                               font=('Arial', 14, 'bold'),
                               bg='white')
        title_label.pack(pady=(0, 20))

        # Start button
        start_button = tk.Button(main_frame,
                                 text="Start",
                                 font=('Arial', 11),
                                 command=self.start_callback,
                                 bg='#4CAF50',
                                 fg='white',
                                 relief='raised',
                                 bd=2,
                                 width=20,
                                 height=2)
        start_button.pack()
