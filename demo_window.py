# =================================Version 02==================================
# demo_window.py - Base demo window manager
import tkinter as tk
from tkinter import ttk
import importlib

class DemoWindow:
    def __init__(self, parent_root, command):
        self.parent_root = parent_root
        self.command = command
        self.window = None
        self.demo_module = None
    
    def show(self):
        """Display the demo window by loading appropriate demo module"""
        command_name = self.command.split(' - ')[0]
        
        # Map commands to their demo modules
        demo_modules = {
            'str': 'demo_strings',
            'print()': 'demo_print',
            'input()': 'demo_input',
            'len()': 'demo_len',
            'type()': 'demo_type',
            'range()': 'demo_range',
            'list()': 'demo_list',
            'dict()': 'demo_dict',
            'for loop': 'demo_for_loop',
            'if statement': 'demo_if_statement',
            'def': 'demo_functions'
        }
        
        module_name = demo_modules.get(command_name)
        
        if module_name:
            try:
                # Dynamically import the demo module
                demo_module = importlib.import_module(module_name)
                
                # Create demo window using the module's DemoContent class
                self.demo_module = demo_module.DemoContent(self.parent_root, self.command)
                self.demo_module.show()
                self.window = self.demo_module.window
                
            except ImportError:
                # Fallback to placeholder if module doesn't exist
                self.show_placeholder()
        else:
            self.show_placeholder()
    
    def show_placeholder(self):
        """Show placeholder demo window for unimplemented demos"""
        self.window = tk.Toplevel(self.parent_root)
        self.window.title(f"Demo: {self.command.split(' - ')[0]}")
        self.window.geometry("600x400")  # Increased width for placeholder
        self.window.resizable(False, False)
        
        # Position window
        menu_x = self.parent_root.winfo_x()
        menu_width = self.parent_root.winfo_width()
        demo_x = menu_x + menu_width + 10
        screen_height = self.parent_root.winfo_screenheight()
        demo_y = (screen_height - 400) // 2
        
        self.window.geometry(f"600x400+{demo_x}+{demo_y}")  # Updated width
        
        # Placeholder content
        main_frame = tk.Frame(self.window, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title_label = tk.Label(main_frame, 
                              text=f"Demo: {self.command.split(' - ')[0]}", 
                              font=('Arial', 14, 'bold'),
                              bg='white')
        title_label.pack(pady=(10, 20))
        
        placeholder_label = tk.Label(main_frame, 
                                   text=f"Demo module for {self.command.split(' - ')[0]} \nwill be implemented here", 
                                   font=('Arial', 12),
                                   bg='white',
                                   fg='gray')
        placeholder_label.pack(expand=True)
        
        close_button = tk.Button(main_frame, 
                                text="Close Demo", 
                                font=('Arial', 10),
                                command=self.close,
                                bg='#f44336',
                                fg='white')
        close_button.pack(pady=(10, 0))
    
    def close(self):
        """Close the demo window"""
        if self.demo_module and hasattr(self.demo_module, 'close'):
            self.demo_module.close()
        elif self.window and self.window.winfo_exists():
            self.window.destroy()