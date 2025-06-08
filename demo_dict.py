# =================================Version 02 - MULTI-EXAMPLE==================================
# demo_dict.py - Demonstrates dictionary creation and operations with 10 examples
import tkinter as tk
from tkinter import ttk
import io
from contextlib import redirect_stdout, redirect_stderr

class DemoContent:
    def __init__(self, parent_root, command):
        self.parent_root = parent_root
        self.command = command
        self.window = None
        self.examples = self.get_dict_examples()

    def calculate_window_height(self):
        base_height = 200
        example_height = len(self.examples) * 120
        total_height = base_height + example_height
        return max(400, min(850, total_height))

    def center_window_vertically(self, height):
        screen_height = self.parent_root.winfo_screenheight()
        y_position = (screen_height - height) // 2
        return y_position

    def show(self):
        window_height = self.calculate_window_height()
        self.window = tk.Toplevel(self.parent_root)
        self.window.title("Demo: dict()")
        self.window.geometry(f"600x{window_height}")
        self.window.resizable(False, False)

        menu_x = self.parent_root.winfo_x()
        menu_width = self.parent_root.winfo_width()
        demo_x = menu_x + menu_width + 10
        demo_y = self.center_window_vertically(window_height)
        self.window.geometry(f"600x{window_height}+{demo_x}+{demo_y}")

        canvas = tk.Canvas(self.window, bg='white')
        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        main_frame = tk.Frame(scrollable_frame, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        title_label = tk.Label(main_frame, text="Demo: dict()", font=('Arial', 14, 'bold'), bg='white')
        title_label.pack(pady=(0, 10))

        usage_frame = tk.Frame(main_frame, bg='#f0f0f0', relief='raised', bd=2)
        usage_frame.pack(fill='x', pady=(0, 20))

        usage_label = tk.Label(usage_frame, text="Correct Usage:", font=('Arial', 10, 'bold'), bg='#f0f0f0')
        usage_label.pack(anchor='w', padx=10, pady=(5, 0))

        usage_text = tk.Text(usage_frame, height=4, font=('Courier', 10), bg='#f8f8f8', relief='flat', wrap='word')
        usage_text.pack(fill='x', padx=10, pady=5)
        usage_text.insert('1.0', "{'a': 1, 'b': 2}\ndict(name='John', age=30)\nlen({'x': 9})\n'day' in {'day': 'Monday'}")
        usage_text.config(state='disabled')

        for i, example in enumerate(self.examples):
            self.create_example_widget(main_frame, example, i)

        close_button = tk.Button(main_frame, text="Close Demo", font=('Arial', 10), command=self.close,
                                 bg='#f44336', fg='white', relief='raised', bd=2)
        close_button.pack(pady=(20, 0))

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def create_example_widget(self, parent, example, index):
        example_frame = tk.LabelFrame(parent, text=f"Example {index + 1}: {example['title']}", 
                                     font=('Arial', 10, 'bold'), bg='white', 
                                     relief='groove', bd=2)
        example_frame.pack(fill='x', pady=10)

        desc_label = tk.Label(example_frame, text=example['description'], 
                             font=('Arial', 9), bg='white', 
                             wraplength=550, justify='left')
        desc_label.pack(anchor='w', padx=10, pady=(5, 10))

        input_frame = tk.Frame(example_frame, bg='white')
        input_frame.pack(fill='x', padx=10)

        input_label = tk.Label(input_frame, text="Try it:", font=('Arial', 9, 'bold'), bg='white')
        input_label.pack(anchor='w')

        input_text = tk.Entry(input_frame, font=('Courier', 10), width=65)
        input_text.pack(fill='x', pady=2)
        input_text.insert(0, example['default_input'])

        output_label = tk.Label(example_frame, text="Output:", font=('Arial', 9, 'bold'), bg='white')
        output_label.pack(anchor='w', padx=10, pady=(10, 0))

        output_text = tk.Text(example_frame, height=3, font=('Courier', 9),
                             bg='#f8f8f8', relief='sunken', bd=1, wrap='word')
        output_text.pack(fill='x', padx=10, pady=(2, 10))

        run_button = tk.Button(input_frame, text="Run", font=('Arial', 8),
                              command=lambda: self.run_example(input_text, output_text),
                              bg='#4CAF50', fg='white')
        run_button.pack(anchor='w', pady=2)

    def run_example(self, input_widget, output_widget):
        code = input_widget.get().strip()
        output_widget.delete('1.0', tk.END)

        if not code:
            output_widget.insert('1.0', "Please enter some code to run.")
            return

        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        try:
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                try:
                    result = eval(code)
                    if result is not None:
                        print(result)
                except SyntaxError:
                    exec(code)

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

    def get_dict_examples(self):
        return [
            {'title': 'Create Dictionary', 'description': 'Using curly braces to define a dictionary', 'default_input': "{'name': 'Alice', 'age': 25}"},
            {'title': 'Using dict()', 'description': 'Using the dict constructor with keyword arguments', 'default_input': "dict(animal='dog', sound='bark')"},
            {'title': 'Access Value', 'description': 'Access a value by key', 'default_input': "{'a': 1, 'b': 2}['a']"},
            {'title': 'Add Entry', 'description': 'Add a new key-value pair', 'default_input': "d = {}; d['x'] = 42; d"},
            {'title': 'Update Value', 'description': 'Change the value of an existing key', 'default_input': "d = {'a': 1}; d['a'] = 99; d"},
            {'title': 'Remove Key', 'description': 'Delete a key using del', 'default_input': "d = {'x': 9}; del d['x']; d"},
            {'title': 'List Keys', 'description': 'Get all the keys from a dictionary', 'default_input': "list({'a':1,'b':2}.keys())"},
            {'title': 'List Values', 'description': 'Get all the values from a dictionary', 'default_input': "list({'a':1,'b':2}.values())"},
            {'title': 'Loop Items', 'description': 'Use items() to loop over key-value pairs', 'default_input': "for k,v in {'a':1,'b':2}.items(): print(k,v)"},
            {'title': 'Check Key Exists', 'description': 'Use "in" to check for a key', 'default_input': "'age' in {'name':'John', 'age':30}"},
        ]

    def close(self):
        if self.window and self.window.winfo_exists():
            self.window.destroy()
