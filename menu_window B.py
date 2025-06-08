# =================================Updated Menu Window with Balanced Layout==================================
# menu_window.py - Enhanced menu window with proper frame spacing
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

        # Main frame with balanced padding
        main_frame = tk.Frame(scrollable_frame, bg='white')
        main_frame.pack(fill='both', expand=True, padx=35, pady=20)  # Increased padx from 25 to 35

        # Title
        title_label = tk.Label(main_frame,
                               text="🐍 Python Learning Hub",
                               font=('Arial', 16, 'bold'),
                               bg='white')
        title_label.pack(pady=(10, 20))

        # User status section
        self.create_user_status_section(main_frame)
        
        # Learning options section
        self.create_learning_section(main_frame)
        
        # Bottom buttons
        self.create_bottom_buttons(main_frame)
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def create_user_status_section(self, parent):
        """Create user status and welcome section"""
        if self.is_logged_in:
            status_frame = tk.Frame(parent, bg='#e8f5e8', relief='raised', bd=2)
            status_frame.pack(fill='x', pady=(0, 15), padx=5)  # Added padx for frame padding
            
            welcome_label = tk.Label(status_frame,
                                   text=f"👋 Welcome back, {self.user_data['first_name']}!",
                                   font=('Arial', 12, 'bold'),
                                   bg='#e8f5e8',
                                   fg='#2e7d32')
            welcome_label.pack(pady=8)
            
            status_label = tk.Label(status_frame,
                                  text="✨ You have full access to demos, quizzes, and progress tracking",
                                  font=('Arial', 10),
                                  bg='#e8f5e8',
                                  fg='#388e3c')
            status_label.pack(pady=(0, 8))
        else:
            status_frame = tk.Frame(parent, bg='#fff3e0', relief='raised', bd=2)
            status_frame.pack(fill='x', pady=(0, 15), padx=5)  # Added padx for frame padding
            
            login_prompt = tk.Label(status_frame,
                                  text="🔐 Please log in to access all features",
                                  font=('Arial', 12, 'bold'),
                                  bg='#fff3e0',
                                  fg='#f57c00')
            login_prompt.pack(pady=8)
            
            login_button = tk.Button(status_frame,
                                   text="🚀 Log In Now",
                                   font=('Arial', 11, 'bold'),
                                   command=self.login_callback,
                                   bg='#2196F3',
                                   fg='white',
                                   relief='raised',
                                   bd=2)
            login_button.pack(pady=(0, 8))

    def create_learning_section(self, parent):
        """Create the main learning options section"""
        # Interactive Demos Section
        demos_frame = tk.LabelFrame(parent, text="🔧 Interactive Python Demos", 
                                   font=('Arial', 12, 'bold'), bg='white',
                                   relief='groove', bd=2)
        demos_frame.pack(fill='x', pady=(0, 10), padx=5)  # Added padx for proper border display
        
        demo_desc = tk.Label(demos_frame,
                           text="Practice Python concepts with hands-on examples",
                           font=('Arial', 10),
                           bg='white',
                           fg='gray')
        demo_desc.pack(anchor='w', padx=15, pady=(5, 0))  # Increased padx for inner spacing
        
        self.commands_var = tk.StringVar()
        commands_dropdown = ttk.Combobox(demos_frame,
                                         textvariable=self.commands_var,
                                         state="readonly" if self.is_logged_in else "disabled",
                                         width=45)  # Increased width to better fit text
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
        commands_dropdown.pack(pady=10, padx=15, fill='x')  # Increased padx and added fill='x'
        commands_dropdown.bind('<<ComboboxSelected>>', self.demo_selected)

        if self.is_logged_in:
            demo_instruction = tk.Label(demos_frame,
                                      text="👆 Select a demo above to start practicing",
                                      font=('Arial', 9, 'italic'),
                                      bg='white',
                                      fg='blue')
            demo_instruction.pack(pady=(0, 10), padx=15)

        # Interactive Quizzes Section
        quiz_frame = tk.LabelFrame(parent, text="🎯 Interactive Python Quizzes", 
                                  font=('Arial', 12, 'bold'), bg='white',
                                  relief='groove', bd=2)
        quiz_frame.pack(fill='x', pady=(0, 10), padx=5)  # Added padx for proper border display
        
        quiz_desc = tk.Label(quiz_frame,
                           text="Test your knowledge with progressive difficulty levels",
                           font=('Arial', 10),
                           bg='white',
                           fg='gray')
        quiz_desc.pack(anchor='w', padx=15, pady=(5, 0))  # Increased padx for inner spacing
        
        self.quiz_var = tk.StringVar()
        quiz_dropdown = ttk.Combobox(quiz_frame,
                                    textvariable=self.quiz_var,
                                    state="readonly" if self.is_logged_in else "disabled",
                                    width=55)  # Increased width to better fit text
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
        quiz_dropdown.pack(pady=10, padx=20, fill='x')  # Increased padx and added fill='x'
        quiz_dropdown.bind('<<ComboboxSelected>>', self.quiz_selected)

        if self.is_logged_in:
            quiz_instruction = tk.Label(quiz_frame,
                                      text="🎓 Select a quiz above to test your skills",
                                      font=('Arial', 9, 'italic'),
                                      bg='white',
                                      fg='blue')
            quiz_instruction.pack(pady=(0, 10), padx=15)

        # Progress Tracking Section
        if self.is_logged_in:
            progress_frame = tk.LabelFrame(parent, text="📊 Your Progress", 
                                         font=('Arial', 12, 'bold'), bg='white',
                                         relief='groove', bd=2)
            progress_frame.pack(fill='x', pady=(0, 15), padx=5)  # Added padx for proper border display
            
            progress_desc = tk.Label(progress_frame,
                                   text="Track your quiz scores and learning progress",
                                   font=('Arial', 10),
                                   bg='white',
                                   fg='gray')
            progress_desc.pack(anchor='w', padx=15, pady=(5, 0))  # Increased padx for inner spacing
            
            records_button = tk.Button(progress_frame,
                                     text="📈 View Detailed Progress Records",
                                     font=('Arial', 11, 'bold'),
                                     command=self.records_callback,
                                     bg='#FF9800',
                                     fg='white',
                                     relief='raised',
                                     bd=2,
                                     width=38)  # Increased width
            records_button.pack(pady=10, padx=15)

    def create_bottom_buttons(self, parent):
        """Create bottom control buttons"""
        bottom_frame = tk.Frame(parent, bg='white')
        bottom_frame.pack(side='bottom', fill='x', pady=(20, 0))

        if self.is_logged_in:
            account_button = tk.Button(bottom_frame,
                                     text="👤 Account Settings",
                                     font=('Arial', 11),
                                     width=15,
                                     height=2,
                                     command=self.login_callback,
                                     bg='#2196F3',
                                     fg='white',
                                     relief='raised',
                                     bd=2)
            account_button.pack(side='left', padx=5)
        else:
            login_button = tk.Button(bottom_frame,
                                   text="🔐 Login / Register",
                                   font=('Arial', 11),
                                   width=15,
                                   height=2,
                                   command=self.login_callback,
                                   bg='#4CAF50',
                                   fg='white',
                                   relief='raised',
                                   bd=2)
            login_button.pack(side='left', padx=5)

        exit_button = tk.Button(bottom_frame,
                              text="❌ Exit Application",
                              font=('Arial', 11),
                              width=15,
                              height=2,
                              command=self.exit_callback,
                              bg='#f44336',
                              fg='white',
                              relief='raised',
                              bd=2)
        exit_button.pack(side='right')

    def demo_selected(self, event):
        """Handle demo selection"""
        if self.is_logged_in:
            selected_command = self.commands_var.get()
            if selected_command:
                print(f"Demo selected: {selected_command}")
                self.demo_callback(selected_command)
                # Clear selection after opening
                self.commands_var.set("")
        else:
            messagebox.showwarning("Login Required", "Please log in first to access demos.")
            self.login_callback()

    def quiz_selected(self, event):
        """Handle quiz selection"""
        if self.is_logged_in:
            selected_quiz = self.quiz_var.get()
            if selected_quiz:
                # Check if it's a "Coming Soon" quiz
                if "Coming Soon" in selected_quiz:
                    command_name = selected_quiz.split(' - ')[0]
                    messagebox.showinfo("Coming Soon", 
                                       f"The {command_name} quiz is being developed and will be available soon!\n\n"
                                       f"In the meantime, you can try the {command_name} demo to practice.")
                    # Clear selection
                    self.quiz_var.set("")
                    return
                
                # Extract command name from quiz selection
                command_name = selected_quiz.split(' - ')[0]
                print(f"Quiz selected: {command_name}")
                self.quiz_callback(command_name)
                # Clear selection after opening
                self.quiz_var.set("")
        else:
            messagebox.showwarning("Login Required", "Please log in first to access quizzes.")
            self.login_callback()