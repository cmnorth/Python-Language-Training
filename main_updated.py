# =================================Updated Main Application with Quiz System==================================
# main_updated.py - Enhanced main application with quiz and records functionality
import tkinter as tk
from welcome_window import WelcomeWindow
from menu_window import MenuWindow
from login_window_updated import LoginWindow
from demo_window import DemoWindow
from quiz_window import QuizWindow
from records_window import RecordsWindow

class PythonCommandsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Commands Explained")
        self.root.geometry("450x700")
        self.root.resizable(False, False)

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

        # Initialize welcome window
        self.welcome_window = WelcomeWindow(self.root, self.show_menu)
        self.welcome_window.show()

    def center_window_left(self):
        screen_height = self.root.winfo_screenheight()
        y_position = (screen_height - 700) // 2
        x_position = 50
        self.root.geometry(f"450x700+{x_position}+{y_position}")  # Updated width to 450

    def show_menu(self):
        self.root.geometry("450x500")  # Updated width to 450
        self.center_window_left_menu()

        self.menu_window = MenuWindow(
            self.root,
            self.show_demo_with_auth_check,
            self.show_quiz_with_auth_check,
            self.show_records_with_auth_check,
            self.show_login,
            self.exit_program,
            user_data=self.user_data
        )
        self.menu_window.show()

    def show_login(self):
        self.root.geometry("450x700")  # Updated width to 450
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

    def center_window_left_menu(self):
        screen_height = self.root.winfo_screenheight()
        y_position = (screen_height - 500) // 2
        x_position = 50
        self.root.geometry(f"450x500+{x_position}+{y_position}")  # Updated width to 450

    def center_window_left_login(self):
        screen_height = self.root.winfo_screenheight()
        y_position = (screen_height - 700) // 2
        x_position = 50
        self.root.geometry(f"450x700+{x_position}+{y_position}")  # Updated width to 450

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
            from tkinter import messagebox
            messagebox.showwarning("Login Required", "Please log in first to access interactive Python demos.")
            self.show_login()
            return

        self.show_demo(command)

    def show_demo(self, command):
        """Show demo window"""
        if not self.is_logged_in:
            from tkinter import messagebox
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
            from tkinter import messagebox
            messagebox.showwarning("Login Required", "Please log in first to access quizzes.")
            self.show_login()
            return

        self.show_quiz(command)

    def show_quiz(self, command):
        """Show quiz window"""
        if not self.is_logged_in:
            from tkinter import messagebox
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
            from tkinter import messagebox
            messagebox.showwarning("Login Required", "Please log in first to view records.")
            self.show_login()
            return

        self.show_records()

    def show_records(self):
        """Show records window"""
        if not self.is_logged_in:
            from tkinter import messagebox
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

# Run the application
if __name__ == "__main__":
    print("Starting Python Commands Explained application...")
    app = PythonCommandsApp()
    app.run()
