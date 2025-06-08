# =================================Updated Quiz Window Manager - All Quizzes Activated==================================
# quiz_window.py - Manages quiz window creation and module loading with all quizzes enabled
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
                
                # Get the quiz class name - mapping to correct class names
                class_mapping = {
                    'str': 'QuizStrings',
                    'print()': 'QuizPrint',
                    'input()': 'QuizInput',
                    'len()': 'QuizLen',
                    'type()': 'QuizType',
                    'range()': 'QuizRange',
                    'list()': 'QuizList',
                    'dict()': 'QuizDict',
                    'for loop': 'QuizForLoop',
                    'if statement': 'QuizIfStatement',
                    'def': 'QuizFunctions'
                }
                
                class_name = class_mapping.get(command_name)
                
                if class_name:
                    # Create quiz window using the module's quiz class
                    quiz_class = getattr(quiz_module, class_name)
                    self.quiz_module = quiz_class(self.parent_root, self.user_data)
                    self.quiz_module.show()
                    self.window = self.quiz_module.window
                else:
                    messagebox.showerror("Error", f"Quiz class not found for {command_name}")
                
            except ImportError as e:
                # Show detailed error message for debugging
                messagebox.showerror("Module Error", 
                                   f"Could not load quiz module '{module_name}' for {command_name}.\n\n"
                                   f"Error: {str(e)}\n\n"
                                   f"Please ensure the quiz module file exists and is properly implemented.")
                print(f"ImportError loading {module_name}: {e}")
                
            except AttributeError as e:
                # Show error if class not found
                messagebox.showerror("Class Error", 
                                   f"Quiz class '{class_name}' not found in module '{module_name}'.\n\n"
                                   f"Error: {str(e)}\n\n"
                                   f"Please ensure the quiz class is properly defined.")
                print(f"AttributeError: {e}")
                
            except Exception as e:
                # Generic error handler
                messagebox.showerror("Unexpected Error", 
                                   f"An unexpected error occurred while loading the quiz:\n\n"
                                   f"Error: {str(e)}\n\n"
                                   f"Please check the quiz module implementation.")
                print(f"Unexpected error: {e}")
        else:
            messagebox.showerror("Error", f"No quiz module mapping found for '{command_name}'")
    
    def close(self):
        """Close the quiz window"""
        if self.quiz_module and hasattr(self.quiz_module, 'close'):
            self.quiz_module.close()
        elif self.window and self.window.winfo_exists():
            self.window.destroy()