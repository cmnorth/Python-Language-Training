# =================================Records Window==================================
# records_window.py - Student progress and records viewing system
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import glob

class RecordsWindow:
    def __init__(self, parent_root, user_data):
        self.parent_root = parent_root
        self.user_data = user_data
        self.window = None
        self.progress_data = {}
        
    def show(self):
        """Display the records window"""
        window_height = 600
        self.window = tk.Toplevel(self.parent_root)
        self.window.title(f"Progress Records - {self.user_data['first_name']} {self.user_data['last_name']}")
        self.window.geometry(f"800x{window_height}")
        self.window.resizable(False, False)

        # Position window
        menu_x = self.parent_root.winfo_x()
        menu_width = self.parent_root.winfo_width()
        demo_x = menu_x + menu_width + 10
        screen_height = self.parent_root.winfo_screenheight()
        demo_y = (screen_height - window_height) // 2
        self.window.geometry(f"800x{window_height}+{demo_x}+{demo_y}")

        self.load_all_progress()
        self.create_interface()

    def load_all_progress(self):
        """Load progress data for all quiz topics"""
        email_safe = self.user_data['email'].replace('@', '_').replace('.', '_')
        pattern = f"quiz_progress_*_{email_safe}.json"
        
        self.progress_data = {}
        
        # Find all progress files for this user
        for filename in glob.glob(pattern):
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    topic = data.get('demo_topic', 'unknown')
                    self.progress_data[topic] = data
            except Exception as e:
                print(f"Error loading {filename}: {e}")

    def create_interface(self):
        """Create the main interface"""
        # Create scrollable main frame
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
        
        # Main content frame
        main_frame = tk.Frame(scrollable_frame, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_frame)
        
        # Overall summary
        self.create_summary(main_frame)
        
        # Individual topic progress
        self.create_topic_progress(main_frame)
        
        # Control buttons
        self.create_controls(main_frame)
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def create_header(self, parent):
        """Create header section"""
        header_frame = tk.Frame(parent, bg='white')
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame, 
                              text="📊 Progress Records",
                              font=('Arial', 18, 'bold'),
                              bg='white')
        title_label.pack()
        
        student_label = tk.Label(header_frame,
                                text=f"Student: {self.user_data['first_name']} {self.user_data['last_name']}",
                                font=('Arial', 12),
                                bg='white',
                                fg='blue')
        student_label.pack()
        
        email_label = tk.Label(header_frame,
                              text=f"Email: {self.user_data['email']}",
                              font=('Arial', 10),
                              bg='white',
                              fg='gray')
        email_label.pack()

    def create_summary(self, parent):
        """Create overall summary section"""
        summary_frame = tk.LabelFrame(parent, text="📈 Overall Progress Summary", 
                                     font=('Arial', 12, 'bold'), bg='white',
                                     relief='groove', bd=2)
        summary_frame.pack(fill='x', pady=(0, 20))
        
        # Calculate overall statistics
        total_topics = len(self.progress_data)
        total_questions = 0
        total_correct = 0
        total_incorrect = 0
        completed_levels = 0
        total_levels = 0
        
        for topic, data in self.progress_data.items():
            score_data = data.get('score_data', {})
            for level, scores in score_data.items():
                total_levels += 1
                total_correct += scores.get('correct', 0)
                total_incorrect += scores.get('incorrect', 0)
                if scores.get('completed', False):
                    completed_levels += 1
        
        total_questions = total_correct + total_incorrect
        
        # Display statistics
        stats_frame = tk.Frame(summary_frame, bg='white')
        stats_frame.pack(fill='x', padx=10, pady=10)
        
        # Create grid layout for stats
        stats = [
            ("Topics Started:", str(total_topics)),
            ("Total Questions Attempted:", str(total_questions)),
            ("Correct Answers:", str(total_correct)),
            ("Incorrect Answers:", str(total_incorrect)),
            ("Accuracy Rate:", f"{(total_correct/total_questions*100):.1f}%" if total_questions > 0 else "0%"),
            ("Levels Completed:", f"{completed_levels}/{total_levels}")
        ]
        
        for i, (label, value) in enumerate(stats):
            row = i // 2
            col = (i % 2) * 2
            
            tk.Label(stats_frame, text=label, font=('Arial', 10, 'bold'), 
                    bg='white', anchor='w').grid(row=row, column=col, sticky='w', padx=5, pady=2)
            tk.Label(stats_frame, text=value, font=('Arial', 10), 
                    bg='white', fg='blue', anchor='w').grid(row=row, column=col+1, sticky='w', padx=15, pady=2)

    def create_topic_progress(self, parent):
        """Create detailed topic progress section"""
        topics_frame = tk.LabelFrame(parent, text="📚 Detailed Progress by Topic", 
                                    font=('Arial', 12, 'bold'), bg='white',
                                    relief='groove', bd=2)
        topics_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        if not self.progress_data:
            no_data_label = tk.Label(topics_frame, 
                                    text="No quiz progress data found.\nStart taking quizzes to see your progress here!",
                                    font=('Arial', 12),
                                    bg='white',
                                    fg='gray',
                                    justify='center')
            no_data_label.pack(expand=True, pady=50)
            return
        
        # Create topic cards
        for topic, data in sorted(self.progress_data.items()):
            self.create_topic_card(topics_frame, topic, data)

    def create_topic_card(self, parent, topic, data):
        """Create a card for individual topic progress"""
        card_frame = tk.LabelFrame(parent, text=f"🐍 {topic.upper()} Quiz", 
                                  font=('Arial', 11, 'bold'), bg='white',
                                  relief='raised', bd=2)
        card_frame.pack(fill='x', padx=10, pady=5)
        
        # Get score data
        score_data = data.get('score_data', {})
        last_updated = data.get('last_updated', 'Unknown')
        
        # Parse last updated date
        try:
            if last_updated != 'Unknown':
                date_obj = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
                last_updated = date_obj.strftime("%Y-%m-%d %H:%M")
        except:
            pass
        
        # Content frame
        content_frame = tk.Frame(card_frame, bg='white')
        content_frame.pack(fill='x', padx=10, pady=8)
        
        # Last updated
        update_label = tk.Label(content_frame, 
                               text=f"Last Updated: {last_updated}",
                               font=('Arial', 8, 'italic'),
                               bg='white',
                               fg='gray')
        update_label.pack(anchor='w')
        
        # Level progress grid
        levels_frame = tk.Frame(content_frame, bg='white')
        levels_frame.pack(fill='x', pady=(5, 0))
        
        # Headers
        headers = ["Level", "Questions", "Correct", "Incorrect", "Accuracy", "Status"]
        for i, header in enumerate(headers):
            tk.Label(levels_frame, text=header, font=('Arial', 9, 'bold'), 
                    bg='#f0f0f0', relief='ridge', bd=1, width=12).grid(row=0, column=i, sticky='ew')
        
        # Level data
        total_correct = 0
        total_incorrect = 0
        
        for level in range(1, 6):
            level_data = score_data.get(str(level), {'correct': 0, 'incorrect': 0, 'completed': False})
            correct = level_data.get('correct', 0)
            incorrect = level_data.get('incorrect', 0)
            completed = level_data.get('completed', False)
            total = correct + incorrect
            accuracy = f"{(correct/total*100):.1f}%" if total > 0 else "0%"
            status = "✅ Complete" if completed else f"🔄 {total}/15"
            
            total_correct += correct
            total_incorrect += incorrect
            
            row_data = [f"Level {level}", str(total), str(correct), str(incorrect), accuracy, status]
            
            for i, cell_data in enumerate(row_data):
                bg_color = '#e8f5e8' if completed else 'white'
                tk.Label(levels_frame, text=cell_data, font=('Arial', 9), 
                        bg=bg_color, relief='ridge', bd=1, width=12).grid(row=level, column=i, sticky='ew')
        
        # Total row
        total_questions = total_correct + total_incorrect
        total_accuracy = f"{(total_correct/total_questions*100):.1f}%" if total_questions > 0 else "0%"
        
        total_data = ["TOTAL", str(total_questions), str(total_correct), str(total_incorrect), total_accuracy, ""]
        for i, cell_data in enumerate(total_data):
            tk.Label(levels_frame, text=cell_data, font=('Arial', 9, 'bold'), 
                    bg='#d0d0d0', relief='ridge', bd=1, width=12).grid(row=6, column=i, sticky='ew')

    def create_controls(self, parent):
        """Create control buttons"""
        button_frame = tk.Frame(parent, bg='white')
        button_frame.pack(fill='x', pady=(20, 0))
        
        refresh_btn = tk.Button(button_frame,
                               text="🔄 Refresh Data",
                               font=('Arial', 10),
                               command=self.refresh_data,
                               bg='#2196F3',
                               fg='white',
                               relief='raised',
                               bd=2)
        refresh_btn.pack(side='left', padx=(0, 10))
        
        export_btn = tk.Button(button_frame,
                              text="📄 Export Report",
                              font=('Arial', 10),
                              command=self.export_report,
                              bg='#4CAF50',
                              fg='white',
                              relief='raised',
                              bd=2)
        export_btn.pack(side='left', padx=10)
        
        close_btn = tk.Button(button_frame,
                             text="❌ Close",
                             font=('Arial', 10),
                             command=self.close,
                             bg='#f44336',
                             fg='white',
                             relief='raised',
                             bd=2)
        close_btn.pack(side='right')

    def refresh_data(self):
        """Refresh progress data"""
        self.load_all_progress()
        self.window.destroy()
        self.show()
        messagebox.showinfo("Refreshed", "Progress data has been refreshed!")

    def export_report(self):
        """Export progress report (placeholder)"""
        # This could be enhanced to export to PDF or text file
        report = self.generate_text_report()
        
        # For now, show in a text window
        report_window = tk.Toplevel(self.window)
        report_window.title("Progress Report")
        report_window.geometry("600x400")
        
        text_widget = tk.Text(report_window, wrap='word', font=('Courier', 10))
        text_widget.pack(fill='both', expand=True, padx=10, pady=10)
        text_widget.insert('1.0', report)
        text_widget.config(state='disabled')
        
        close_btn = tk.Button(report_window, text="Close", command=report_window.destroy)
        close_btn.pack(pady=5)

    def generate_text_report(self):
        """Generate a text-based progress report"""
        report = f"""
PYTHON LEARNING PROGRESS REPORT
================================

Student: {self.user_data['first_name']} {self.user_data['last_name']}
Email: {self.user_data['email']}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERALL SUMMARY
===============
"""
        
        # Calculate totals
        total_topics = len(self.progress_data)
        total_correct = 0
        total_incorrect = 0
        
        for topic, data in self.progress_data.items():
            score_data = data.get('score_data', {})
            for level, scores in score_data.items():
                total_correct += scores.get('correct', 0)
                total_incorrect += scores.get('incorrect', 0)
        
        total_questions = total_correct + total_incorrect
        accuracy = (total_correct/total_questions*100) if total_questions > 0 else 0
        
        report += f"""
Topics Started: {total_topics}
Total Questions: {total_questions}
Correct Answers: {total_correct}
Incorrect Answers: {total_incorrect}
Overall Accuracy: {accuracy:.1f}%

DETAILED BREAKDOWN
==================
"""
        
        for topic, data in sorted(self.progress_data.items()):
            report += f"\n{topic.upper()} QUIZ:\n"
            report += "-" * (len(topic) + 6) + "\n"
            
            score_data = data.get('score_data', {})
            for level in range(1, 6):
                level_data = score_data.get(str(level), {'correct': 0, 'incorrect': 0, 'completed': False})
                correct = level_data.get('correct', 0)
                incorrect = level_data.get('incorrect', 0)
                total = correct + incorrect
                completed = level_data.get('completed', False)
                status = "Complete" if completed else f"In Progress ({total}/15)"
                
                report += f"  Level {level}: {correct} correct, {incorrect} incorrect - {status}\n"
        
        return report

    def close(self):
        """Close the records window"""
        if self.window and self.window.winfo_exists():
            self.window.destroy()