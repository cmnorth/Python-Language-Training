# =================================Demo Code Display Fix==================================
# demo_display_utils.py - Utilities for proper code formatting in demos
import tkinter as tk

class CodeDisplayManager:
    """Manages proper formatting and display of code snippets in demos"""
    
    @staticmethod
    def format_code_snippet(code_text):
        """Format code snippet for proper display"""
        # Replace literal \n with actual newlines
        formatted = code_text.replace('\\n', '\n')
        
        # Handle common Python indentation
        lines = formatted.split('\n')
        
        # Clean up each line and maintain proper indentation
        cleaned_lines = []
        for line in lines:
            # Strip only trailing whitespace, preserve leading spaces
            cleaned_line = line.rstrip()
            cleaned_lines.append(cleaned_line)
        
        return '\n'.join(cleaned_lines)
    
    @staticmethod
    def create_code_display_widget(parent, code_text, height=None, bg_color='#f8f8f8'):
        """Create a properly formatted code display widget"""
        # Automatically calculate height based on number of lines
        if height is None:
            lines = code_text.count('\n') + 1
            height = max(3, min(10, lines + 1))  # Between 3-10 lines
        
        # Format the code
        formatted_code = CodeDisplayManager.format_code_snippet(code_text)
        
        # Create text widget with proper configuration
        code_widget = tk.Text(parent, 
                             height=height, 
                             font=('Courier New', 10),  # Better monospace font
                             bg=bg_color, 
                             relief='sunken', 
                             bd=1, 
                             wrap='none',  # Don't wrap code lines
                             selectbackground='#4CAF50',
                             state='normal')
        
        # Insert formatted code
        code_widget.insert('1.0', formatted_code)
        
        # Make read-only
        code_widget.config(state='disabled')
        
        return code_widget
    
    @staticmethod
    def update_demo_usage_section(parent_frame, usage_examples, colors):
        """Create an improved usage section with properly formatted code"""
        usage_frame = tk.Frame(parent_frame, bg=colors.get("frame_bg", "#f0f0f0"), relief='raised', bd=2)
        usage_frame.pack(fill='x', pady=(0, 20))
        
        usage_label = tk.Label(usage_frame, 
                              text="💡 Usage Examples:", 
                              font=('Arial', 10, 'bold'),
                              bg=colors.get("frame_bg", "#f0f0f0"),
                              fg=colors.get("text", "black"))
        usage_label.pack(anchor='w', padx=10, pady=(5, 0))
        
        # Create scrollable text area for multiple examples
        code_display = CodeDisplayManager.create_code_display_widget(
            usage_frame, 
            usage_examples,
            height=6,
            bg_color=colors.get("code_bg", "#f8f8f8")
        )
        code_display.pack(fill='x', padx=10, pady=5)
        
        return usage_frame