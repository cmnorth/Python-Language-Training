# =================================Menu Window Integration with Admin==================================
# menu_window_integration.py - Add this to your menu_window.py file

def add_admin_integration_to_menu(menu_window_class):
    """
    This function shows how to integrate admin functionality into your existing menu window.
    You can either modify your existing menu_window.py file or create a new one.
    """
    
    # Add these imports to the top of your menu_window.py:
    """
    from config_manager import ConfigManager
    from theme_manager import ThemeManager
    from admin_auth import AdminAuthWindow
    from admin_window import AdminWindow
    """
    
    # Add this to your MenuWindow.__init__ method:
    """
    def __init__(self, root, demo_callback, quiz_callback, records_callback, 
                 login_callback, exit_callback, user_data=None):
        # ... existing code ...
        
        # Add these lines:
        self.config_manager = ConfigManager()
        self.theme_manager = ThemeManager(self.config_manager)
        
        # Apply theme to root window
        colors = self.config_manager.get_theme_colors()
        self.root.configure(bg=colors["background"])
    """
    
    # Modify your create_bottom_buttons method to include admin button:
    def create_bottom_buttons_with_admin(self, parent):
        """Modified version of create_bottom_buttons with admin access"""
        colors = self.config_manager.get_theme_colors()
        
        bottom_frame = tk.Frame(parent, bg=colors["background"])
        bottom_frame.pack(side='bottom', fill='x', pady=(20, 0))

        # Admin button (always visible)
        admin_btn = tk.Button(bottom_frame,
                              text="🛠️ Admin Panel",
                              font=('Arial', 10),
                              width=12,
                              height=2,
                              command=self.show_admin_panel,
                              bg=colors["logout"],  # Purple color for admin
                              fg="white",
                              relief='raised',
                              bd=2)
        admin_btn.pack(side='left', padx=(0, 5))

        if self.is_logged_in:
            account_button = tk.Button(bottom_frame,
                                     text="👤 Account Settings",
                                     font=('Arial', 11),
                                     width=15,
                                     height=2,
                                     command=self.login_callback,
                                     bg=colors["secondary"],
                                     fg="white",
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
                                   bg=colors["primary"],
                                   fg="white",
                                   relief='raised',
                                   bd=2)
            login_button.pack(side='left', padx=5)

        exit_button = tk.Button(bottom_frame,
                              text="❌ Exit Application",
                              font=('Arial', 11),
                              width=15,
                              height=2,
                              command=self.exit_callback,
                              bg=colors["danger"],
                              fg="white",
                              relief='raised',
                              bd=2)
        exit_button.pack(side='right')
    
    # Add this method to your MenuWindow class:
    def show_admin_panel(self):
        """Show admin authentication and panel"""
        def on_admin_auth_success():
            """Callback when admin authentication succeeds"""
            admin_window = AdminWindow(
                self.root,
                self.config_manager,
                self.theme_manager
            )
            admin_window.show()
        
        # Show admin authentication window
        auth_window = AdminAuthWindow(
            self.root,
            self.config_manager,
            on_admin_auth_success
        )
        auth_window.show()

# Example of how to modify your existing demo files to fix code display:
def update_demo_file_for_better_code_display():
    """
    Add this to your demo files (like demo_print.py, demo_len.py, etc.)
    Replace the usage_text creation section with this:
    """
    
    # Instead of:
    # usage_text = tk.Text(usage_frame, height=4, font=('Courier', 10), 
    #                    bg='#f8f8f8', relief='flat', wrap='word')
    # usage_text.pack(fill='x', padx=10, pady=5)
    # usage_text.insert('1.0', 'print("Hello")\nprint("World")')
    # usage_text.config(state='disabled')
    
    # Use this:
    """
    from demo_display_utils import CodeDisplayManager
    
    # Multi-line code examples
    usage_examples = '''print("Hello, World!")
name = input("Enter your name: ")
print(f"Hello, {name}!")
for i in range(3):
    print(f"Count: {i}")'''
    
    # Create properly formatted code display
    CodeDisplayManager.update_demo_usage_section(main_frame, usage_examples, colors)
    """