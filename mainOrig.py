# =================================Version 08 - CLEAN DEMO-ONLY==================================
# main.py - Clean main application controller without quiz functionality
import tkinter as tk
from welcome_window import WelcomeWindow
from menu_window import MenuWindow
from login_window import LoginWindow
from demo_window import DemoWindow

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
        self.root.geometry(f"400x700+{x_position}+{y_position}")

    def show_menu(self):
        self.root.geometry("400x500")
        self.center_window_left_menu()

        self.menu_window = MenuWindow(
            self.root,
            self.show_demo_with_auth_check,
            self.show_login,
            self.exit_program,
            user_data=self.user_data
        )
        self.menu_window.show()

    def show_login(self):
        self.root.geometry("400x700")
        self.center_window_left_login()

        self.login_window = LoginWindow(
            self.root,
            self.show_demo,
            self.on_login_success,
            self.show_menu,
            self.logout_user,
            quiz_callback=None  # No longer used
        )
        self.login_window.show()

    def center_window_left_menu(self):
        screen_height = self.root.winfo_screenheight()
        y_position = (screen_height - 500) // 2
        x_position = 50
        self.root.geometry(f"400x500+{x_position}+{y_position}")

    def center_window_left_login(self):
        screen_height = self.root.winfo_screenheight()
        y_position = (screen_height - 700) // 2
        x_position = 50
        self.root.geometry(f"400x700+{x_position}+{y_position}")

    def on_login_success(self, user_data):
        self.is_logged_in = True
        self.user_data = user_data

        if self.menu_window:
            self.menu_window.update_login_status(user_data)

        print(f"User logged in: {user_data['first_name']} {user_data['last_name']}")

    def logout_user(self):
        self.is_logged_in = False
        self.user_data = None

        if self.demo_window and self.demo_window.window and self.demo_window.window.winfo_exists():
            self.demo_window.close()

        if self.menu_window:
            self.menu_window.update_login_status(None)

        print("User logged out")

    def show_demo_with_auth_check(self, command):
        if not self.is_logged_in:
            from tkinter import messagebox
            messagebox.showwarning("Login Required", "Please log in first to access interactive Python demos.")
            self.show_login()
            return

        self.show_demo(command)

    def show_demo(self, command):
        if not self.is_logged_in:
            from tkinter import messagebox
            messagebox.showwarning("Login Required", "Please log in first to access demos.")
            return

        if self.demo_window and self.demo_window.window and self.demo_window.window.winfo_exists():
            self.demo_window.close()

        self.demo_window = DemoWindow(self.root, command)
        self.demo_window.show()

        print(f"Demo opened: {command} for user {self.user_data['first_name']}")

    def exit_program(self):
        if self.demo_window and self.demo_window.window and self.demo_window.window.winfo_exists():
            self.demo_window.close()

        print("Application closing...")
        self.root.quit()
        self.root.destroy()

    def run(self):
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
