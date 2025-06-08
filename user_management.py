# =================================User Management Functions==================================
# user_management.py - User creation and management utilities
import tkinter as tk
from tkinter import messagebox
import csv
import os
import hashlib
from datetime import datetime

class CreateUserDialog:
    def __init__(self, parent, config_manager, refresh_callback):
        self.parent = parent
        self.config_manager = config_manager
        self.refresh_callback = refresh_callback
        self.window = None
        
        # Form variables
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.class_name_var = tk.StringVar()
        self.password_var = tk.StringVar()
        
        self.show()

    def show(self):
        """Show create user dialog"""
        self.window = tk.Toplevel(self.parent)
        self.window.title("Create New User")
        self.window.geometry("400x350")
        self.window.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # Make modal
        self.window.transient(self.parent)
        self.window.grab_set()
        
        colors = self.config_manager.get_theme_colors()
        self.window.configure(bg=colors["background"])
        
        self.create_interface(colors)

    def center_window(self):
        """Center the window"""
        self.window.update_idletasks()
        width = 400
        height = 350
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def create_interface(self, colors):
        """Create the form interface"""
        main_frame = tk.Frame(self.window, bg=colors["background"])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="➕ Create New User",
                              font=('Arial', 14, 'bold'),
                              bg=colors["background"], fg=colors["text"])
        title_label.pack(pady=(0, 20))
        
        # Form fields
        fields = [
            ("First Name*:", self.first_name_var),
            ("Last Name*:", self.last_name_var),
            ("Email*:", self.email_var),
            ("Class Name:", self.class_name_var),
            ("Password*:", self.password_var)
        ]
        
        for label_text, var in fields:
            tk.Label(main_frame, text=label_text, font=('Arial', 10),
                    bg=colors["background"], fg=colors["text"]).pack(anchor='w', pady=(5, 2))
            
            entry = tk.Entry(main_frame, textvariable=var, font=('Arial', 10), width=30)
            if "Password" in label_text:
                entry.config(show="*")
            entry.pack(fill='x', pady=(0, 5))
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=colors["background"])
        button_frame.pack(fill='x', pady=(20, 0))
        
        tk.Button(button_frame, text="Create User",
                 command=self.create_user,
                 bg=colors["primary"], fg="white",
                 font=('Arial', 10, 'bold')).pack(side='left')
        
        tk.Button(button_frame, text="Cancel",
                 command=self.close,
                 bg=colors["danger"], fg="white",
                 font=('Arial', 10)).pack(side='right')

    def create_user(self):
        """Create the new user"""
        # Get values
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        email = self.email_var.get().strip()
        class_name = self.class_name_var.get().strip()
        password = self.password_var.get().strip()
        
        # Validate
        if not first_name or not last_name or not email or not password:
            messagebox.showerror("Error", "Please fill in all required fields (marked with *).")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long.")
            return
        
        if "@" not in email or "." not in email.split("@")[1]:
            messagebox.showerror("Error", "Please enter a valid email address.")
            return
        
        # Check if email exists
        if self.email_exists(email):
            messagebox.showerror("Error", "A user with this email already exists.")
            return
        
        # Create user
        if self.save_user(first_name, last_name, email, class_name, password):
            messagebox.showinfo("Success", f"User '{first_name} {last_name}' created successfully!")
            self.refresh_callback()
            self.close()
        else:
            messagebox.showerror("Error", "Failed to create user.")

    def email_exists(self, email):
        """Check if email already exists"""
        csv_filename = "student_logins.csv"
        if not os.path.exists(csv_filename):
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

    def save_user(self, first_name, last_name, email, class_name, password):
        """Save user to CSV file"""
        csv_filename = "student_logins.csv"
        file_exists = os.path.isfile(csv_filename)
        
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'class_name': class_name,
            'email': email,
            'password_hash': hashlib.sha256(password.encode()).hexdigest(),
            'login_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['first_name', 'last_name', 'class_name', 'email', 'password_hash', 'login_time']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(user_data)
                return True
        except Exception as e:
            print(f"Error saving user: {e}")
            return False

    def close(self):
        """Close dialog"""
        if self.window:
            self.window.grab_release()
            self.window.destroy()