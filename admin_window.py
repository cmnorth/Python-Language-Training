# =================================Admin Window System==================================
# admin_window.py - Main administrative interface
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
import shutil
from datetime import datetime
import hashlib
from user_management import CreateUserDialog

class AdminWindow:
    def __init__(self, parent_root, config_manager, theme_manager):
        self.parent_root = parent_root
        self.config_manager = config_manager
        self.theme_manager = theme_manager
        self.window = None
        
        # Admin settings variables
        self.admin_username_var = tk.StringVar()
        self.admin_email_var = tk.StringVar()
        self.admin_password_var = tk.StringVar()
        self.admin_confirm_password_var = tk.StringVar()
        
        # User management variables
        self.selected_user = None
        self.user_listbox = None
        
        # Theme variables
        self.theme_var = tk.StringVar()

    def show(self):
        """Display the admin window"""
        self.window = tk.Toplevel(self.parent_root)
        self.window.title("🛠️ Administrator Panel")
        self.window.geometry("900x700")
        self.window.resizable(True, True)
        
        # Position window
        self.center_window()
        
        # Apply current theme
        colors = self.config_manager.get_theme_colors()
        self.window.configure(bg=colors["background"])
        
        self.create_interface(colors)
        self.load_admin_settings()
        self.refresh_user_list()

    def center_window(self):
        """Center the window on screen"""
        self.window.update_idletasks()
        width = 900
        height = 700
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def create_interface(self, colors):
        """Create the admin interface"""
        # Create notebook for tabs
        notebook = ttk.Notebook(self.window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_user_management_tab(notebook, colors)
        self.create_admin_settings_tab(notebook, colors)
        self.create_theme_settings_tab(notebook, colors)
        self.create_system_settings_tab(notebook, colors)
        
        # Bottom buttons
        self.create_bottom_buttons(colors)

    def create_user_management_tab(self, notebook, colors):
        """Create user management tab"""
        user_frame = tk.Frame(notebook, bg=colors["background"])
        notebook.add(user_frame, text="👥 User Management")
        
        # User list section
        list_frame = tk.LabelFrame(user_frame, text="Registered Users", 
                                  font=('Arial', 12, 'bold'),
                                  bg=colors["background"], fg=colors["text"])
        list_frame.pack(fill='both', expand=True, padx=10, pady=(10, 5))
        
        # User listbox with scrollbar
        list_container = tk.Frame(list_frame, bg=colors["background"])
        list_container.pack(fill='both', expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(list_container)
        scrollbar.pack(side='right', fill='y')
        
        self.user_listbox = tk.Listbox(list_container, 
                                      yscrollcommand=scrollbar.set,
                                      font=('Arial', 10),
                                      height=15)
        self.user_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.user_listbox.yview)
        
        self.user_listbox.bind('<<ListboxSelect>>', self.on_user_select)
        
        # User actions section
        actions_frame = tk.LabelFrame(user_frame, text="User Actions",
                                     font=('Arial', 12, 'bold'),
                                     bg=colors["background"], fg=colors["text"])
        actions_frame.pack(fill='x', padx=10, pady=5)
        
        # Action buttons
        button_frame = tk.Frame(actions_frame, bg=colors["background"])
        button_frame.pack(fill='x', padx=5, pady=5)
        
        self.create_user_btn = tk.Button(button_frame, text="➕ Create User",
                                        command=self.create_new_user,
                                        bg=colors["primary"], fg="white",
                                        font=('Arial', 10, 'bold'))
        self.create_user_btn.pack(side='left', padx=(0, 5))
        
        self.reset_password_btn = tk.Button(button_frame, text="🔑 Reset Password",
                                           command=self.reset_user_password,
                                           bg=colors["warning"], fg="white",
                                           font=('Arial', 10))
        self.reset_password_btn.pack(side='left', padx=5)
        
        self.delete_user_btn = tk.Button(button_frame, text="🗑️ Delete User",
                                        command=self.delete_user,
                                        bg=colors["danger"], fg="white",
                                        font=('Arial', 10))
        self.delete_user_btn.pack(side='left', padx=5)
        
        self.delete_all_btn = tk.Button(button_frame, text="⚠️ Delete ALL Users",
                                       command=self.delete_all_users,
                                       bg=colors["danger"], fg="white",
                                       font=('Arial', 10, 'bold'))
        self.delete_all_btn.pack(side='right')
        
        # User info display
        info_frame = tk.LabelFrame(actions_frame, text="Selected User Information",
                                  font=('Arial', 10, 'bold'),
                                  bg=colors["background"], fg=colors["text"])
        info_frame.pack(fill='x', padx=5, pady=(10, 5))
        
        self.user_info_text = tk.Text(info_frame, height=4, width=50,
                                     bg=colors["frame_bg"], fg=colors["text"],
                                     font=('Arial', 9), state='disabled')
        self.user_info_text.pack(fill='x', padx=5, pady=5)

    def create_admin_settings_tab(self, notebook, colors):
        """Create admin settings tab"""
        admin_frame = tk.Frame(notebook, bg=colors["background"])
        notebook.add(admin_frame, text="⚙️ Admin Settings")
        
        # Current admin info
        current_frame = tk.LabelFrame(admin_frame, text="Current Admin Information",
                                     font=('Arial', 12, 'bold'),
                                     bg=colors["background"], fg=colors["text"])
        current_frame.pack(fill='x', padx=10, pady=(10, 5))
        
        admin_info = self.config_manager.config["admin"]
        current_info = f"Username: {admin_info['username']}\n"
        current_info += f"Email: {admin_info['email']}\n"
        current_info += f"Created: {admin_info.get('created_date', 'Unknown')}\n"
        current_info += f"Last Updated: {admin_info.get('last_updated', 'Never')}"
        
        current_label = tk.Label(current_frame, text=current_info,
                                font=('Arial', 10), bg=colors["background"],
                                fg=colors["text"], justify='left')
        current_label.pack(anchor='w', padx=10, pady=5)
        
        # Update admin settings
        update_frame = tk.LabelFrame(admin_frame, text="Update Admin Credentials",
                                    font=('Arial', 12, 'bold'),
                                    bg=colors["background"], fg=colors["text"])
        update_frame.pack(fill='x', padx=10, pady=5)
        
        # Form fields
        fields_frame = tk.Frame(update_frame, bg=colors["background"])
        fields_frame.pack(fill='x', padx=10, pady=10)
        
        # Username
        tk.Label(fields_frame, text="New Username:", font=('Arial', 10),
                bg=colors["background"], fg=colors["text"]).grid(row=0, column=0, sticky='w', pady=2)
        username_entry = tk.Entry(fields_frame, textvariable=self.admin_username_var,
                                 font=('Arial', 10), width=30)
        username_entry.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Email
        tk.Label(fields_frame, text="New Email:", font=('Arial', 10),
                bg=colors["background"], fg=colors["text"]).grid(row=1, column=0, sticky='w', pady=2)
        email_entry = tk.Entry(fields_frame, textvariable=self.admin_email_var,
                              font=('Arial', 10), width=30)
        email_entry.grid(row=1, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Password
        tk.Label(fields_frame, text="New Password:", font=('Arial', 10),
                bg=colors["background"], fg=colors["text"]).grid(row=2, column=0, sticky='w', pady=2)
        password_entry = tk.Entry(fields_frame, textvariable=self.admin_password_var,
                                 font=('Arial', 10), width=30, show="*")
        password_entry.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Confirm Password
        tk.Label(fields_frame, text="Confirm Password:", font=('Arial', 10),
                bg=colors["background"], fg=colors["text"]).grid(row=3, column=0, sticky='w', pady=2)
        confirm_entry = tk.Entry(fields_frame, textvariable=self.admin_confirm_password_var,
                                font=('Arial', 10), width=30, show="*")
        confirm_entry.grid(row=3, column=1, sticky='w', padx=(10, 0), pady=2)
        
        # Update button
        update_btn = tk.Button(update_frame, text="🔄 Update Admin Settings",
                              command=self.update_admin_settings,
                              bg=colors["primary"], fg="white",
                              font=('Arial', 11, 'bold'))
        update_btn.pack(pady=10)

    def create_theme_settings_tab(self, notebook, colors):
        """Create theme settings tab"""
        theme_frame = tk.Frame(notebook, bg=colors["background"])
        notebook.add(theme_frame, text="🎨 Theme Settings")
        
        # Theme selection
        selection_frame = tk.LabelFrame(theme_frame, text="Color Scheme",
                                       font=('Arial', 12, 'bold'),
                                       bg=colors["background"], fg=colors["text"])
        selection_frame.pack(fill='x', padx=10, pady=(10, 5))
        
        # Theme options
        themes = self.theme_manager.get_available_themes()
        current_theme = self.theme_manager.get_current_theme()
        self.theme_var.set(current_theme)
        
        for theme in themes:
            theme_display = {
                "light": "☀️ Light Mode",
                "dark": "🌙 Dark Mode", 
                "night": "🌌 Night Mode (Reduced Blue Light)"
            }
            
            rb = tk.Radiobutton(selection_frame,
                               text=theme_display.get(theme, theme.title()),
                               variable=self.theme_var,
                               value=theme,
                               command=self.change_theme,
                               font=('Arial', 11),
                               bg=colors["background"],
                               fg=colors["text"],
                               selectcolor=colors["frame_bg"])
            rb.pack(anchor='w', padx=10, pady=5)
        
        # Theme preview
        preview_frame = tk.LabelFrame(theme_frame, text="Theme Preview",
                                     font=('Arial', 12, 'bold'),
                                     bg=colors["background"], fg=colors["text"])
        preview_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create preview widgets
        self.create_theme_preview(preview_frame, colors)

    def create_theme_preview(self, parent, colors):
        """Create theme preview widgets"""
        preview_container = tk.Frame(parent, bg=colors["background"])
        preview_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Sample widgets
        tk.Label(preview_container, text="Sample Text",
                font=('Arial', 12), bg=colors["background"],
                fg=colors["text"]).pack(pady=5)
        
        btn_frame = tk.Frame(preview_container, bg=colors["background"])
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Primary Button",
                 bg=colors["primary"], fg="white",
                 font=('Arial', 10)).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Secondary Button",
                 bg=colors["secondary"], fg="white",
                 font=('Arial', 10)).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Warning Button",
                 bg=colors["warning"], fg="white",
                 font=('Arial', 10)).pack(side='left', padx=5)
        
        sample_frame = tk.Frame(preview_container, bg=colors["frame_bg"],
                               relief='raised', bd=2)
        sample_frame.pack(fill='x', pady=10)
        
        tk.Label(sample_frame, text="Sample Frame Content",
                font=('Arial', 10), bg=colors["frame_bg"],
                fg=colors["text"]).pack(pady=10)

    def create_system_settings_tab(self, notebook, colors):
        """Create system settings tab"""
        system_frame = tk.Frame(notebook, bg=colors["background"])
        notebook.add(system_frame, text="🖥️ System Settings")
        
        # Backup section
        backup_frame = tk.LabelFrame(system_frame, text="Data Management",
                                    font=('Arial', 12, 'bold'),
                                    bg=colors["background"], fg=colors["text"])
        backup_frame.pack(fill='x', padx=10, pady=(10, 5))
        
        backup_info = tk.Label(backup_frame,
                              text="Create backups of user data and configuration settings",
                              font=('Arial', 10), bg=colors["background"],
                              fg=colors["text"])
        backup_info.pack(pady=5)
        
        backup_btn_frame = tk.Frame(backup_frame, bg=colors["background"])
        backup_btn_frame.pack(pady=10)
        
        tk.Button(backup_btn_frame, text="💾 Backup All Data",
                 command=self.backup_data,
                 bg=colors["secondary"], fg="white",
                 font=('Arial', 10)).pack(side='left', padx=5)
        
        tk.Button(backup_btn_frame, text="📁 Restore Data",
                 command=self.restore_data,
                 bg=colors["warning"], fg="white",
                 font=('Arial', 10)).pack(side='left', padx=5)
        
        # Reset section
        reset_frame = tk.LabelFrame(system_frame, text="System Reset",
                                   font=('Arial', 12, 'bold'),
                                   bg=colors["background"], fg=colors["text"])
        reset_frame.pack(fill='x', padx=10, pady=5)
        
        reset_info = tk.Label(reset_frame,
                             text="⚠️ Reset system to defaults for software transfer.\n"
                                  "This will keep theme settings but reset admin credentials.",
                             font=('Arial', 10), bg=colors["background"],
                             fg=colors["warning"], justify='center')
        reset_info.pack(pady=5)
        
        tk.Button(reset_frame, text="🔄 Reset to Defaults",
                 command=self.reset_to_defaults,
                 bg=colors["danger"], fg="white",
                 font=('Arial', 11, 'bold')).pack(pady=10)

    def create_bottom_buttons(self, colors):
        """Create bottom control buttons"""
        bottom_frame = tk.Frame(self.window, bg=colors["background"])
        bottom_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(bottom_frame, text="❌ Close Admin Panel",
                 command=self.close,
                 bg=colors["danger"], fg="white",
                 font=('Arial', 11, 'bold')).pack(side='right')

    # User Management Methods
    def refresh_user_list(self):
        """Refresh the user list display"""
        self.user_listbox.delete(0, tk.END)
        
        csv_filename = "student_logins.csv"
        if os.path.exists(csv_filename):
            try:
                with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        display_text = f"{row['first_name']} {row['last_name']} ({row['email']})"
                        self.user_listbox.insert(tk.END, display_text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load user data: {str(e)}")

    def on_user_select(self, event):
        """Handle user selection"""
        selection = self.user_listbox.curselection()
        if selection:
            index = selection[0]
            # Get user data
            csv_filename = "student_logins.csv"
            if os.path.exists(csv_filename):
                try:
                    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile)
                        users = list(reader)
                        if index < len(users):
                            self.selected_user = users[index]
                            self.display_user_info()
                except Exception as e:
                    print(f"Error loading user: {e}")

    def display_user_info(self):
        """Display selected user information"""
        if self.selected_user:
            self.user_info_text.config(state='normal')
            self.user_info_text.delete('1.0', tk.END)
            
            info = f"Name: {self.selected_user['first_name']} {self.selected_user['last_name']}\n"
            info += f"Email: {self.selected_user['email']}\n"
            info += f"Class: {self.selected_user.get('class_name', 'Not specified')}\n"
            info += f"Registration: {self.selected_user.get('login_time', 'Unknown')}"
            
            self.user_info_text.insert('1.0', info)
            self.user_info_text.config(state='disabled')

    def create_new_user(self):
        """Create a new user account"""
        CreateUserDialog(self.window, self.config_manager, self.refresh_user_list)

    def reset_user_password(self):
        """Reset selected user's password"""
        if not self.selected_user:
            messagebox.showwarning("No Selection", "Please select a user first.")
            return
        
        from tkinter import simpledialog
        
        new_password = simpledialog.askstring(
            "Reset Password",
            f"Enter new password for {self.selected_user['first_name']} {self.selected_user['last_name']}:",
            show='*'
        )
        
        if new_password:
            if len(new_password) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters long.")
                return
            
            # Update password in CSV
            if self.update_user_password(self.selected_user['email'], new_password):
                messagebox.showinfo("Success", "Password reset successfully!")
            else:
                messagebox.showerror("Error", "Failed to reset password.")

    def update_user_password(self, email, new_password):
        """Update user password in CSV file"""
        csv_filename = "student_logins.csv"
        if not os.path.exists(csv_filename):
            return False
        
        try:
            # Read all users
            with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                users = list(reader)
            
            # Update password
            hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
            for user in users:
                if user['email'] == email:
                    user['password_hash'] = hashed_password
                    break
            
            # Write back to file
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['first_name', 'last_name', 'class_name', 'email', 'password_hash', 'login_time']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(users)
            
            return True
        except Exception as e:
            print(f"Error updating password: {e}")
            return False

    def delete_user(self):
        """Delete selected user"""
        if not self.selected_user:
            messagebox.showwarning("No Selection", "Please select a user first.")
            return
        
        user_name = f"{self.selected_user['first_name']} {self.selected_user['last_name']}"
        if messagebox.askyesno("Confirm Delete", 
                              f"Are you sure you want to delete user '{user_name}'?\n\n"
                              f"This will also delete all their quiz progress."):
            if self.delete_user_from_csv(self.selected_user['email']):
                self.delete_user_progress(self.selected_user['email'])
                self.refresh_user_list()
                self.user_info_text.config(state='normal')
                self.user_info_text.delete('1.0', tk.END)
                self.user_info_text.config(state='disabled')
                messagebox.showinfo("Success", f"User '{user_name}' deleted successfully!")
            else:
                messagebox.showerror("Error", "Failed to delete user.")

    def delete_user_from_csv(self, email):
        """Delete user from CSV file"""
        csv_filename = "student_logins.csv"
        if not os.path.exists(csv_filename):
            return False
        
        try:
            # Read all users except the one to delete
            with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                users = [user for user in reader if user['email'] != email]
            
            # Write back to file
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['first_name', 'last_name', 'class_name', 'email', 'password_hash', 'login_time']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(users)
            
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def delete_user_progress(self, email):
        """Delete user's quiz progress files"""
        email_safe = email.replace('@', '_').replace('.', '_')
        topics = ['str', 'print', 'len', 'type', 'range', 'list', 'dict', 
                 'for_loop', 'if_statement', 'def']
        
        for topic in topics:
            progress_file = f"quiz_progress_{topic}_{email_safe}.json"
            if os.path.exists(progress_file):
                try:
                    os.remove(progress_file)
                except Exception as e:
                    print(f"Error deleting progress file {progress_file}: {e}")

    def delete_all_users(self):
        """Delete all user accounts"""
        if messagebox.askyesno("⚠️ CONFIRM DELETE ALL", 
                              "Are you ABSOLUTELY SURE you want to delete ALL users?\n\n"
                              "This action cannot be undone!\n"
                              "All user accounts and progress will be permanently deleted."):
            # Double confirmation
            if messagebox.askyesno("⚠️ FINAL CONFIRMATION", 
                                  "This is your FINAL warning!\n\n"
                                  "Click YES to permanently delete ALL user data."):
                self.perform_delete_all()

    def perform_delete_all(self):
        """Perform the actual deletion of all users"""
        try:
            # Delete CSV file
            csv_filename = "student_logins.csv"
            if os.path.exists(csv_filename):
                os.remove(csv_filename)
            
            # Delete all progress files
            for filename in os.listdir('.'):
                if filename.startswith('quiz_progress_') and filename.endswith('.json'):
                    os.remove(filename)
            
            self.refresh_user_list()
            self.user_info_text.config(state='normal')
            self.user_info_text.delete('1.0', tk.END)
            self.user_info_text.config(state='disabled')
            
            messagebox.showinfo("Success", "All user accounts and progress data deleted successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete all users: {str(e)}")

    # Admin Settings Methods
    def load_admin_settings(self):
        """Load current admin settings into form"""
        admin_config = self.config_manager.config["admin"]
        self.admin_username_var.set(admin_config["username"])
        self.admin_email_var.set(admin_config["email"])

    def update_admin_settings(self):
        """Update admin credentials"""
        username = self.admin_username_var.get().strip()
        email = self.admin_email_var.get().strip()
        password = self.admin_password_var.get().strip()
        confirm = self.admin_confirm_password_var.get().strip()
        
        # Validation
        if not username or not email:
            messagebox.showerror("Error", "Username and email are required.")
            return
        
        if password:  # Only validate password if it's being changed
            if len(password) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters long.")
                return
            
            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match.")
                return
        
        # Update credentials
        if password:
            success = self.config_manager.update_admin_credentials(username, password, email)
        else:
            # Update only username and email, keep current password
            self.config_manager.config["admin"]["username"] = username
            self.config_manager.config["admin"]["email"] = email
            self.config_manager.config["admin"]["last_updated"] = datetime.now().isoformat()
            success = self.config_manager.save_config()
        
        if success:
            messagebox.showinfo("Success", "Admin settings updated successfully!")
            # Clear password fields
            self.admin_password_var.set("")
            self.admin_confirm_password_var.set("")
            # Reload settings display
            self.load_admin_settings()
        else:
            messagebox.showerror("Error", "Failed to update admin settings.")

    # Theme Methods
    def change_theme(self):
        """Change application theme"""
        new_theme = self.theme_var.get()
        if self.theme_manager.set_theme(new_theme):
            # Update current window
            colors = self.config_manager.get_theme_colors()
            self.window.configure(bg=colors["background"])
            # Note: Full theme update would require recreating the interface
            messagebox.showinfo("Theme Changed", 
                               f"Theme changed to {new_theme.title()} mode!\n"
                               f"Restart the application to see full theme changes.")

    # System Methods
    def backup_data(self):
        """Backup all application data"""
        try:
            backup_dir = filedialog.askdirectory(title="Select Backup Directory")
            if not backup_dir:
                return
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_folder = os.path.join(backup_dir, f"PythonTraining_Backup_{timestamp}")
            os.makedirs(backup_folder, exist_ok=True)
            
            # Backup files
            files_to_backup = [
                "student_logins.csv",
                "app_config.json"
            ]
            
            # Add progress files
            for filename in os.listdir('.'):
                if filename.startswith('quiz_progress_') and filename.endswith('.json'):
                    files_to_backup.append(filename)
            
            # Copy files
            backed_up = []
            for file in files_to_backup:
                if os.path.exists(file):
                    shutil.copy2(file, backup_folder)
                    backed_up.append(file)
            
            messagebox.showinfo("Backup Complete", 
                               f"Backup created successfully!\n\n"
                               f"Location: {backup_folder}\n"
                               f"Files backed up: {len(backed_up)}")
            
        except Exception as e:
            messagebox.showerror("Backup Error", f"Failed to create backup: {str(e)}")

    def restore_data(self):
        """Restore application data from backup"""
        backup_dir = filedialog.askdirectory(title="Select Backup Directory to Restore")
        if not backup_dir:
            return
        
        if messagebox.askyesno("Confirm Restore", 
                              "⚠️ Restoring data will overwrite current data!\n\n"
                              "Are you sure you want to continue?"):
            try:
                # Find files to restore
                restored = []
                for filename in os.listdir(backup_dir):
                    if (filename == "student_logins.csv" or 
                        filename == "app_config.json" or
                        (filename.startswith('quiz_progress_') and filename.endswith('.json'))):
                        
                        src = os.path.join(backup_dir, filename)
                        dst = filename
                        shutil.copy2(src, dst)
                        restored.append(filename)
                
                messagebox.showinfo("Restore Complete",
                                   f"Data restored successfully!\n\n"
                                   f"Files restored: {len(restored)}\n"
                                   f"Please restart the application.")
                
            except Exception as e:
                messagebox.showerror("Restore Error", f"Failed to restore data: {str(e)}")

    def reset_to_defaults(self):
        """Reset system to defaults"""
        if messagebox.askyesno("Confirm Reset", 
                              "⚠️ This will reset admin credentials to defaults!\n\n"
                              "Current theme will be preserved.\n"
                              "Are you sure you want to continue?"):
            if self.config_manager.reset_to_defaults():
                messagebox.showinfo("Reset Complete", 
                                   "System reset to defaults!\n\n"
                                   "Default admin credentials:\n"
                                   "Username: admin\n"
                                   "Password: admin123\n\n"
                                   "Please restart the application.")
                self.close()
            else:
                messagebox.showerror("Error", "Failed to reset to defaults.")

    def close(self):
        """Close admin window"""
        if self.window:
            self.window.destroy()