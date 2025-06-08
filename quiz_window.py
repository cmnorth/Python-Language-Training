# =================================Quiz Window Manager==================================
# quiz_window.py - Manages quiz window creation and module loading
import tkinter as tk
from tkinter import ttk, messagebox
import importlib

class QuizWindow:
    def __init__(self, parent_root, command, user_data):
        self.parent_root = parent_root
        self.command = command
        self.user_data = user_data
        self.window = None
        self.quiz_module = None
    
    def show(self):
        """Display the quiz window by loading appropriate quiz module"""
        command_name = self.command.split(' - ')[0]
        
        # Map commands to their quiz modules
        quiz_modules = {
            'str': 'quiz_strings',
            'print()': 'quiz_print',
            'input()': 'quiz_input',
            'len()': 'quiz_len',
            'type()': 'quiz_type',
            'range()': 'quiz_range',
            'list()': 'quiz_list',
            'dict()': 'quiz_dict',
            'for loop': 'quiz_for_loop',
            'if statement': 'quiz_if_statement',
            'def': 'quiz_functions'
        }
        
        module_name = quiz_modules.get(command_name)
        
        if module_name:
            try:
                # Dynamically import the quiz module
                quiz_module = importlib.import_module(module_name)
                
                # Get the quiz class name (e.g., QuizStrings)
                class_name = f"Quiz{command_name.replace('()', '').replace(' ', '').title()}"
                if command_name == 'str':
                    class_name = 'QuizStrings'
                elif command_name == 'print()':
                    class_name = 'QuizPrint'
                elif command_name == 'input()':
                    class_name = 'QuizInput'
                elif command_name == 'len()':
                    class_name = 'QuizLen'
                elif command_name == 'type()':
                    class_name = 'QuizType'
                elif command_name == 'range()':
                    class_name = 'QuizRange'
                elif command_name == 'list()':
                    class_name = 'QuizList'
                elif command_name == 'dict()':
                    class_name = 'QuizDict'
                elif command_name == 'for loop':
                    class_name = 'QuizForLoop'
                elif command_name == 'if statement':
                    class_name = 'QuizIfStatement'
                elif command_name == 'def':
                    class_name = 'QuizFunctions'
                
                # Create quiz window using the module's quiz class
                quiz_class = getattr(quiz_module, class_name)
                self.quiz_module = quiz_class(self.parent_root, self.user_data)
                self.quiz_module.show()
                self.window = self.quiz_module.window
                
            except ImportError as e:
                # Show coming soon message for unimplemented quizzes
                messagebox.showinfo("Coming Soon", 
                                   f"The {command_name} quiz is being developed and will be available soon!\n\n"
                                   f"In the meantime, you can try the {command_name} demo to practice.")
            except AttributeError as e:
                # Show error if class not found
                messagebox.showerror("Error", f"Quiz class not found for {command_name}")
        else:
            messagebox.showinfo("Coming Soon", f"Quiz for {command_name} coming soon!")
    
    def close(self):
        """Close the quiz window"""
        if self.quiz_module and hasattr(self.quiz_module, 'close'):
            self.quiz_module.close()
        elif self.window and self.window.winfo_exists():
            self.window.destroy()