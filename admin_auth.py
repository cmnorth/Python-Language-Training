# =================================Admin Authentication Window==================================
# admin_auth.py - Admin login and authentication
import tkinter as tk
from tkinter import messagebox

class AdminAuthWindow:
    def __init__(self, parent_root, config_manager, success_callback):
        self.parent_root = parent_root
        self.config_manager = config_manager
        self.success_callback = success_callback
        self.window = None
        
        # Login fields
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

    def show(self):
        """Display admin authentication window"""
        self.window = tk.Toplevel(self.parent_root)
        self.window.title("Administrator Login")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Make it modal
        self.window.transient(self.parent_root)
        self.window.grab_set()
        
        # Apply current theme
        colors = self.config_manager.get_theme_colors()
        self.window.configure(bg=colors["background"])
        
        self.create_interface(colors)

    def center_window(self):
        """Center the window on screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"+{x}+{y}")

    def create_interface(self, colors):
        """Create the authentication interface"""
        main_frame = tk.Frame(self.window, bg=colors["background"])
        main_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Title
        title_label = tk.Label(main_frame,
                              text="🔐 Administrator Access",
                              font=('Arial', 16, 'bold'),
                              bg=colors["background"],
                              fg=colors["text"])
        title_label.pack(pady=(0, 20))
        
        # Warning message
        warning_label = tk.Label(main_frame,
                                text="⚠️ Administrative access required\nEnter admin credentials to continue",
                                font=('Arial', 10),
                                bg=colors["background"],
                                fg=colors["warning"],
                                justify='center')
        warning_label.pack(pady=(0, 20))
        
        # Login form
        form_frame = tk.Frame(main_frame, bg=colors["background"])
        form_frame.pack(fill='x', pady=10)
        
        # Username
        tk.Label(form_frame, text="Username:", font=('Arial', 10), 
                bg=colors["background"], fg=colors["text"]).pack(anchor='w')
        username_entry = tk.Entry(form_frame, textvariable=self.username_var, 
                                 font=('Arial', 11), width=25)
        username_entry.pack(fill='x', pady=(2, 10))
        username_entry.focus_set()
        
        # Password
        tk.Label(form_frame, text="Password:", font=('Arial', 10),
                bg=colors["background"], fg=colors["text"]).pack(anchor='w')
        password_entry = tk.Entry(form_frame, textvariable=self.password_var,
                                 font=('Arial', 11), width=25, show="*")
        password_entry.pack(fill='x', pady=(2, 20))
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=colors["background"])
        button_frame.pack(fill='x', pady=10)
        
        login_btn = tk.Button(button_frame,
                             text="Login",
                             font=('Arial', 11, 'bold'),
                             command=self.authenticate,
                             bg=colors["primary"],
                             fg="white",
                             relief='raised',
                             bd=2,
                             width=12)
        login_btn.pack(side='left', padx=(0, 10))
        
        cancel_btn = tk.Button(button_frame,
                              text="Cancel", 
                              font=('Arial', 11),
                              command=self.close,
                              bg=colors["danger"],
                              fg="white",
                              relief='raised',
                              bd=2,
                              width=12)
        cancel_btn.pack(side='right')
        
        # Default admin info (remove in production)
        if self.config_manager.is_first_run():
            info_frame = tk.Frame(main_frame, bg=colors["frame_bg"], relief='raised', bd=1)
            info_frame.pack(fill='x', pady=(20, 0))
            
            info_label = tk.Label(info_frame,
                                 text="Default Admin Credentials:\nUsername: admin\nPassword: admin123",
                                 font=('Arial', 9),
                                 bg=colors["frame_bg"],
                                 fg=colors["text"],
                                 justify='center')
            info_label.pack(pady=5)
        
        # Bind Enter key to login
        self.window.bind('<Return>', lambda e: self.authenticate())

    def authenticate(self):
        """Authenticate admin credentials"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        if self.config_manager.verify_admin_credentials(username, password):
            self.close()
            self.success_callback()
        else:
            messagebox.showerror("Authentication Failed", 
                               "Invalid admin credentials.\nPlease check your username and password.")
            self.password_var.set("")  # Clear password field

    def close(self):
        """Close the authentication window"""
        if self.window:
            self.window.grab_release()
            self.window.destroy()
