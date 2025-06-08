# =================================Version 02==================================
# demo_print.py - Print function demo module
import tkinter as tk
from tkinter import ttk
import io
import sys
from contextlib import redirect_stdout, redirect_stderr

class DemoContent:
    def __init__(self, parent_root, command):
        self.parent_root = parent_root
        self.command = command
        self.window = None
        self.examples = self.get_print_examples()
    
    def calculate_window_height(self):
        """Calculate appropriate window height based on content"""
        base_height = 200  # Base height for title and buttons
        example_height = len(self.examples) * 120  # Estimate height per example
        total_height = base_height + example_height
        
        # Constrain between 400px and 850px
        return max(400, min(850, total_height))
    
    def center_window_vertically(self, height):
        """Calculate Y position to center window vertically"""
        screen_height = self.parent_root.winfo_screenheight()
        y_position = (screen_height - height) // 2
        return y_position
    
    def show(self):
        """Display the print function demo window"""
        # Calculate window dimensions
        window_height = self.calculate_window_height()
        
        # Create new demo window
        self.window = tk.Toplevel(self.parent_root)
        self.window.title("Demo: print() Function")
        self.window.geometry(f"600x{window_height}")
        self.window.resizable(False, False)
        
        # Position demo window to the right of menu window with 10px buffer
        menu_x = self.parent_root.winfo_x()
        menu_width = self.parent_root.winfo_width()
        
        demo_x = menu_x + menu_width + 10  # 10px buffer
        demo_y = self.center_window_vertically(window_height)  # Vertically centered
        
        self.window.geometry(f"600x{window_height}+{demo_x}+{demo_y}")
        
        # Create scrollable content
        canvas = tk.Canvas(self.window, bg='white')
        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollable components
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Demo window content
        main_frame = tk.Frame(scrollable_frame, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title and description
        title_label = tk.Label(main_frame, 
                              text="Demo: print() Function", 
                              font=('Arial', 14, 'bold'),
                              bg='white')
        title_label.pack(pady=(0, 10))
        
        # Command usage example at top
        usage_frame = tk.Frame(main_frame, bg='#f0f0f0', relief='raised', bd=2)
        usage_frame.pack(fill='x', pady=(0, 20))
        
        usage_label = tk.Label(usage_frame, 
                              text="Correct Usage:", 
                              font=('Arial', 10, 'bold'),
                              bg='#f0f0f0')
        usage_label.pack(anchor='w', padx=10, pady=(5, 0))
        
        usage_text = tk.Text(usage_frame, height=5, font=('Courier', 10), 
                           bg='#f8f8f8', relief='flat', wrap='word')
        usage_text.pack(fill='x', padx=10, pady=5)
        usage_text.insert('1.0', 'print("Hello, World!")\nprint("Name:", "Alice")\nprint("Score:", 95)\nprint("Items:", 1, 2, 3, sep=", ")\nprint("End with question", end="?\\n")')
        usage_text.config(state='disabled')
        
        # Interactive examples section
        for i, example in enumerate(self.examples):
            self.create_example_widget(main_frame, example, i)
        
        # Close button
        close_button = tk.Button(main_frame, 
                                text="Close Demo", 
                                font=('Arial', 10),
                                command=self.close,
                                bg='#f44336',
                                fg='white',
                                relief='raised',
                                bd=2)
        close_button.pack(pady=(20, 0))
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def create_example_widget(self, parent, example, index):
        """Create an interactive example widget"""
        # Example frame
        example_frame = tk.LabelFrame(parent, text=f"Example {index + 1}: {example['title']}", 
                                     font=('Arial', 10, 'bold'), bg='white', 
                                     relief='groove', bd=2)
        example_frame.pack(fill='x', pady=10)
        
        # Description
        desc_label = tk.Label(example_frame, text=example['description'], 
                             font=('Arial', 9), bg='white', 
                             wraplength=550, justify='left')
        desc_label.pack(anchor='w', padx=10, pady=(5, 10))
        
        # Input area
        input_frame = tk.Frame(example_frame, bg='white')
        input_frame.pack(fill='x', padx=10)
        
        input_label = tk.Label(input_frame, text="Try it:", 
                              font=('Arial', 9, 'bold'), bg='white')
        input_label.pack(anchor='w')
        
        input_text = tk.Entry(input_frame, font=('Courier', 10), width=65)
        input_text.pack(fill='x', pady=2)
        input_text.insert(0, example['default_input'])
        
        # Run button
        run_button = tk.Button(input_frame, text="Run", font=('Arial', 8),
                              command=lambda: self.run_example(input_text, output_text),
                              bg='#4CAF50', fg='white')
        run_button.pack(anchor='w', pady=2)
        
        # Output area
        output_label = tk.Label(example_frame, text="Output:", 
                               font=('Arial', 9, 'bold'), bg='white')
        output_label.pack(anchor='w', padx=10, pady=(10, 0))
        
        output_text = tk.Text(example_frame, height=3, font=('Courier', 9),
                             bg='#f8f8f8', relief='sunken', bd=1, wrap='word')
        output_text.pack(fill='x', padx=10, pady=(2, 10))
    
    def run_example(self, input_widget, output_widget):
        """Execute the code and display output/errors"""
        code = input_widget.get().strip()
        output_widget.delete('1.0', tk.END)
        
        if not code:
            output_widget.insert('1.0', "Please enter some code to run.")
            return
        
        # Capture stdout and stderr
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # Use exec for statements, eval for expressions
                try:
                    result = eval(code)
                    if result is not None:
                        print(result)
                except SyntaxError:
                    exec(code)
            
            # Get output
            stdout_output = stdout_capture.getvalue()
            stderr_output = stderr_capture.getvalue()
            
            if stdout_output:
                output_widget.insert('1.0', stdout_output)
                output_widget.config(fg='black')
            elif stderr_output:
                output_widget.insert('1.0', f"Error: {stderr_output}")
                output_widget.config(fg='red')
            else:
                output_widget.insert('1.0', "Code executed successfully (no output)")
                output_widget.config(fg='green')
                
        except Exception as e:
            output_widget.insert('1.0', f"Error: {str(e)}")
            output_widget.config(fg='red')
    
    def get_print_examples(self):
        """Get all the print function examples"""
        return [
            {
                'title': 'Basic Print Statement',
                'description': 'The simplest way to display text using print()',
                'default_input': 'print("Hello, World!")'
            },
            {
                'title': 'Printing Variables',
                'description': 'Display the value stored in variables',
                'default_input': 'name = "Alice"\nage = 25\nprint("Name:", name)\nprint("Age:", age)'
            },
            {
                'title': 'Multiple Items with Comma',
                'description': 'Print multiple items separated by spaces (default)',
                'default_input': 'print("Score:", 95, "out of", 100)'
            },
            {
                'title': 'Custom Separator',
                'description': 'Change what separates multiple items using sep parameter',
                'default_input': 'print("apple", "banana", "cherry", sep=", ")'
            },
            {
                'title': 'Custom End Character',
                'description': 'Change what appears at the end using end parameter',
                'default_input': 'print("Loading", end="...")\nprint(" Done!")'
            },
            {
                'title': 'Printing Numbers and Calculations',
                'description': 'Display numbers and mathematical expressions',
                'default_input': 'print(5 + 3)\nprint("Result:", 10 * 2)'
            },
            {
                'title': 'Empty Print (New Line)',
                'description': 'Print with no arguments creates a blank line',
                'default_input': 'print("Line 1")\nprint()\nprint("Line 3")'
            },
            {
                'title': 'Print with F-strings',
                'description': 'Modern string formatting with f-strings',
                'default_input': 'name = "Bob"\nscore = 87\nprint(f"{name} scored {score} points")'
            },
            {
                'title': 'Common Error - Missing Quotes',
                'description': 'See what happens when you forget quotes around text',
                'default_input': 'print(Hello World)'
            },
            {
                'title': 'Print Function Return Value',
                'description': 'Check what print() function returns',
                'default_input': 'result = print("Hello")\nprint("Return value:", result)\nprint(type(result))'
            }
        ]
    
    def close(self):
        """Close the demo window"""
        if self.window and self.window.winfo_exists():
            self.window.destroy()