# =================================Fixed Quiz Base System==================================
# quiz_base.py - Enhanced quiz system with auto-checking and better UX
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import random

class QuizBase:
    def __init__(self, parent_root, topic, user_data):
        self.parent_root = parent_root
        self.topic = topic
        self.user_data = user_data
        self.window = None
        
        # Quiz state
        self.current_level = 1
        self.current_question_index = 0
        self.current_question = None
        self.questions = self.get_questions()
        self.answer_submitted = False
        
        # Progress tracking - initialize with integer keys
        self.progress_data = self.load_progress()
        self.level_scores = {i: {'correct': 0, 'incorrect': 0, 'completed': False} for i in range(1, 6)}
        self.used_questions = {i: [] for i in range(1, 6)}
        
        # Load existing progress and convert string keys to integers
        if self.progress_data:
            loaded_scores = self.progress_data.get('score_data', {})
            loaded_questions = self.progress_data.get('used_questions', {})
            
            # Convert string keys to integers for level_scores
            for key, value in loaded_scores.items():
                self.level_scores[int(key)] = value
            
            # Convert string keys to integers for used_questions
            for key, value in loaded_questions.items():
                self.used_questions[int(key)] = value
        
        # Question types and their handlers
        self.question_handlers = {
            'multiple_choice': self.create_multiple_choice,
            'missing_word': self.create_missing_word,
            'mix_match': self.create_mix_match,
            'syntax_error': self.create_syntax_error,
            'one_word': self.create_one_word,
            'snippet_analysis': self.create_snippet_analysis
        }
        
        # Result display variables
        self.result_frame = None

    def calculate_window_height(self):
        return 750  # Increased from 600 to show all levels

    def center_window_vertically(self, height):
        screen_height = self.parent_root.winfo_screenheight()
        y_position = (screen_height - height) // 2
        return y_position

    def show(self):
        window_height = self.calculate_window_height()
        self.window = tk.Toplevel(self.parent_root)
        self.window.title(f"Quiz: {self.topic.upper()}")
        self.window.geometry(f"800x{window_height}")  # Increased width too
        self.window.resizable(False, False)

        # Position window
        menu_x = self.parent_root.winfo_x()
        menu_width = self.parent_root.winfo_width()
        demo_x = menu_x + menu_width + 10
        demo_y = self.center_window_vertically(window_height)
        self.window.geometry(f"800x{window_height}+{demo_x}+{demo_y}")

        self.create_main_interface()
        self.load_next_question()

    def create_main_interface(self):
        # Main container with scrolling
        canvas = tk.Canvas(self.window, bg='white')
        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.main_frame = tk.Frame(scrollable_frame, bg='white')
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Header with progress
        self.create_header()
        
        # Result display area (for showing correct/incorrect feedback)
        self.create_result_display()
        
        # Level selection
        self.create_level_selector()
        
        # Progress display
        self.create_progress_display()
        
        # Question area
        self.create_question_area()
        
        # Control buttons (simplified)
        self.create_control_buttons()
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def create_header(self):
        header_frame = tk.Frame(self.main_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 10))
        
        title_label = tk.Label(header_frame, 
                              text=f"Python {self.topic.upper()} Quiz",
                              font=('Arial', 16, 'bold'),
                              bg='white')
        title_label.pack()
        
        user_label = tk.Label(header_frame,
                             text=f"Student: {self.user_data['first_name']} {self.user_data['last_name']}",
                             font=('Arial', 10),
                             bg='white',
                             fg='blue')
        user_label.pack()

    def create_result_display(self):
        """Create area to show question results"""
        self.result_frame = tk.Frame(self.main_frame, bg='white')
        self.result_frame.pack(fill='x', pady=(0, 10))
        # Initially hidden - will be shown when answers are processed

    def show_result(self, is_correct, correct_answer=None):
        """Display the result of the current question"""
        # Clear previous result
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        if is_correct:
            result_label = tk.Label(self.result_frame,
                                   text="✅ Correct! Well done!",
                                   font=('Arial', 12, 'bold'),
                                   bg='#e8f5e8',
                                   fg='#2e7d32',
                                   relief='raised',
                                   bd=2)
        else:
            result_text = "❌ Incorrect."
            if correct_answer:
                result_text += f" The correct answer is: {correct_answer}"
            
            result_label = tk.Label(self.result_frame,
                                   text=result_text,
                                   font=('Arial', 12, 'bold'),
                                   bg='#ffebee',
                                   fg='#c62828',
                                   relief='raised',
                                   bd=2,
                                   wraplength=700)
        
        result_label.pack(fill='x', pady=5)
        
        # Auto-advance to next question after 2 seconds
        self.window.after(2000, self.load_next_question)

    def create_level_selector(self):
        level_frame = tk.LabelFrame(self.main_frame, text="Select Level", 
                                   font=('Arial', 10, 'bold'), bg='white')
        level_frame.pack(fill='x', pady=(0, 10))
        
        button_frame = tk.Frame(level_frame, bg='white')
        button_frame.pack(pady=5)
        
        self.level_buttons = {}
        for level in range(1, 6):
            btn = tk.Button(button_frame,
                           text=f"Level {level}",
                           font=('Arial', 9),
                           width=8,
                           command=lambda l=level: self.select_level(l),
                           bg='#e0e0e0',
                           relief='raised')
            btn.pack(side='left', padx=2)
            self.level_buttons[level] = btn
        
        self.update_level_buttons()

    def create_progress_display(self):
        self.progress_frame = tk.LabelFrame(self.main_frame, text="Progress Summary", 
                                          font=('Arial', 10, 'bold'), bg='white')
        self.progress_frame.pack(fill='x', pady=(0, 10))
        
        self.progress_text = tk.Text(self.progress_frame, height=6, font=('Arial', 9),  # Increased height
                                    bg='#f8f8f8', relief='flat', wrap='word',
                                    state='disabled')
        self.progress_text.pack(fill='x', padx=10, pady=5)
        
        self.update_progress_display()

    def create_question_area(self):
        self.question_frame = tk.LabelFrame(self.main_frame, text="Question", 
                                          font=('Arial', 10, 'bold'), bg='white')
        self.question_frame.pack(fill='both', expand=True, pady=(0, 10))

    def create_control_buttons(self):
        """Create simplified control buttons: Skip and Exit only"""
        button_frame = tk.Frame(self.main_frame, bg='white')
        button_frame.pack(fill='x', pady=(10, 0))
        
        skip_btn = tk.Button(button_frame,
                            text="⏭ Skip Question",
                            font=('Arial', 10),
                            command=self.skip_question,
                            bg='#FF9800',
                            fg='white',
                            relief='raised',
                            bd=2)
        skip_btn.pack(side='left', padx=(0, 10))
        
        exit_btn = tk.Button(button_frame,
                            text="❌ Exit Quiz",
                            font=('Arial', 10),
                            command=self.close,
                            bg='#f44336',
                            fg='white',
                            relief='raised',
                            bd=2)
        exit_btn.pack(side='right')

    def skip_question(self):
        """Skip current question and move to next"""
        # Count as incorrect
        self.level_scores[self.current_level]['incorrect'] += 1
        self.update_progress_display()
        self.save_progress()
        
        # Show skip message briefly then move to next
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        skip_label = tk.Label(self.result_frame,
                             text="⏭ Question Skipped",
                             font=('Arial', 12, 'bold'),
                             bg='#fff3e0',
                             fg='#f57c00',
                             relief='raised',
                             bd=2)
        skip_label.pack(fill='x', pady=5)
        
        # Move to next question after 1 second
        self.window.after(1000, self.load_next_question)

    def select_level(self, level):
        self.current_level = level
        self.current_question_index = 0
        self.answer_submitted = False
        self.update_level_buttons()
        
        # Clear result display
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        self.load_next_question()

    def update_level_buttons(self):
        for level, btn in self.level_buttons.items():
            if level == self.current_level:
                btn.config(bg='#4CAF50', fg='white')
            elif self.level_scores[level]['completed']:
                btn.config(bg='#81C784', fg='white')
            else:
                btn.config(bg='#e0e0e0', fg='black')

    def update_progress_display(self):
        self.progress_text.config(state='normal')
        self.progress_text.delete('1.0', tk.END)
        
        progress_lines = []
        for level in range(1, 6):
            score = self.level_scores[level]
            total_attempted = score['correct'] + score['incorrect']
            status = "✓ Completed" if score['completed'] else f"({total_attempted}/15 questions)"
            
            line = f"Level {level}: {score['correct']} correct, {score['incorrect']} incorrect {status}"
            progress_lines.append(line)
        
        self.progress_text.insert('1.0', '\n'.join(progress_lines))
        self.progress_text.config(state='disabled')

    def load_next_question(self):
        # Clear result display
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        level_questions = [q for q in self.questions if q['level'] == self.current_level]
        
        # Check if level is completed
        if len(self.used_questions[self.current_level]) >= 15:
            self.level_scores[self.current_level]['completed'] = True
            self.update_level_buttons()
            self.update_progress_display()
            self.save_progress()
            messagebox.showinfo("Level Complete", 
                               f"Level {self.current_level} completed!\n"
                               f"Score: {self.level_scores[self.current_level]['correct']}/15")
            return
        
        # Get unused questions for current level
        available_questions = [q for i, q in enumerate(level_questions) 
                             if i not in self.used_questions[self.current_level]]
        
        if not available_questions:
            messagebox.showinfo("No More Questions", f"No more questions available for Level {self.current_level}")
            return
        
        # Select random question
        self.current_question = random.choice(available_questions)
        question_index = level_questions.index(self.current_question)
        self.used_questions[self.current_level].append(question_index)
        
        # Reset answer state
        self.answer_submitted = False
        
        self.display_question()

    def display_question(self):
        # Clear previous question
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        
        # Get question type and create appropriate interface
        question_type = self.current_question['type']
        if question_type in self.question_handlers:
            self.question_handlers[question_type]()
        else:
            self.create_multiple_choice()  # Default fallback

    def create_multiple_choice(self):
        question_text = self.current_question['question']
        options = self.current_question['options']
        
        # Question text
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Options
        self.selected_option = tk.StringVar()
        
        for i, option in enumerate(options):
            rb = tk.Radiobutton(self.question_frame, text=f"{chr(65+i)}. {option}",
                               variable=self.selected_option, value=option,
                               font=('Arial', 10), bg='white',
                               command=self.process_answer)
            rb.pack(anchor='w', padx=20, pady=2)

    def create_missing_word(self):
        question_text = self.current_question['question']
        
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        tk.Label(self.question_frame, text="Fill in the missing word:",
                font=('Arial', 10, 'bold'), bg='white').pack(anchor='w', padx=10, pady=(10, 5))
        
        self.missing_word_entry = tk.Entry(self.question_frame, font=('Arial', 11), width=30)
        self.missing_word_entry.pack(anchor='w', padx=20, pady=5)
        self.missing_word_entry.bind('<Return>', lambda e: self.process_answer())
        self.missing_word_entry.focus_set()

    def create_mix_match(self):
        question_text = self.current_question['question']
        left_items = self.current_question['left_items']
        right_items = self.current_question['right_items']
        
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Create matching interface
        match_frame = tk.Frame(self.question_frame, bg='white')
        match_frame.pack(fill='x', padx=10, pady=10)
        
        left_frame = tk.Frame(match_frame, bg='white')
        left_frame.pack(side='left', fill='both', expand=True)
        
        right_frame = tk.Frame(match_frame, bg='white')
        right_frame.pack(side='right', fill='both', expand=True)
        
        tk.Label(left_frame, text="Match these:", font=('Arial', 10, 'bold'), bg='white').pack()
        tk.Label(right_frame, text="With these:", font=('Arial', 10, 'bold'), bg='white').pack()
        
        self.match_vars = {}
        
        for i, item in enumerate(left_items):
            tk.Label(left_frame, text=f"{i+1}. {item}", font=('Arial', 10), bg='white').pack(anchor='w')
            
            var = tk.StringVar()
            combo = ttk.Combobox(right_frame, textvariable=var, values=right_items, width=20, state='readonly')
            combo.pack(pady=2)
            combo.bind('<<ComboboxSelected>>', lambda e: self.check_mix_match_complete())
            self.match_vars[i] = var

    def create_syntax_error(self):
        question_text = self.current_question['question']
        code_snippet = self.current_question['code']
        
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Code display
        code_frame = tk.Frame(self.question_frame, bg='#f8f8f8', relief='sunken', bd=1)
        code_frame.pack(fill='x', padx=10, pady=10)
        
        code_text = tk.Text(code_frame, height=4, font=('Courier', 10),
                           bg='#f8f8f8', relief='flat', wrap='word')
        code_text.pack(fill='x', padx=5, pady=5)
        code_text.insert('1.0', code_snippet)
        code_text.config(state='disabled')
        
        tk.Label(self.question_frame, text="What is the syntax error?",
                font=('Arial', 10, 'bold'), bg='white').pack(anchor='w', padx=10, pady=(10, 5))
        
        self.syntax_error_entry = tk.Entry(self.question_frame, font=('Arial', 11), width=50)
        self.syntax_error_entry.pack(anchor='w', padx=20, pady=5)
        self.syntax_error_entry.bind('<Return>', lambda e: self.process_answer())
        self.syntax_error_entry.focus_set()

    def create_one_word(self):
        question_text = self.current_question['question']
        
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        tk.Label(self.question_frame, text="Answer (one word):",
                font=('Arial', 10, 'bold'), bg='white').pack(anchor='w', padx=10, pady=(10, 5))
        
        self.one_word_entry = tk.Entry(self.question_frame, font=('Arial', 11), width=20)
        self.one_word_entry.pack(anchor='w', padx=20, pady=5)
        self.one_word_entry.bind('<Return>', lambda e: self.process_answer())
        self.one_word_entry.focus_set()

    def create_snippet_analysis(self):
        question_text = self.current_question['question']
        code_snippet = self.current_question['code']
        
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Code display
        code_frame = tk.Frame(self.question_frame, bg='#f8f8f8', relief='sunken', bd=1)
        code_frame.pack(fill='x', padx=10, pady=10)
        
        code_text = tk.Text(code_frame, height=4, font=('Courier', 10),
                           bg='#f8f8f8', relief='flat', wrap='word')
        code_text.pack(fill='x', padx=5, pady=5)
        code_text.insert('1.0', code_snippet)
        code_text.config(state='disabled')
        
        # Options for analysis
        if 'options' in self.current_question:
            self.selected_option = tk.StringVar()
            
            for i, option in enumerate(self.current_question['options']):
                rb = tk.Radiobutton(self.question_frame, text=f"{chr(65+i)}. {option}",
                                   variable=self.selected_option, value=option,
                                   font=('Arial', 10), bg='white',
                                   command=self.process_answer)
                rb.pack(anchor='w', padx=20, pady=2)

    def check_mix_match_complete(self):
        """Check if all mix-match selections are complete, then auto-submit"""
        if not self.answer_submitted:
            # Check if all combos have selections
            all_selected = all(var.get() for var in self.match_vars.values())
            if all_selected:
                self.process_answer()

    def process_answer(self):
        """Process the answer and show result"""
        if self.answer_submitted:
            return
        
        self.answer_submitted = True
        
        is_correct = self.check_answer()
        correct_answer = self.get_correct_answer()
        
        if is_correct:
            self.level_scores[self.current_level]['correct'] += 1
        else:
            self.level_scores[self.current_level]['incorrect'] += 1
        
        # Update displays
        self.update_progress_display()
        self.save_progress()
        
        # Show result
        self.show_result(is_correct, correct_answer if not is_correct else None)

    def check_answer(self):
        question_type = self.current_question['type']
        correct_answer = self.current_question['correct_answer']
        
        if question_type == 'multiple_choice' or question_type == 'snippet_analysis':
            return self.selected_option.get() == correct_answer
        elif question_type == 'missing_word':
            user_answer = self.missing_word_entry.get().strip().lower()
            if isinstance(correct_answer, list):
                return user_answer in [ans.lower() for ans in correct_answer]
            else:
                return user_answer == correct_answer.lower()
        elif question_type == 'mix_match':
            user_matches = {i: var.get() for i, var in self.match_vars.items()}
            return user_matches == correct_answer
        elif question_type in ['syntax_error', 'one_word']:
            if question_type == 'syntax_error':
                user_answer = self.syntax_error_entry.get().strip().lower()
            else:
                user_answer = self.one_word_entry.get().strip().lower()
            
            if isinstance(correct_answer, list):
                return user_answer in [ans.lower() for ans in correct_answer]
            else:
                return user_answer == correct_answer.lower()
        
        return False

    def get_correct_answer(self):
        correct_answer = self.current_question['correct_answer']
        if isinstance(correct_answer, list):
            return ', '.join(correct_answer)
        return str(correct_answer)

    def load_progress(self):
        filename = f"quiz_progress_{self.topic}_{self.user_data['email'].replace('@', '_').replace('.', '_')}.json"
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    return json.load(f)
            except:
                return None
        return None

    def save_progress(self):
        filename = f"quiz_progress_{self.topic}_{self.user_data['email'].replace('@', '_').replace('.', '_')}.json"
        
        # Convert integer keys to strings for JSON compatibility
        score_data_str_keys = {str(k): v for k, v in self.level_scores.items()}
        used_questions_str_keys = {str(k): v for k, v in self.used_questions.items()}
        
        progress_data = {
            'user_email': self.user_data['email'],
            'demo_topic': self.topic,
            'score_data': score_data_str_keys,
            'used_questions': used_questions_str_keys,
            'last_updated': datetime.now().isoformat()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(progress_data, f, indent=2)
        except Exception as e:
            print(f"Failed to save progress: {e}")

    def get_questions(self):
        # This method should be overridden by specific quiz modules
        return []

    def close(self):
        if self.window and self.window.winfo_exists():
            self.save_progress()
            self.window.destroy()