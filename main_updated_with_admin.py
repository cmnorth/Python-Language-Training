# =================================Enhanced Main Application with Admin System==================================
# main_updated_with_admin.py - Replace your main_updated.py with this version
import tkinter as tk
from tkinter import messagebox
from welcome_window import WelcomeWindow
from menu_window import MenuWindow
from login_window_updated import LoginWindow
from demo_window import DemoWindow
from quiz_window import QuizWindow
from records_window import RecordsWindow
from config_manager import ConfigManager
from theme_manager import ThemeManager
from admin_auth import AdminAuthWindow
from admin_window import AdminWindow

class PythonCommandsApp:
    def __init__(self):
        # Initialize config and theme managers first
        self.config_manager = ConfigManager()
        self.theme_manager = ThemeManager(self.config_manager)
        
        # Apply initial theme
        colors = self.config_manager.get_theme_colors()
        
        self.root = tk.Tk()
        self.root.title("Python Commands Explained")
        
        # Get window dimensions from config
        width = self.config_manager.get_app_setting("window_width", 450)
        height = self.config_manager.get_app_setting("window_height", 700)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        
        # Apply theme to root window
        self.root.configure(bg=colors["background"])
        self.theme_manager.register_widget(self.root, "window")

        # Position window at left center of screen
        self.center_window_left()

        # Track windows and login state
        self.demo_window = None
        self.quiz_window = None
        self.records_window = None
        self.menu_window = None
        self.login_window = None
        self.is_logged_in = False
        self.user_data = None

        # Check if first run
        if self.config_manager.is_first_run():
            self.show_first_run_setup()
        else:
            self.initialize_app()

    def show_first_run_setup(self):
        """Show first run setup dialog"""
        messagebox.showinfo(
            "Welcome to Python Language Training",
            "Welcome! This appears to be your first time running the application.\n\n"
            "Default admin credentials:\n"
            "Username: admin\n"
            "Password: admin123\n\n"
            "Please change these credentials in the Admin Panel after setup.\n"
            "Access the Admin Panel from the main menu."
        )
        
        self.config_manager.set_first_run_complete()
        self.initialize_app()

    def initialize_app(self):
        """Initialize the main application"""
        # Initialize welcome window
        self.welcome_window = WelcomeWindow(self.root, self.show_menu)
        self.welcome_window.show()

    def center_window_left(self):
        """Center window on left side of screen"""
        screen_height = self.root.winfo_screenheight()
        height = self.config_manager.get_app_setting("window_height", 700)
        y_position = (screen_height - height) // 2
        x_position = 50
        
        width = self.config_manager.get_app_setting("window_width", 450)
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

    def show_menu(self):
        """Show main menu with admin integration"""
        # Adjust window size for menu
        menu_height = 500
        self.root.geometry(f"{self.config_manager.get_app_setting('window_width', 450)}x{menu_height}")
        self.center_window_left_menu()

        # Create enhanced menu window
        self.menu_window = EnhancedMenuWindow(
            self.root,
            self.show_demo_with_auth_check,
            self.show_quiz_with_auth_check,
            self.show_records_with_auth_check,
            self.show_login,
            self.exit_program,
            self.config_manager,
            self.theme_manager,
            user_data=self.user_data
        )
        self.menu_window.show()

    def center_window_left_menu(self):
        """Center menu window"""
        screen_height = self.root.winfo_screenheight()
        y_position = (screen_height - 500) // 2
        x_position = 50
        width = self.config_manager.get_app_setting("window_width", 450)
        self.root.geometry(f"{width}x500+{x_position}+{y_position}")

    def show_login(self):
        """Show login window"""
        self.root.geometry(f"{self.config_manager.get_app_setting('window_width', 450)}x700")
        self.center_window_left_login()

        self.login_window = LoginWindow(
            self.root,
            self.show_demo,
            self.on_login_success,
            self.show_menu,
            self.logout_user,
            self.show_quiz,
            self.show_records
        )
        self.login_window.show()

    def center_window_left_login(self):
        """Center login window"""
        screen_height = self.root.winfo_screenheight()
        y_position = (screen_height - 700) // 2
        x_position = 50
        width = self.config_manager.get_app_setting("window_width", 450)
        self.root.geometry(f"{width}x700+{x_position}+{y_position}")

    def on_login_success(self, user_data):
        """Handle successful login"""
        self.is_logged_in = True
        self.user_data = user_data

        if self.menu_window:
            self.menu_window.update_login_status(user_data)

        print(f"User logged in: {user_data['first_name']} {user_data['last_name']}")

    def logout_user(self):
        """Handle user logout"""
        self.is_logged_in = False
        self.user_data = None

        # Close any open windows
        self.close_all_secondary_windows()

        if self.menu_window:
            self.menu_window.update_login_status(None)

        print("User logged out")

    def close_all_secondary_windows(self):
        """Close all demo, quiz, and records windows"""
        if self.demo_window and self.demo_window.window and self.demo_window.window.winfo_exists():
            self.demo_window.close()
        
        if self.quiz_window and self.quiz_window.window and self.quiz_window.window.winfo_exists():
            self.quiz_window.close()
        
        if self.records_window and self.records_window.window and self.records_window.window.winfo_exists():
            self.records_window.close()

    def show_demo_with_auth_check(self, command):
        """Show demo with authentication check"""
        if not self.is_logged_in:
            messagebox.showwarning("Login Required", "Please log in first to access interactive Python demos.")
            self.show_login()
            return

        self.show_demo(command)

    def show_demo(self, command):
        """Show demo window"""
        if not self.is_logged_in:
            messagebox.showwarning("Login Required", "Please log in first to access demos.")
            return

        # Close existing demo window if open
        if self.demo_window and self.demo_window.window and self.demo_window.window.winfo_exists():
            self.demo_window.close()

        self.demo_window = DemoWindow(self.root, command)
        self.demo_window.show()

        print(f"Demo opened: {command} for user {self.user_data['first_name']}")

    def show_quiz_with_auth_check(self, command):
        """Show quiz with authentication check"""
        if not self.is_logged_in:
            messagebox.showwarning("Login Required", "Please log in first to access quizzes.")
            self.show_login()
            return

        self.show_quiz(command)

    def show_quiz(self, command):
        """Show quiz window"""
        if not self.is_logged_in:
            messagebox.showwarning("Login Required", "Please log in first to access quizzes.")
            return

        # Close existing quiz window if open
        if self.quiz_window and self.quiz_window.window and self.quiz_window.window.winfo_exists():
            self.quiz_window.close()

        self.quiz_window = QuizWindow(self.root, command, self.user_data)
        self.quiz_window.show()

        print(f"Quiz opened: {command} for user {self.user_data['first_name']}")

    def show_records_with_auth_check(self):
        """Show records with authentication check"""
        if not self.is_logged_in:
            messagebox.showwarning("Login Required", "Please log in first to view records.")
            self.show_login()
            return

        self.show_records()

    def show_records(self):
        """Show records window"""
        if not self.is_logged_in:
            messagebox.showwarning("Login Required", "Please log in first to view records.")
            return

        # Close existing records window if open
        if self.records_window and self.records_window.window and self.records_window.window.winfo_exists():
            self.records_window.close()

        self.records_window = RecordsWindow(self.root, self.user_data)
        self.records_window.show()

        print(f"Records opened for user {self.user_data['first_name']}")

    def exit_program(self):
        """Exit the application"""
        self.close_all_secondary_windows()
        print("Application closing...")
        self.root.quit()
        self.root.destroy()

    def run(self):
        """Run the application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nApplication interrupted by user")
            self.exit_program()
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.exit_program()


class EnhancedMenuWindow(MenuWindow):
    """Enhanced menu window with admin panel access"""
    
    def __init__(self, root, demo_callback, quiz_callback, records_callback, 
                 login_callback, exit_callback, config_manager, theme_manager, user_data=None):
        # Initialize parent class
        super().__init__(root, demo_callback, quiz_callback, records_callback, 
                        login_callback, exit_callback, user_data)
        
        # Add admin system integration
        self.config_manager = config_manager
        self.theme_manager = theme_manager

    def create_bottom_buttons(self, parent):
        """Override to include admin button"""
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


# Run the application
if __name__ == "__main__":
    print("Starting Python Commands Explained application with Admin System...")
    app = PythonCommandsApp()
    app.run()