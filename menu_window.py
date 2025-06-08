# =================================Updated Menu Window with Proper Width Layout==================================
# menu_window.py - Enhanced menu window with wider layout for dropdown content
import tkinter as tk
from tkinter import ttk, messagebox

class MenuWindow:
    def __init__(self, root, demo_callback, quiz_callback, records_callback, login_callback, exit_callback, user_data=None):
        self.root = root
        self.demo_callback = demo_callback
        self.quiz_callback = quiz_callback
        self.records_callback = records_callback
        self.login_callback = login_callback
        self.exit_callback = exit_callback
        self.user_data = user_data
        self.commands_var = None
        self.quiz_var = None

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

        # Create scrollable main frame for better layout
        canvas = tk.Canvas(self.root, bg='white')
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollable components
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Main frame with increased padding for wider layout
        main_frame = tk.Frame(scrollable_frame, bg='white')
        main_frame.pack(fill='both', expand=True, padx=35, pady=20)  # Increased padx from 25 to 35

        # Title
        title_label = tk.Label(main_frame, 
                              text="🐍 Python Learning Hub", 
                              font=('Arial', 16, 'bold'),
                              bg='white',
                              fg='#2e7d32')
        title_label.pack(pady=(0, 20))

        # User status display
        self.create_user_status_display(main_frame)

        # Interactive Demos Section
        demos_frame = tk.LabelFrame(main_frame, text="🔧 Interactive Python Demos", 
                                   font=('Arial', 12, 'bold'), bg='white',
                                   relief='groove', bd=2)
        demos_frame.pack(fill='x', pady=(0, 15), padx=10)  # Increased padx from 5 to 10 for proper border display
        
        demo_desc = tk.Label(demos_frame,
                           text="Practice Python concepts with hands-on examples",
                           font=('Arial', 10),
                           bg='white',
                           fg='gray')
        demo_desc.pack(anchor='w', padx=20, pady=(5, 0))  # Increased padx from 15 to 20 for inner spacing
        
        self.commands_var = tk.StringVar()
        commands_dropdown = ttk.Combobox(demos_frame,
                                         textvariable=self.commands_var,
                                         state="readonly" if self.is_logged_in else "disabled",
                                         width=55)  # Increased width from 45 to 55 to better fit text
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
        commands_dropdown.pack(pady=10, padx=20, fill='x')  # Increased padx from 15 to 20 and added fill='x'
        commands_dropdown.bind('<<ComboboxSelected>>', self.demo_selected)

        if self.is_logged_in:
            demo_instruction = tk.Label(demos_frame,
                                      text="👆 Select a demo above to start practicing",
                                      font=('Arial', 9, 'italic'),
                                      bg='white',
                                      fg='blue')
            demo_instruction.pack(pady=(0, 10), padx=20)  # Increased padx from 15 to 20
        else:
            demo_disabled_text = tk.Label(demos_frame,
                                        text="🔒 Please login to access interactive demos",
                                        font=('Arial', 9, 'italic'),
                                        bg='white',
                                        fg='gray')
            demo_disabled_text.pack(pady=(0, 10), padx=20)  # Increased padx from 15 to 20

        # Interactive Quizzes Section
        quiz_frame = tk.LabelFrame(main_frame, text="🎯 Interactive Python Quizzes", 
                                  font=('Arial', 12, 'bold'), bg='white',
                                  relief='groove', bd=2)
        quiz_frame.pack(fill='x', pady=(0, 15), padx=10)  # Increased padx from 5 to 10 for proper border display
        
        quiz_desc = tk.Label(quiz_frame,
                           text="Test your knowledge with progressive difficulty levels",
                           font=('Arial', 10),
                           bg='white',
                           fg='gray')
        quiz_desc.pack(anchor='w', padx=20, pady=(5, 0))  # Increased padx from 15 to 20 for inner spacing
        
        self.quiz_var = tk.StringVar()
        quiz_dropdown = ttk.Combobox(quiz_frame,
                                    textvariable=self.quiz_var,
                                    state="readonly" if self.is_logged_in else "disabled",
                                    width=55)  # Increased width from 45 to 55 to better fit text
        quiz_dropdown['values'] = (
            'str - Strings Quiz (75 questions)',
            'print() - Print Function Quiz (75 questions)',
            'input() - Input Function Quiz (Coming Soon)',
            'len() - Length Function Quiz (Coming Soon)',
            'type() - Type Function Quiz (Coming Soon)',
            'range() - Range Function Quiz (Coming Soon)',
            'list() - List Function Quiz (Coming Soon)',
            'dict() - Dictionary Quiz (Coming Soon)',
            'for loop - Loop Quiz (Coming Soon)',
            'if statement - Conditional Quiz (Coming Soon)',
            'def - Functions Quiz (Coming Soon)'
        )
        quiz_dropdown.pack(pady=10, padx=20, fill='x')  # Increased padx from 15 to 20 and added fill='x'
        quiz_dropdown.bind('<<ComboboxSelected>>', self.quiz_selected)

        if self.is_logged_in:
            quiz_instruction = tk.Label(quiz_frame,
                                      text="🎓 Select a quiz above to test your skills",
                                      font=('Arial', 9, 'italic'),
                                      bg='white',
                                      fg='blue')
            quiz_instruction.pack(pady=(0, 10), padx=20)  # Increased padx from 15 to 20
        else:
            quiz_disabled_text = tk.Label(quiz_frame,
                                        text="🔒 Please login to access interactive quizzes",
                                        font=('Arial', 9, 'italic'),
                                        bg='white',
                                        fg='gray')
            quiz_disabled_text.pack(pady=(0, 10), padx=20)  # Increased padx from 15 to 20

        # Action buttons with wider spacing
        self.create_action_buttons(main_frame)

    def create_user_status_display(self, parent):
        """Create user status display section"""
        status_frame = tk.Frame(parent, bg='white')
        status_frame.pack(fill='x', pady=(0, 20))

        if self.is_logged_in:
            welcome_text = f"👋 Welcome back, {self.user_data.get('first_name', 'User')}!"
            status_color = '#4caf50'
            status_icon = "✅"
            status_text = "Logged In"
        else:
            welcome_text = "👋 Welcome to Python Learning Hub"
            status_color = '#ff9800'
            status_icon = "⚠️"
            status_text = "Please Login"

        # Welcome message
        welcome_label = tk.Label(status_frame,
                               text=welcome_text,
                               font=('Arial', 12, 'bold'),
                               bg='white',
                               fg=status_color)
        welcome_label.pack()

        # Status indicator
        status_label = tk.Label(status_frame,
                              text=f"{status_icon} Status: {status_text}",
                              font=('Arial', 10),
                              bg='white',
                              fg=status_color)
        status_label.pack(pady=(5, 0))

    def create_action_buttons(self, parent):
        """Create action buttons section with proper spacing"""
        button_frame = tk.Frame(parent, bg='white')
        button_frame.pack(fill='x', pady=(20, 0))

        # First row of buttons
        top_button_frame = tk.Frame(button_frame, bg='white')
        top_button_frame.pack(fill='x', pady=(0, 10))

        if self.is_logged_in:
            # Records button
            records_button = tk.Button(top_button_frame,
                                     text="📊 View My Records",
                                     font=('Arial', 11, 'bold'),
                                     width=18,
                                     height=2,
                                     command=self.records_callback,
                                     bg='#2196f3',
                                     fg='white',
                                     relief='raised',
                                     bd=2)
            records_button.pack(side='left', padx=(0, 10))

            # Logout button
            logout_button = tk.Button(top_button_frame,
                                    text="🚪 Logout",
                                    font=('Arial', 11),
                                    width=15,
                                    height=2,
                                    command=self.logout_clicked,
                                    bg='#ff5722',
                                    fg='white',
                                    relief='raised',
                                    bd=2)
            logout_button.pack(side='right')
        else:
            # Login button (centered when logged out)
            login_button = tk.Button(top_button_frame,
                                   text="🔑 Login / Register",
                                   font=('Arial', 12, 'bold'),
                                   width=20,
                                   height=2,
                                   command=self.login_callback,
                                   bg='#4caf50',
                                   fg='white',
                                   relief='raised',
                                   bd=2)
            login_button.pack()

        # Second row - Exit button
        bottom_button_frame = tk.Frame(button_frame, bg='white')
        bottom_button_frame.pack(fill='x')

        exit_button = tk.Button(bottom_button_frame,
                              text="❌ Exit Application",
                              font=('Arial', 11),
                              width=20,
                              height=2,
                              command=self.exit_callback,
                              bg='#f44336',
                              fg='white',
                              relief='raised',
                              bd=2)
        exit_button.pack()

    def demo_selected(self, event):
        """Handle demo selection"""
        if self.is_logged_in:
            selected_command = self.commands_var.get()
            if selected_command:
                self.demo_callback(selected_command)
                # Clear selection
                self.commands_var.set("")
        else:
            messagebox.showwarning("Login Required", "Please login first to access demos.")

    def quiz_selected(self, event):
        """Handle quiz selection"""
        if self.is_logged_in:
            selected_quiz = self.quiz_var.get()
            if selected_quiz:
                # Extract command name from quiz selection
                command_name = selected_quiz.split(' - ')[0]
                self.quiz_callback(command_name)
                # Clear selection
                self.quiz_var.set("")
        else:
            messagebox.showwarning("Login Required", "Please login first to access quizzes.")

    def logout_clicked(self):
        """Handle logout button click"""
        if messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?"):
            self.user_data = None
            self.is_logged_in = False
            self.show()  # Refresh the display