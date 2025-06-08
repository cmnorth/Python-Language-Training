# =================================Version 06 - CLEAN DEMO-ONLY==================================
# menu_window.py - Demo-only menu window without quiz or report features
import tkinter as tk
from tkinter import ttk, messagebox

class MenuWindow:
    def __init__(self, root, demo_callback, login_callback, exit_callback, user_data=None):
        self.root = root
        self.demo_callback = demo_callback
        self.login_callback = login_callback
        self.exit_callback = exit_callback
        self.user_data = user_data
        self.commands_var = None

        self.is_logged_in = bool(user_data)
        print(f"MenuWindow initialized - Logged in: {self.is_logged_in}, User: {user_data.get('first_name', 'None') if user_data else 'None'}")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def update_login_status(self, user_data=None):
        self.user_data = user_data
        self.is_logged_in = bool(user_data)
        print(f"Menu login status updated - Logged in: {self.is_logged_in}, User: {user_data.get('first_name', 'None') if user_data else 'None'}")
        self.show()

    def show(self):
        self.clear_window()

        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        title_label = tk.Label(main_frame,
                               text="Python Commands Menu",
                               font=('Arial', 16, 'bold'),
                               bg='white')
        title_label.pack(pady=(10, 20))

        if self.is_logged_in:
            user_status = tk.Label(main_frame,
                                   text=f"Welcome, {self.user_data['first_name']} {self.user_data['last_name']}!",
                                   font=('Arial', 11, 'bold'),
                                   bg='white',
                                   fg='green')
            user_status.pack(pady=(0, 10))

            instructions = tk.Label(main_frame,
                                    text="✨ Select a command demo below to get started:",
                                    font=('Arial', 10),
                                    bg='white')
            instructions.pack(pady=(0, 15))

            status_frame = tk.Frame(main_frame, bg='#f0f8ff', relief='raised', bd=1)
            status_frame.pack(fill='x', pady=(0, 15))

            status_label = tk.Label(status_frame,
                                    text="🎯 You have access to all interactive demos!",
                                    font=('Arial', 9, 'bold'),
                                    bg='#f0f8ff',
                                    fg='#2196F3')
            status_label.pack(pady=5)
        else:
            login_button = tk.Button(main_frame,
                                     text="🔐 Log In to Access Demos",
                                     font=('Arial', 12, 'bold'),
                                     width=30,
                                     height=2,
                                     command=self.login_callback,
                                     bg='#2196F3',
                                     fg='white',
                                     relief='raised',
                                     bd=2)
            login_button.pack(pady=20)

            info_label = tk.Label(main_frame,
                                  text="Please log in to access interactive Python demos.",
                                  font=('Arial', 10, 'italic'),
                                  bg='white',
                                  fg='gray')
            info_label.pack(pady=(0, 20))

        commands_frame = tk.Frame(main_frame, bg='white')
        commands_frame.pack(pady=10, fill='x')

        commands_label = tk.Label(commands_frame,
                                  text="🐍 Interactive Python Commands:" if self.is_logged_in else "🔒 Commands (Login Required):",
                                  font=('Arial', 11, 'bold'),
                                  bg='white',
                                  fg='black' if self.is_logged_in else 'gray')
        commands_label.pack(anchor='w')

        self.commands_var = tk.StringVar()
        commands_dropdown = ttk.Combobox(commands_frame,
                                         textvariable=self.commands_var,
                                         state="readonly" if self.is_logged_in else "disabled",
                                         width=40)
        commands_dropdown['values'] = (
            'str - Strings and text data',
            'print() - Display output',
            'input() - Get user input',
            'len() - Get length',
            'type() - Check data type',
            'range() - Create number sequence',
            'list() - Create list',
            'dict() - Create dictionary',
            'for loop - Iterate over items',
            'if statement - Conditional logic',
            'def - Define function'
        )
        commands_dropdown.pack(pady=5, fill='x')
        commands_dropdown.bind('<<ComboboxSelected>>', self.command_selected)

        if self.is_logged_in:
            demo_instruction = tk.Label(commands_frame,
                                        text="👆 Select a command to open an interactive demo",
                                        font=('Arial', 8, 'italic'),
                                        bg='white',
                                        fg='blue')
            demo_instruction.pack(pady=2)

        bottom_frame = tk.Frame(main_frame, bg='white')
        bottom_frame.pack(side='bottom', fill='x', pady=(20, 0))

        account_button = tk.Button(bottom_frame,
                                   text="👤 Account" if self.is_logged_in else "🔐 Login",
                                   font=('Arial', 11),
                                   width=12,
                                   height=2,
                                   command=self.login_callback,
                                   bg='#4CAF50' if not self.is_logged_in else '#2196F3',
                                   fg='white',
                                   relief='raised',
                                   bd=2)
        account_button.pack(side='left', padx=5)

        exit_button = tk.Button(bottom_frame,
                                text="❌ Exit",
                                font=('Arial', 11),
                                width=12,
                                height=2,
                                command=self.exit_callback,
                                bg='#f44336',
                                fg='white',
                                relief='raised',
                                bd=2)
        exit_button.pack(side='right')

    def command_selected(self, event):
        if self.is_logged_in:
            selected_command = self.commands_var.get()
            if selected_command:
                print(f"Demo selected: {selected_command}")
                self.demo_callback(selected_command)
        else:
            messagebox.showwarning("Login Required", "Please log in first to access demos.")
            self.login_callback()
