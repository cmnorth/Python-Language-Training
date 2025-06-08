# =================================Updated Login Window with Quiz Integration==================================
# login_window_updated.py - Enhanced login window with full quiz and records integration
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import hashlib
from datetime import datetime

class LoginWindow:
    def __init__(self, root, demo_callback, login_success_callback, back_to_menu_callback, logout_callback, quiz_callback, records_callback):
        self.root = root
        self.demo_callback = demo_callback
        self.login_success_callback = login_success_callback
        self.back_to_menu_callback = back_to_menu_callback
        self.logout_callback = logout_callback
        self.quiz_callback = quiz_callback
        self.records_callback = records_callback
        self.commands_var = None
        self.quiz_var = None
        self.is_logged_in = False
        self.user_data = {}
        
        # Form fields for new user registration
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.class_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        
        # Form fields for returning user login
        self.login_email_var = tk.StringVar()
        self.login_password_var = tk.StringVar()
    
    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show(self):
        """Display the login window"""
        self.clear_window()
        
        # Create scrollable main frame
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
        
        # Main content frame
        main_frame = tk.Frame(scrollable_frame, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, 
                              text="Student Login", 
                              font=('Arial', 16, 'bold'),
                              bg='white')
        title_label.pack(pady=(10, 20))
        
        # Create login sections
        self.create_returning_user_section(main_frame)
        self.create_separator(main_frame)
        self.create_new_user_section(main_frame)
        self.create_interactive_sections(main_frame)
        self.create_bottom_buttons(main_frame)
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Set focus to first login field
        self.login_email_entry.focus_set()

    def create_returning_user_section(self, parent):
        """Create returning user login section"""
        returning_frame = tk.LabelFrame(parent, text="Returning User Login", 
                                       font=('Arial', 12, 'bold'), bg='white', 
                                       relief='groove', bd=2)
        returning_frame.pack(fill='x', pady=(0, 15))
        
        # Email field
        tk.Label(returning_frame, text="Email:", font=('Arial', 10), bg='white').pack(anchor='w', padx=10, pady=(10, 2))
        self.login_email_entry = tk.Entry(returning_frame, textvariable=self.login_email_var, font=('Arial', 10), width=30)
        self.login_email_entry.pack(padx=10, pady=(0, 5))
        self.login_email_entry.bind('<Return>', lambda e: self.login_existing_user())
        
        # Password field
        tk.Label(returning_frame, text="Password:", font=('Arial', 10), bg='white').pack(anchor='w', padx=10, pady=(5, 2))
        self.login_password_entry = tk.Entry(returning_frame, textvariable=self.login_password_var, font=('Arial', 10), width=30, show="*")
        self.login_password_entry.pack(padx=10, pady=(0, 10))
        self.login_password_entry.bind('<Return>', lambda e: self.login_existing_user())
        
        # Login button
        login_button = tk.Button(returning_frame, 
                                text="Login", 
                                font=('Arial', 11, 'bold'),
                                command=self.login_existing_user,
                                bg='#2196F3',
                                fg='white',
                                relief='raised',
                                bd=2)
        login_button.pack(pady=10)

    def create_separator(self, parent):
        """Create separator between sections"""
        separator = tk.Label(parent, text="── OR ──", font=('Arial', 10), bg='white', fg='gray')
        separator.pack(pady=10)

    def create_new_user_section(self, parent):
        """Create new user registration section"""
        registration_frame = tk.LabelFrame(parent, text="New User Registration", 
                                          font=('Arial', 12, 'bold'), bg='white', 
                                          relief='groove', bd=2)
        registration_frame.pack(fill='x', pady=(0, 20))
        
        # Registration fields
        fields = [
            ("First Name*:", self.first_name_var),
            ("Last Name*:", self.last_name_var),
            ("Class Name (Optional):", self.class_name_var),
            ("Email*:", self.email_var),
            ("Password* (minimum 6 characters):", self.password_var)
        ]
        
        for label_text, var in fields:
            tk.Label(registration_frame, text=label_text, font=('Arial', 10), bg='white').pack(anchor='w', padx=10, pady=(5, 2))
            entry = tk.Entry(registration_frame, textvariable=var, font=('Arial', 10), width=30)
            if "Password" in label_text:
                entry.config(show="*")
                entry.bind('<Return>', lambda e: self.submit_user_data())
            entry.pack(padx=10, pady=(0, 5))
        
        # Register button
        submit_button = tk.Button(registration_frame, 
                                 text="Register", 
                                 font=('Arial', 11, 'bold'),
                                 command=self.submit_user_data,
                                 bg='#4CAF50',
                                 fg='white',
                                 relief='raised',
                                 bd=2)
        submit_button.pack(pady=10)

    def create_interactive_sections(self, parent):
        """Create interactive demos and quizzes sections"""
        # Interactive Commands Dropdown
        commands_frame = tk.Frame(parent, bg='white')
        commands_frame.pack(pady=10, fill='x')
        
        self.commands_label = tk.Label(commands_frame, 
                                      text="🔧 Interactive Demos:", 
                                      font=('Arial', 11, 'bold'),
                                      bg='white',
                                      fg='gray')
        self.commands_label.pack(anchor='w')
        
        self.commands_var = tk.StringVar()
        self.commands_dropdown = ttk.Combobox(commands_frame, 
                                            textvariable=self.commands_var,
                                            state="disabled",
                                            width=35)
        self.commands_dropdown['values'] = (
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
        self.commands_dropdown.pack(pady=5, fill='x')
        self.commands_dropdown.bind('<<ComboboxSelected>>', self.command_selected)
        
        # Quiz Dropdown
        quiz_frame = tk.Frame(parent, bg='white')
        quiz_frame.pack(pady=15, fill='x')
        
        self.quiz_label = tk.Label(quiz_frame, 
                                  text="🎯 Interactive Quizzes:", 
                                  font=('Arial', 11, 'bold'),
                                  bg='white',
                                  fg='gray')
        self.quiz_label.pack(anchor='w')
        
        self.quiz_var = tk.StringVar()
        self.quiz_dropdown = ttk.Combobox(quiz_frame,
                                         textvariable=self.quiz_var,
                                         state="disabled",
                                         width=35)
        self.quiz_dropdown['values'] = (
            'str - Strings Quiz',
            'print() - Print Function Quiz',
            'input() - Input Function Quiz',
            'len() - Length Function Quiz',
            'type() - Type Function Quiz',
            'range() - Range Function Quiz',
            'list() - List Function Quiz',
            'dict() - Dictionary Quiz',
            'for loop - Loop Quiz',
            'if statement - Conditional Quiz',
            'def - Functions Quiz'
        )
        self.quiz_dropdown.pack(pady=5, fill='x')
        self.quiz_dropdown.bind('<<ComboboxSelected>>', self.quiz_selected)
        
        # Instructions
        self.demo_instruction = tk.Label(commands_frame, 
                                        text="Select a demo above to practice Python concepts", 
                                        font=('Arial', 9, 'italic'),
                                        bg='white',
                                        fg='gray')
        self.demo_instruction.pack(pady=2)
        
        self.quiz_instruction = tk.Label(quiz_frame, 
                                        text="Select a quiz above to test your knowledge", 
                                        font=('Arial', 9, 'italic'),
                                        bg='white',
                                        fg='gray')
        self.quiz_instruction.pack(pady=2)

    def create_bottom_buttons(self, parent):
        """Create bottom control buttons"""
        bottom_frame = tk.Frame(parent, bg='white')
        bottom_frame.pack(side='bottom', fill='x', pady=(20, 0))
        
        # Records button
        self.records_button = tk.Button(bottom_frame, 
                                       text="📊 View Records", 
                                       font=('Arial', 11),
                                       width=12,
                                       height=2,
                                       command=self.show_records,
                                       bg='#FF9800',
                                       fg='white',
                                       relief='raised',
                                       bd=2,
                                       state='disabled')
        self.records_button.pack(side='left', padx=(0, 5))
        
        # Logout button
        self.logout_button = tk.Button(bottom_frame, 
                                      text="🚪 Logout", 
                                      font=('Arial', 11),
                                      width=10,
                                      height=2,
                                      command=self.logout_user,
                                      bg='#9C27B0',
                                      fg='white',
                                      relief='raised',
                                      bd=2,
                                      state='disabled')
        self.logout_button.pack(side='left', padx=5)
        
        # Back to Menu button
        self.back_button = tk.Button(bottom_frame, 
                                    text="🏠 Back to Menu", 
                                    font=('Arial', 11),
                                    width=14,
                                    height=2,
                                    command=self.back_to_menu_callback,
                                    bg='#f44336',
                                    fg='white',
                                    relief='raised',
                                    bd=2)
        self.back_button.pack(side='right')

    def enable_interface(self):
        """Enable dropdowns and features after successful login"""
        # Enable dropdowns
        self.commands_dropdown.config(state="readonly")
        self.quiz_dropdown.config(state="readonly")
        
        # Enable buttons
        self.records_button.config(state='normal')
        self.logout_button.config(state='normal')
        
        # Update label colors
        self.commands_label.config(fg='black')
        self.quiz_label.config(fg='black')
        self.demo_instruction.config(fg='blue')
        self.quiz_instruction.config(fg='blue')

    def disable_interface(self):
        """Disable interface when logged out"""
        # Disable dropdowns
        self.commands_dropdown.config(state="disabled")
        self.quiz_dropdown.config(state="disabled")
        
        # Disable buttons
        self.records_button.config(state='disabled')
        self.logout_button.config(state='disabled')
        
        # Update label colors
        self.commands_label.config(fg='gray')
        self.quiz_label.config(fg='gray')
        self.demo_instruction.config(fg='gray')
        self.quiz_instruction.config(fg='gray')

    def command_selected(self, event):
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

    def show_records(self):
        """Show records window"""
        if self.is_logged_in:
            self.records_callback()
        else:
            messagebox.showwarning("Login Required", "Please login first to view records.")

    # Authentication methods (same as before)
    def hash_password(self, password):
        """Hash password for secure storage"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_email(self, email):
        """Enhanced email validation"""
        if not email:
            return False, "Email is required"
        
        if "@" not in email:
            return False, "Email must contain @ symbol"
        
        if "." not in email.split("@")[1]:
            return False, "Email must contain a domain (e.g., .com, .edu)"
        
        if len(email.split("@")) != 2:
            return False, "Email can only contain one @ symbol"
        
        username, domain = email.split("@")
        if len(username) < 1:
            return False, "Email must have a username before @"
        
        if len(domain) < 3:
            return False, "Email domain is too short"
        
        return True, ""
    
    def validate_password(self, password):
        """Enhanced password validation"""
        if not password:
            return False, "Password is required"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters long"
        
        return True, ""
    
    def login_existing_user(self):
        """Handle login for existing users"""
        email = self.login_email_var.get().strip()
        password = self.login_password_var.get().strip()
        
        # Validate inputs
        if not email:
            messagebox.showerror("Error", "Please enter your email address")
            self.login_email_entry.focus_set()
            return
        
        if not password:
            messagebox.showerror("Error", "Please enter your password")
            self.login_password_entry.focus_set()
            return
        
        # Validate email format
        email_valid, email_error = self.validate_email(email)
        if not email_valid:
            messagebox.showerror("Error", f"Invalid email: {email_error}")
            self.login_email_entry.focus_set()
            return
        
        # Check credentials
        user_data = self.validate_user_credentials(email, password)
        if user_data:
            self.user_data = user_data
            self.is_logged_in = True
            self.enable_interface()
            self.back_button.config(text="🏠 Log Off")
            self.login_success_callback(user_data)
            messagebox.showinfo("Success", f"Welcome back, {user_data['first_name']}!")
            
            # Clear login fields
            self.login_email_var.set("")
            self.login_password_var.set("")
        else:
            messagebox.showerror("Error", "Invalid email or password.\n\nIf you're a new user, please use the registration form below.")
            self.login_password_entry.focus_set()
    
    def validate_user_credentials(self, email, password):
        """Validate user credentials against CSV file"""
        csv_filename = "student_logins.csv"
        if not os.path.isfile(csv_filename):
            return None
        
        hashed_password = self.hash_password(password)
        
        try:
            with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['email'].lower() == email.lower() and row.get('password_hash') == hashed_password:
                        return {
                            'first_name': row['first_name'],
                            'last_name': row['last_name'],
                            'class_name': row['class_name'],
                            'email': row['email'],
                            'login_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read user data: {str(e)}")
        
        return None
    
    def submit_user_data(self):
        """Handle new user registration"""
        # Get and validate fields
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        email = self.email_var.get().strip()
        password = self.password_var.get().strip()
        class_name = self.class_name_var.get().strip()
        
        # Validate required fields
        if not first_name:
            messagebox.showerror("Error", "First name is required")
            return
        
        if not last_name:
            messagebox.showerror("Error", "Last name is required")
            return
        
        # Validate email
        email_valid, email_error = self.validate_email(email)
        if not email_valid:
            messagebox.showerror("Error", f"Invalid email: {email_error}")
            return
        
        # Validate password
        password_valid, password_error = self.validate_password(password)
        if not password_valid:
            messagebox.showerror("Error", password_error)
            return
        
        # Check if email exists
        if self.email_exists(email):
            messagebox.showerror("Error", 
                               "An account with this email already exists.\n\n"
                               "Please use the 'Returning User Login' section above to log in.")
            return
        
        # Store user data
        self.user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'class_name': class_name,
            'email': email,
            'password_hash': self.hash_password(password),
            'login_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Save to CSV
        if self.save_to_csv():
            self.is_logged_in = True
            self.enable_interface()
            self.back_button.config(text="🏠 Log Off")
            self.login_success_callback(self.user_data)
            self.clear_registration_fields()
            messagebox.showinfo("Success", 
                               f"Welcome {first_name} {last_name}!\n\n"
                               f"Your account has been created successfully.\n"
                               f"You can now access interactive demos and quizzes.")
        else:
            messagebox.showerror("Error", "Failed to create account. Please try again.")
    
    def clear_registration_fields(self):
        """Clear registration form fields"""
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.class_name_var.set("")
        self.email_var.set("")
        self.password_var.set("")
    
    def email_exists(self, email):
        """Check if email already exists"""
        csv_filename = "student_logins.csv"
        if not os.path.isfile(csv_filename):
            return False
        
        try:
            with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['email'].lower() == email.lower():
                        return True
        except Exception:
            pass
        
        return False
    
    def save_to_csv(self):
        """Save user data to CSV file"""
        csv_filename = "student_logins.csv"
        file_exists = os.path.isfile(csv_filename)
        
        try:
            with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['first_name', 'last_name', 'class_name', 'email', 'password_hash', 'login_time']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(self.user_data)
                return True
                
        except Exception as e:
            print(f"CSV save error: {e}")
            return False
    
    def logout_user(self):
        """Handle user logout"""
        if messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?"):
            self.is_logged_in = False
            self.user_data = {}
            
            # Clear form fields
            self.clear_registration_fields()
            self.login_email_var.set("")
            self.login_password_var.set("")
            
            # Reset dropdowns
            self.commands_var.set("")
            self.quiz_var.set("")
            
            # Disable interface
            self.disable_interface()
            self.back_button.config(text="🏠 Back to Menu")
            
            # Call logout callback
            self.logout_callback()
            
            messagebox.showinfo("Logged Out", "You have been successfully logged out.")