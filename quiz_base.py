# =================================Enhanced Quiz Base with Auto-save + Timer + Bookmarking + Analytics==================================
# quiz_base.py - Enhanced quiz system with auto-save, timer, bookmarking, and detailed analytics functionality
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import shutil
from datetime import datetime, timedelta
import random
import threading
import time

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
        
        # Auto-save tracking
        self.last_auto_save = datetime.now()
        self.auto_save_count = 0
        self.save_status_var = tk.StringVar()
        self.save_status_var.set("💾 Ready")
        self.session_start = datetime.now().isoformat()
        
        # Timer functionality
        self.timer_enabled = False
        self.timer_running = False
        self.question_start_time = None
        self.time_limit = 60  # Default 60 seconds
        self.remaining_time = 0
        self.timer_var = tk.StringVar()
        self.timer_var.set("⏱️ Timer: OFF")
        self.timer_thread = None
        
        # Bookmarking functionality
        self.review_mode = False
        self.current_question_bookmarked = False
        self.bookmark_var = tk.StringVar()
        self.bookmark_var.set("🔖 Bookmark")
        self.bookmarked_questions = []
        self.review_questions = []
        self.bookmark_button = None
        
        # Analytics functionality - NEW
        self.detailed_analytics = {
            'blooms_performance': {str(i): {'correct': 0, 'incorrect': 0, 'total': 0} for i in range(1, 6)},
            'question_type_performance': {},
            'accuracy_trend': [],
            'improvement_tracking': [],
            'session_analytics': [],
            'weakness_areas': [],
            'strength_areas': []
        }
        
        # Timer settings
        self.timer_settings = {
            'enabled': False,
            'time_limit_seconds': 60,
            'auto_submit': True,
            'show_countdown': True,
            'audio_alerts': False,
            'difficulty_multipliers': {
                '1': 1.0,
                '2': 1.2,
                '3': 1.5,
                '4': 1.8,
                '5': 2.0
            }
        }
        
        # Timing data collection
        self.session_timing = {
            'session_start': self.session_start,
            'questions_timing': [],
            'total_questions': 0,
            'total_time': 0
        }
        
        # Progress tracking - initialize with integer keys
        self.progress_data = self.load_progress()
        self.level_scores = {i: {'correct': 0, 'incorrect': 0, 'completed': False} for i in range(1, 6)}
        self.used_questions = {i: [] for i in range(1, 6)}
        
        # Load existing progress, timer settings, bookmarks, and analytics
        if self.progress_data:
            loaded_scores = self.progress_data.get('score_data', {})
            loaded_questions = self.progress_data.get('used_questions', {})
            loaded_timer_settings = self.progress_data.get('timer_settings', {})
            loaded_bookmarks = self.progress_data.get('bookmarked_questions', [])
            loaded_analytics = self.progress_data.get('detailed_analytics', {})
            
            # Convert string keys to integers for level_scores
            for key, value in loaded_scores.items():
                self.level_scores[int(key)] = value
            
            # Convert string keys to integers for used_questions
            for key, value in loaded_questions.items():
                self.used_questions[int(key)] = value
            
            # Load timer settings
            if loaded_timer_settings:
                self.timer_settings.update(loaded_timer_settings)
                self.timer_enabled = self.timer_settings.get('enabled', False)
            
            # Load bookmarks
            self.bookmarked_questions = loaded_bookmarks
            
            # Load analytics
            if loaded_analytics:
                self.detailed_analytics.update(loaded_analytics)

        # Question handlers mapping
        self.question_handlers = {
            'multiple_choice': self.create_multiple_choice,
            'missing_word': self.create_missing_word,
            'syntax_error': self.create_syntax_error,
            'one_word': self.create_one_word,
            'snippet_analysis': self.create_multiple_choice,
            'mix_match': self.create_mix_match
        }

    def show(self):
        """Display the quiz window"""
        self.create_window()
        self.create_header()
        self.create_auto_save_indicator()
        self.create_timer_controls()
        self.create_bookmark_controls()
        self.create_analytics_controls()  # NEW: Analytics controls
        self.create_level_selector()
        self.create_progress_display()
        self.create_question_area()
        self.create_result_area()
        self.create_control_buttons()
        
        # Start auto-save monitoring
        self.start_auto_save_monitoring()
        
        # Load first question
        self.load_next_question()

    def create_window(self):
        """Create the quiz window"""
        self.window = tk.Toplevel(self.parent_root)
        self.window.title(f"Quiz: {self.topic}")
        self.window.geometry("800x850")  # Even taller for analytics controls
        self.window.resizable(False, False)
        
        # Center the window
        self.window.transient(self.parent_root)
        self.window.grab_set()
        
        # Create main frame
        self.main_frame = tk.Frame(self.window, bg='white')
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)

    def create_header(self):
        """Create header with quiz info"""
        header_frame = tk.Frame(self.main_frame, bg='white')
        header_frame.pack(fill='x', pady=(0, 10))
        
        title_label = tk.Label(header_frame, 
                              text=f"🐍 {self.topic.upper()} Quiz",
                              font=('Arial', 16, 'bold'),
                              bg='white',
                              fg='#2e7d32')
        title_label.pack(side='left')
        
        user_label = tk.Label(header_frame,
                             text=f"👤 {self.user_data.get('first_name', 'User')}",
                             font=('Arial', 10),
                             bg='white',
                             fg='gray')
        user_label.pack(side='right')

    def create_auto_save_indicator(self):
        """Create auto-save status indicator"""
        auto_save_frame = tk.Frame(self.main_frame, bg='white')
        auto_save_frame.pack(fill='x', pady=(0, 5))
        
        # Auto-save status label
        self.save_status_label = tk.Label(auto_save_frame,
                                         textvariable=self.save_status_var,
                                         font=('Arial', 8),
                                         bg='white',
                                         fg='green')
        self.save_status_label.pack(side='right')
        
        # Last saved time
        self.last_saved_label = tk.Label(auto_save_frame,
                                        text=f"Last saved: {self.last_auto_save.strftime('%H:%M:%S')}",
                                        font=('Arial', 8),
                                        bg='white',
                                        fg='gray')
        self.last_saved_label.pack(side='right', padx=(0, 10))

    def create_timer_controls(self):
        """Create timer control interface"""
        timer_frame = tk.Frame(self.main_frame, bg='white', relief='sunken', bd=1)
        timer_frame.pack(fill='x', pady=(0, 5))
        
        # Timer display
        self.timer_display = tk.Label(timer_frame,
                                     textvariable=self.timer_var,
                                     font=('Arial', 12, 'bold'),
                                     bg='white',
                                     fg='#1976d2')
        self.timer_display.pack(side='left', padx=10, pady=5)
        
        # Timer toggle button
        self.timer_toggle_btn = tk.Button(timer_frame,
                                         text="ON" if self.timer_enabled else "OFF",
                                         font=('Arial', 9),
                                         width=6,
                                         command=self.toggle_timer,
                                         bg='#4caf50' if self.timer_enabled else '#f44336',
                                         fg='white')
        self.timer_toggle_btn.pack(side='left', padx=5)
        
        # Timer settings button
        settings_btn = tk.Button(timer_frame,
                               text="⚙️ Settings",
                               font=('Arial', 9),
                               command=self.show_timer_settings,
                               bg='#ff9800',
                               fg='white')
        settings_btn.pack(side='left', padx=5)
        
        # Update timer display
        self.update_timer_display()

    def create_bookmark_controls(self):
        """Create bookmark control interface"""
        bookmark_frame = tk.Frame(self.main_frame, bg='white', relief='sunken', bd=1)
        bookmark_frame.pack(fill='x', pady=(0, 5))
        
        # Review mode toggle
        review_mode_var = tk.BooleanVar(value=self.review_mode)
        self.review_mode_cb = tk.Checkbutton(bookmark_frame,
                                           text="📚 Review Mode (Bookmarked Questions Only)",
                                           variable=review_mode_var,
                                           font=('Arial', 10, 'bold'),
                                           bg='white',
                                           command=lambda: self.toggle_review_mode(review_mode_var.get()))
        self.review_mode_cb.pack(side='left', padx=10, pady=5)
        
        # Bookmark stats
        bookmark_count = len(self.bookmarked_questions)
        self.bookmark_stats_label = tk.Label(bookmark_frame,
                                            text=f"📖 Bookmarks: {bookmark_count}",
                                            font=('Arial', 9),
                                            bg='white',
                                            fg='#1976d2')
        self.bookmark_stats_label.pack(side='left', padx=10)
        
        # Manage bookmarks button
        manage_btn = tk.Button(bookmark_frame,
                             text="📋 Manage Bookmarks",
                             font=('Arial', 9),
                             command=self.show_bookmark_manager,
                             bg='#9c27b0',
                             fg='white')
        manage_btn.pack(side='right', padx=5)

    def create_analytics_controls(self):
        """NEW: Create analytics control interface"""
        analytics_frame = tk.Frame(self.main_frame, bg='white', relief='sunken', bd=1)
        analytics_frame.pack(fill='x', pady=(0, 10))
        
        # Analytics title
        analytics_title = tk.Label(analytics_frame,
                                  text="📊 Performance Analytics",
                                  font=('Arial', 10, 'bold'),
                                  bg='white',
                                  fg='#1976d2')
        analytics_title.pack(side='left', padx=10, pady=5)
        
        # Quick stats
        accuracy = self.calculate_overall_accuracy()
        trend = self.get_accuracy_trend()
        
        quick_stats = tk.Label(analytics_frame,
                              text=f"Overall: {accuracy:.1f}% | Trend: {trend}",
                              font=('Arial', 9),
                              bg='white',
                              fg='#666')
        quick_stats.pack(side='left', padx=10)
        
        # Analytics buttons
        detailed_btn = tk.Button(analytics_frame,
                               text="📈 Detailed Analytics",
                               font=('Arial', 9),
                               command=self.show_detailed_analytics,
                               bg='#4caf50',
                               fg='white')
        detailed_btn.pack(side='right', padx=5)
        
        recommendations_btn = tk.Button(analytics_frame,
                                      text="💡 Study Recommendations",
                                      font=('Arial', 9),
                                      command=self.show_study_recommendations,
                                      bg='#ff5722',
                                      fg='white')
        recommendations_btn.pack(side='right', padx=5)

    def calculate_overall_accuracy(self):
        """NEW: Calculate overall accuracy percentage"""
        total_correct = sum(level['correct'] for level in self.level_scores.values())
        total_incorrect = sum(level['incorrect'] for level in self.level_scores.values())
        total = total_correct + total_incorrect
        
        if total == 0:
            return 0.0
        return (total_correct / total) * 100

    def get_accuracy_trend(self):
        """NEW: Get accuracy trend indicator"""
        trends = self.detailed_analytics.get('accuracy_trend', [])
        if len(trends) < 2:
            return "📊 Collecting data"
        
        recent_avg = sum(trends[-3:]) / min(3, len(trends))
        earlier_avg = sum(trends[:-3][-3:]) / min(3, len(trends[:-3])) if len(trends) > 3 else 0
        
        if recent_avg > earlier_avg + 5:
            return "📈 Improving"
        elif recent_avg < earlier_avg - 5:
            return "📉 Declining"
        else:
            return "➡️ Stable"

    def show_detailed_analytics(self):
        """NEW: Show comprehensive analytics dashboard"""
        analytics_window = tk.Toplevel(self.window)
        analytics_window.title("📊 Detailed Performance Analytics")
        analytics_window.geometry("800x600")
        analytics_window.resizable(False, False)
        analytics_window.transient(self.window)
        analytics_window.grab_set()
        
        # Create notebook for tabs
        notebook = ttk.Notebook(analytics_window)
        notebook.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Tab 1: Bloom's Taxonomy Performance
        blooms_frame = ttk.Frame(notebook)
        notebook.add(blooms_frame, text="🎯 Difficulty Analysis")
        self.create_blooms_analysis_tab(blooms_frame)
        
        # Tab 2: Question Type Performance
        types_frame = ttk.Frame(notebook)
        notebook.add(types_frame, text="❓ Question Types")
        self.create_question_types_tab(types_frame)
        
        # Tab 3: Progress Trends
        trends_frame = ttk.Frame(notebook)
        notebook.add(trends_frame, text="📈 Progress Trends")
        self.create_trends_tab(trends_frame)
        
        # Tab 4: Recommendations
        recommendations_frame = ttk.Frame(notebook)
        notebook.add(recommendations_frame, text="💡 Recommendations")
        self.create_recommendations_tab(recommendations_frame)

    def create_blooms_analysis_tab(self, parent):
        """NEW: Create Bloom's taxonomy analysis tab"""
        main_frame = tk.Frame(parent, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="📊 Performance by Difficulty Level (Bloom's Taxonomy)", 
                        font=('Arial', 14, 'bold'), bg='white')
        title.pack(pady=(0, 20))
        
        # Description
        desc = tk.Label(main_frame, 
                       text="Level 1: Remember | Level 2: Understand | Level 3: Apply | Level 4: Analyze | Level 5: Create",
                       font=('Arial', 9), bg='white', fg='gray')
        desc.pack(pady=(0, 15))
        
        # Performance bars
        for level in range(1, 6):
            level_data = self.detailed_analytics['blooms_performance'].get(str(level), 
                                                                          {'correct': 0, 'incorrect': 0, 'total': 0})
            
            level_frame = tk.Frame(main_frame, bg='white')
            level_frame.pack(fill='x', pady=5)
            
            # Level label
            level_label = tk.Label(level_frame, text=f"Level {level}:", 
                                  font=('Arial', 11, 'bold'), bg='white', width=10)
            level_label.pack(side='left')
            
            # Progress bar frame
            bar_frame = tk.Frame(level_frame, bg='#e0e0e0', height=20, relief='sunken', bd=1)
            bar_frame.pack(side='left', fill='x', expand=True, padx=10)
            bar_frame.pack_propagate(False)
            
            # Calculate accuracy
            total = level_data['correct'] + level_data['incorrect']
            if total > 0:
                accuracy = (level_data['correct'] / total) * 100
                bar_width = int(accuracy)
                
                # Color based on performance
                if accuracy >= 80:
                    color = '#4caf50'  # Green
                elif accuracy >= 60:
                    color = '#ff9800'  # Orange
                else:
                    color = '#f44336'  # Red
                
                # Progress bar
                progress_bar = tk.Frame(bar_frame, bg=color, height=18)
                progress_bar.place(x=1, y=1, width=bar_width*2 if bar_width*2 <= 200 else 200)
                
                # Stats label
                stats_text = f"{accuracy:.1f}% ({level_data['correct']}/{total})"
            else:
                stats_text = "No data yet"
            
            stats_label = tk.Label(level_frame, text=stats_text, 
                                  font=('Arial', 10), bg='white', width=15)
            stats_label.pack(side='right')

    def create_question_types_tab(self, parent):
        """NEW: Create question types analysis tab"""
        main_frame = tk.Frame(parent, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="❓ Performance by Question Type", 
                        font=('Arial', 14, 'bold'), bg='white')
        title.pack(pady=(0, 20))
        
        # Question type performance
        question_types = self.detailed_analytics.get('question_type_performance', {})
        
        if not question_types:
            no_data = tk.Label(main_frame, text="📊 No question type data available yet.\nComplete more questions to see analysis.",
                              font=('Arial', 12), bg='white', fg='gray', justify='center')
            no_data.pack(expand=True)
            return
        
        for q_type, data in question_types.items():
            type_frame = tk.Frame(main_frame, bg='white')
            type_frame.pack(fill='x', pady=8)
            
            # Type label
            type_name = q_type.replace('_', ' ').title()
            type_label = tk.Label(type_frame, text=f"{type_name}:", 
                                 font=('Arial', 11, 'bold'), bg='white', width=20)
            type_label.pack(side='left')
            
            # Performance stats
            total = data['correct'] + data['incorrect']
            if total > 0:
                accuracy = (data['correct'] / total) * 100
                avg_time = data.get('avg_time', 0)
                
                stats_text = f"Accuracy: {accuracy:.1f}% ({data['correct']}/{total})"
                if avg_time > 0:
                    stats_text += f" | Avg Time: {avg_time:.1f}s"
                
                color = '#4caf50' if accuracy >= 70 else '#ff9800' if accuracy >= 50 else '#f44336'
            else:
                stats_text = "No data"
                color = '#gray'
            
            stats_label = tk.Label(type_frame, text=stats_text, 
                                  font=('Arial', 10), bg='white', fg=color)
            stats_label.pack(side='left', padx=20)

    def create_trends_tab(self, parent):
        """NEW: Create progress trends tab"""
        main_frame = tk.Frame(parent, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="📈 Progress Trends Over Time", 
                        font=('Arial', 14, 'bold'), bg='white')
        title.pack(pady=(0, 20))
        
        # Accuracy trend
        trend_data = self.detailed_analytics.get('accuracy_trend', [])
        
        if len(trend_data) < 2:
            no_data = tk.Label(main_frame, text="📊 Not enough data for trend analysis yet.\nComplete more quiz sessions to see trends.",
                              font=('Arial', 12), bg='white', fg='gray', justify='center')
            no_data.pack(expand=True)
            return
        
        # Simple text-based trend display
        trend_frame = tk.LabelFrame(main_frame, text="Accuracy Trend", font=('Arial', 11, 'bold'), bg='white')
        trend_frame.pack(fill='x', pady=10)
        
        # Recent sessions
        recent_sessions = trend_data[-10:]  # Last 10 sessions
        
        for i, accuracy in enumerate(recent_sessions):
            session_frame = tk.Frame(trend_frame, bg='white')
            session_frame.pack(fill='x', padx=10, pady=2)
            
            session_label = tk.Label(session_frame, text=f"Session {len(trend_data)-len(recent_sessions)+i+1}:", 
                                    font=('Arial', 10), bg='white', width=15)
            session_label.pack(side='left')
            
            # Visual bar
            bar_frame = tk.Frame(session_frame, bg='#e0e0e0', height=15, width=200, relief='sunken', bd=1)
            bar_frame.pack(side='left', padx=10)
            bar_frame.pack_propagate(False)
            
            bar_width = int(accuracy * 2)  # Scale to 200px max
            color = '#4caf50' if accuracy >= 70 else '#ff9800' if accuracy >= 50 else '#f44336'
            
            progress_bar = tk.Frame(bar_frame, bg=color, height=13)
            progress_bar.place(x=1, y=1, width=bar_width)
            
            accuracy_label = tk.Label(session_frame, text=f"{accuracy:.1f}%", 
                                     font=('Arial', 10), bg='white')
            accuracy_label.pack(side='left', padx=10)

    def create_recommendations_tab(self, parent):
        """NEW: Create personalized recommendations tab"""
        main_frame = tk.Frame(parent, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="💡 Personalized Study Recommendations", 
                        font=('Arial', 14, 'bold'), bg='white')
        title.pack(pady=(0, 20))
        
        # Generate recommendations
        recommendations = self.generate_study_recommendations()
        
        # Display recommendations
        for i, recommendation in enumerate(recommendations):
            rec_frame = tk.LabelFrame(main_frame, text=f"Recommendation {i+1}", 
                                     font=('Arial', 11, 'bold'), bg='white')
            rec_frame.pack(fill='x', pady=10)
            
            # Priority indicator
            priority_colors = {'High': '#f44336', 'Medium': '#ff9800', 'Low': '#4caf50'}
            priority_color = priority_colors.get(recommendation['priority'], '#gray')
            
            priority_label = tk.Label(rec_frame, text=f"Priority: {recommendation['priority']}", 
                                     font=('Arial', 10, 'bold'), bg='white', fg=priority_color)
            priority_label.pack(anchor='w', padx=10, pady=(5, 0))
            
            # Recommendation text
            rec_text = tk.Label(rec_frame, text=recommendation['text'], 
                               font=('Arial', 10), bg='white', wraplength=700, justify='left')
            rec_text.pack(anchor='w', padx=10, pady=(5, 10))

    def generate_study_recommendations(self):
        """NEW: Generate personalized study recommendations"""
        recommendations = []
        
        # Analyze weak areas by Bloom's taxonomy
        for level in range(1, 6):
            level_data = self.detailed_analytics['blooms_performance'].get(str(level), 
                                                                          {'correct': 0, 'incorrect': 0})
            total = level_data['correct'] + level_data['incorrect']
            
            if total >= 5:  # Enough data to make recommendations
                accuracy = (level_data['correct'] / total) * 100
                
                if accuracy < 50:
                    recommendations.append({
                        'priority': 'High',
                        'text': f"Focus on Level {level} questions. Your accuracy is {accuracy:.1f}%. "
                               f"Try the Review Mode with bookmarked Level {level} questions."
                    })
                elif accuracy < 70:
                    recommendations.append({
                        'priority': 'Medium',
                        'text': f"Improve Level {level} performance. Current accuracy: {accuracy:.1f}%. "
                               f"Practice more questions at this difficulty level."
                    })
        
        # Analyze question types
        question_types = self.detailed_analytics.get('question_type_performance', {})
        for q_type, data in question_types.items():
            total = data['correct'] + data['incorrect']
            if total >= 3:
                accuracy = (data['correct'] / total) * 100
                if accuracy < 60:
                    type_name = q_type.replace('_', ' ').title()
                    recommendations.append({
                        'priority': 'Medium',
                        'text': f"Practice {type_name} questions more. Current accuracy: {accuracy:.1f}%. "
                               f"These question types need more attention."
                    })
        
        # Timing recommendations
        speed_stats = self.calculate_speed_stats()
        if speed_stats and speed_stats.get('average_time', 0) > 90:
            recommendations.append({
                'priority': 'Low',
                'text': f"Consider practicing with the timer enabled. Your average response time is "
                       f"{speed_stats['average_time']:.1f} seconds. Faster decision-making can help in tests."
            })
        
        # Bookmark recommendations
        if len(self.bookmarked_questions) > 5:
            recommendations.append({
                'priority': 'Medium',
                'text': f"You have {len(self.bookmarked_questions)} bookmarked questions. "
                       f"Use Review Mode to practice these challenging questions regularly."
            })
        
        # Default recommendation if no specific issues found
        if not recommendations:
            recommendations.append({
                'priority': 'Low',
                'text': "Great job! Your performance is solid across all areas. "
                       "Continue practicing to maintain and improve your skills."
            })
        
        return recommendations[:5]  # Limit to 5 recommendations

    def show_study_recommendations(self):
        """NEW: Show study recommendations popup"""
        recommendations = self.generate_study_recommendations()
        
        rec_window = tk.Toplevel(self.window)
        rec_window.title("💡 Study Recommendations")
        rec_window.geometry("600x400")
        rec_window.resizable(False, False)
        rec_window.transient(self.window)
        rec_window.grab_set()
        
        main_frame = tk.Frame(rec_window, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="💡 Personalized Study Recommendations", 
                        font=('Arial', 14, 'bold'), bg='white')
        title.pack(pady=(0, 20))
        
        # Scrollable recommendations
        canvas = tk.Canvas(main_frame, bg='white')
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Display recommendations
        for i, rec in enumerate(recommendations):
            rec_frame = tk.Frame(scrollable_frame, bg='white', relief='raised', bd=1)
            rec_frame.pack(fill='x', pady=5, padx=5)
            
            priority_colors = {'High': '#f44336', 'Medium': '#ff9800', 'Low': '#4caf50'}
            priority_color = priority_colors.get(rec['priority'], '#gray')
            
            header = tk.Label(rec_frame, text=f"{i+1}. {rec['priority']} Priority", 
                             font=('Arial', 11, 'bold'), bg='white', fg=priority_color)
            header.pack(anchor='w', padx=10, pady=(5, 0))
            
            text = tk.Label(rec_frame, text=rec['text'], 
                           font=('Arial', 10), bg='white', wraplength=500, justify='left')
            text.pack(anchor='w', padx=10, pady=(0, 10))

    def record_analytics_data(self, is_correct):
        """NEW: Record detailed analytics data for current question"""
        if not self.current_question:
            return
        
        level = str(self.current_level)
        question_type = self.current_question['type']
        
        # Update Bloom's taxonomy performance
        if level not in self.detailed_analytics['blooms_performance']:
            self.detailed_analytics['blooms_performance'][level] = {'correct': 0, 'incorrect': 0, 'total': 0}
        
        if is_correct:
            self.detailed_analytics['blooms_performance'][level]['correct'] += 1
        else:
            self.detailed_analytics['blooms_performance'][level]['incorrect'] += 1
        
        self.detailed_analytics['blooms_performance'][level]['total'] += 1
        
        # Update question type performance
        if question_type not in self.detailed_analytics['question_type_performance']:
            self.detailed_analytics['question_type_performance'][question_type] = {
                'correct': 0, 'incorrect': 0, 'total_time': 0, 'questions': 0, 'avg_time': 0
            }
        
        type_data = self.detailed_analytics['question_type_performance'][question_type]
        if is_correct:
            type_data['correct'] += 1
        else:
            type_data['incorrect'] += 1
        
        # Record timing for question type
        if self.question_start_time:
            time_taken = time.time() - self.question_start_time
            type_data['total_time'] += time_taken
            type_data['questions'] += 1
            type_data['avg_time'] = type_data['total_time'] / type_data['questions']
        
        # Update session accuracy for trend tracking
        current_accuracy = self.calculate_overall_accuracy()
        self.detailed_analytics['accuracy_trend'].append(current_accuracy)
        
        # Limit trend data to last 50 sessions
        if len(self.detailed_analytics['accuracy_trend']) > 50:
            self.detailed_analytics['accuracy_trend'] = self.detailed_analytics['accuracy_trend'][-50:]

    # ===== EXISTING METHODS (Enhanced with analytics integration) =====

    def toggle_timer(self):
        """Toggle timer on/off"""
        self.timer_enabled = not self.timer_enabled
        self.timer_settings['enabled'] = self.timer_enabled
        
        # Update button
        self.timer_toggle_btn.config(
            text="ON" if self.timer_enabled else "OFF",
            bg='#4caf50' if self.timer_enabled else '#f44336'
        )
        
        # Update display
        self.update_timer_display()
        
        # Save settings
        self.save_timer_settings()
        
        # If timer was turned on during a question, start it
        if self.timer_enabled and not self.answer_submitted:
            self.start_question_timer()

    def show_timer_settings(self):
        """Show timer settings dialog"""
        settings_window = tk.Toplevel(self.window)
        settings_window.title("Timer Settings")
        settings_window.geometry("400x500")
        settings_window.resizable(False, False)
        settings_window.transient(self.window)
        settings_window.grab_set()
        
        main_frame = tk.Frame(settings_window, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="⏱️ Timer Settings", 
                        font=('Arial', 14, 'bold'), bg='white')
        title.pack(pady=(0, 20))
        
        # Enable timer checkbox
        enable_var = tk.BooleanVar(value=self.timer_settings['enabled'])
        enable_cb = tk.Checkbutton(main_frame, text="Enable Timer",
                                  variable=enable_var, font=('Arial', 11),
                                  bg='white')
        enable_cb.pack(anchor='w', pady=5)
        
        # Time limit setting
        time_frame = tk.Frame(main_frame, bg='white')
        time_frame.pack(fill='x', pady=10)
        
        tk.Label(time_frame, text="Base Time Limit:", font=('Arial', 10), bg='white').pack(side='left')
        time_var = tk.IntVar(value=self.timer_settings['time_limit_seconds'])
        time_spin = tk.Spinbox(time_frame, from_=30, to=300, textvariable=time_var,
                              width=10, font=('Arial', 10))
        time_spin.pack(side='left', padx=5)
        tk.Label(time_frame, text="seconds", font=('Arial', 10), bg='white').pack(side='left')
        
        # Auto-submit checkbox
        auto_submit_var = tk.BooleanVar(value=self.timer_settings['auto_submit'])
        auto_submit_cb = tk.Checkbutton(main_frame, text="Auto-submit when time expires",
                                       variable=auto_submit_var, font=('Arial', 11),
                                       bg='white')
        auto_submit_cb.pack(anchor='w', pady=5)
        
        # Show countdown checkbox
        countdown_var = tk.BooleanVar(value=self.timer_settings['show_countdown'])
        countdown_cb = tk.Checkbutton(main_frame, text="Show countdown timer",
                                     variable=countdown_var, font=('Arial', 11),
                                     bg='white')
        countdown_cb.pack(anchor='w', pady=5)
        
        # Difficulty multipliers
        diff_frame = tk.LabelFrame(main_frame, text="Time by Difficulty Level", 
                                  font=('Arial', 10, 'bold'), bg='white')
        diff_frame.pack(fill='x', pady=20)
        
        multiplier_vars = {}
        for level in range(1, 6):
            level_frame = tk.Frame(diff_frame, bg='white')
            level_frame.pack(fill='x', padx=10, pady=2)
            
            tk.Label(level_frame, text=f"Level {level}:", 
                    font=('Arial', 10), bg='white', width=10).pack(side='left')
            
            multiplier = self.timer_settings['difficulty_multipliers'].get(str(level), 1.0)
            mult_var = tk.DoubleVar(value=multiplier)
            multiplier_vars[level] = mult_var
            
            mult_spin = tk.Spinbox(level_frame, from_=0.5, to=3.0, increment=0.1,
                                  textvariable=mult_var, width=8, font=('Arial', 10))
            mult_spin.pack(side='left', padx=5)
            
            # Show calculated time
            calc_time = int(time_var.get() * multiplier)
            time_label = tk.Label(level_frame, text=f"({calc_time}s)",
                                 font=('Arial', 9), bg='white', fg='gray')
            time_label.pack(side='left', padx=5)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(fill='x', pady=20)
        
        def save_settings():
            # Update timer settings
            self.timer_settings['enabled'] = enable_var.get()
            self.timer_settings['time_limit_seconds'] = time_var.get()
            self.timer_settings['auto_submit'] = auto_submit_var.get()
            self.timer_settings['show_countdown'] = countdown_var.get()
            
            # Update multipliers
            for level, var in multiplier_vars.items():
                self.timer_settings['difficulty_multipliers'][str(level)] = var.get()
            
            # Apply changes
            self.timer_enabled = self.timer_settings['enabled']
            self.toggle_timer() if self.timer_enabled != (self.timer_toggle_btn['text'] == 'ON') else None
            self.save_timer_settings()
            
            settings_window.destroy()
            messagebox.showinfo("Settings Saved", "Timer settings have been saved!")
        
        tk.Button(button_frame, text="Save", command=save_settings,
                 bg='#4caf50', fg='white', font=('Arial', 11)).pack(side='right', padx=5)
        tk.Button(button_frame, text="Cancel", command=settings_window.destroy,
                 bg='#f44336', fg='white', font=('Arial', 11)).pack(side='right')

    def start_question_timer(self):
        """Start timer for current question"""
        if not self.timer_enabled or self.answer_submitted:
            return
        
        # Calculate time limit for current question level
        base_time = self.timer_settings['time_limit_seconds']
        multiplier = self.timer_settings['difficulty_multipliers'].get(str(self.current_level), 1.0)
        self.time_limit = int(base_time * multiplier)
        self.remaining_time = self.time_limit
        
        # Record question start time
        self.question_start_time = time.time()
        
        # Start timer thread
        self.timer_running = True
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_running = False
            self.timer_thread.join()
        
        self.timer_thread = threading.Thread(target=self.timer_countdown, daemon=True)
        self.timer_thread.start()

    def timer_countdown(self):
        """Timer countdown thread"""
        while self.timer_running and self.remaining_time > 0 and not self.answer_submitted:
            if hasattr(self, 'window') and self.window and self.window.winfo_exists():
                self.window.after(0, self.update_timer_display)
            
            time.sleep(1)
            self.remaining_time -= 1
        
        # Time's up!
        if self.timer_running and self.remaining_time <= 0 and not self.answer_submitted:
            if hasattr(self, 'window') and self.window and self.window.winfo_exists():
                self.window.after(0, self.handle_timeout)

    def update_timer_display(self):
        """Update timer display"""
        if not self.timer_enabled:
            self.timer_var.set("⏱️ Timer: OFF")
            self.timer_display.config(fg='gray')
            return
        
        if not self.timer_running:
            self.timer_var.set("⏱️ Timer: READY")
            self.timer_display.config(fg='#1976d2')
            return
        
        # Format time display
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        
        # Color coding based on remaining time
        if self.remaining_time > 30:
            color = '#4caf50'  # Green
            self.timer_var.set(f"⏱️ Time: {time_str}")
        elif self.remaining_time > 10:
            color = '#ff9800'  # Orange
            self.timer_var.set(f"⏱️ Time: {time_str} ⚠️")
        else:
            color = '#f44336'  # Red
            self.timer_var.set(f"⏱️ Time: {time_str} 🚨")
        
        self.timer_display.config(fg=color)

    def handle_timeout(self):
        """Handle when timer expires"""
        if self.answer_submitted:
            return
        
        self.timer_running = False
        
        # Record timing data
        self.record_question_timing(timeout=True)
        
        if self.timer_settings['auto_submit']:
            # Auto-submit (count as incorrect)
            self.answer_submitted = True
            self.level_scores[self.current_level]['incorrect'] += 1
            
            # Record analytics for timeout (incorrect)
            self.record_analytics_data(False)
            
            self.update_progress_display()
            self.auto_save_progress()
            
            # Show timeout message
            for widget in self.result_frame.winfo_children():
                widget.destroy()
            
            timeout_label = tk.Label(self.result_frame,
                                   text="⏰ Time's Up! Question auto-submitted as incorrect.",
                                   font=('Arial', 12, 'bold'),
                                   bg='#ffebee',
                                   fg='#c62828',
                                   relief='raised',
                                   bd=2)
            timeout_label.pack(fill='x', pady=5)
            
            # Move to next question after 3 seconds
            self.window.after(3000, self.load_next_question)
        else:
            # Just show warning, let student continue
            messagebox.showwarning("Time's Up!", 
                                 f"Time limit of {self.time_limit} seconds has expired.\n"
                                 f"You can still submit your answer.")

    def record_question_timing(self, timeout=False):
        """Record timing data for current question"""
        if not self.question_start_time:
            return
        
        time_taken = time.time() - self.question_start_time
        
        question_timing = {
            'question_id': f"{self.topic}_level{self.current_level}_q{len(self.session_timing['questions_timing']) + 1}",
            'level': self.current_level,
            'time_taken': round(time_taken, 1),
            'time_limit': self.time_limit if self.timer_enabled else None,
            'timeout': timeout,
            'timestamp': datetime.now().isoformat()
        }
        
        self.session_timing['questions_timing'].append(question_timing)
        self.session_timing['total_questions'] += 1
        self.session_timing['total_time'] += time_taken

    def calculate_speed_stats(self):
        """Calculate speed statistics"""
        timings = self.session_timing['questions_timing']
        if not timings:
            return {}
        
        times = [t['time_taken'] for t in timings if not t['timeout']]
        if not times:
            return {}
        
        return {
            'average_time': round(sum(times) / len(times), 1),
            'fastest_time': round(min(times), 1),
            'slowest_time': round(max(times), 1),
            'timeout_count': len([t for t in timings if t['timeout']]),
            'under_30sec_count': len([t for t in times if t <= 30]),
            'total_questions': len(timings)
        }

    def save_timer_settings(self):
        """Save timer settings to file"""
        try:
            self.auto_save_progress()  # This will include timer settings
        except Exception as e:
            print(f"Error saving timer settings: {e}")

    # ===== BOOKMARK METHODS (Existing) =====

    def toggle_review_mode(self, enabled):
        """Toggle review mode on/off"""
        self.review_mode = enabled
        
        if self.review_mode:
            if not self.bookmarked_questions:
                messagebox.showinfo("No Bookmarks", 
                                  "You haven't bookmarked any questions yet!\n"
                                  "Bookmark difficult questions during regular mode to review them later.")
                self.review_mode_cb.deselect()
                self.review_mode = False
                return
            
            # Prepare review questions
            self.prepare_review_questions()
            messagebox.showinfo("Review Mode", 
                              f"Review mode activated!\n"
                              f"You will only see your {len(self.review_questions)} bookmarked questions.")
        else:
            messagebox.showinfo("Regular Mode", "Regular mode activated! You will see all questions.")
        
        # Restart current level
        self.load_next_question()

    def prepare_review_questions(self):
        """Prepare bookmarked questions for review"""
        self.review_questions = []
        
        for bookmark in self.bookmarked_questions:
            # Find the actual question object
            question_level = bookmark['level']
            question_text = bookmark['question_text']
            
            # Find matching question in questions list
            for question in self.questions:
                if (question['level'] == question_level and 
                    question['question'] == question_text):
                    self.review_questions.append(question)
                    break

    def show_bookmark_manager(self):
        """Show bookmark management dialog"""
        if not self.bookmarked_questions:
            messagebox.showinfo("No Bookmarks", "You haven't bookmarked any questions yet!")
            return
        
        manager_window = tk.Toplevel(self.window)
        manager_window.title("Bookmark Manager")
        manager_window.geometry("700x500")
        manager_window.resizable(False, False)
        manager_window.transient(self.window)
        manager_window.grab_set()
        
        main_frame = tk.Frame(manager_window, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        title = tk.Label(main_frame, text="📚 Your Bookmarked Questions", 
                        font=('Arial', 14, 'bold'), bg='white')
        title.pack(pady=(0, 20))
        
        # Create scrollable list
        list_frame = tk.Frame(main_frame, bg='white')
        list_frame.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Listbox for bookmarks
        bookmark_listbox = tk.Listbox(list_frame, 
                                     yscrollcommand=scrollbar.set,
                                     font=('Arial', 10),
                                     height=15)
        bookmark_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=bookmark_listbox.yview)
        
        # Populate listbox
        for i, bookmark in enumerate(self.bookmarked_questions):
            date_added = bookmark['bookmarked_date'][:10]  # Just the date part
            level = bookmark['level']
            question_preview = bookmark['question_text'][:60] + "..." if len(bookmark['question_text']) > 60 else bookmark['question_text']
            
            display_text = f"Level {level} | {date_added} | {question_preview}"
            bookmark_listbox.insert(tk.END, display_text)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(fill='x', pady=20)
        
        def remove_bookmark():
            selection = bookmark_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please select a bookmark to remove.")
                return
            
            index = selection[0]
            bookmark = self.bookmarked_questions[index]
            
            if messagebox.askyesno("Remove Bookmark", 
                                 f"Remove bookmark for:\n{bookmark['question_text'][:100]}..."):
                self.bookmarked_questions.pop(index)
                bookmark_listbox.delete(index)
                self.update_bookmark_stats()
                self.auto_save_progress()
                messagebox.showinfo("Removed", "Bookmark removed successfully!")
        
        def clear_all_bookmarks():
            if messagebox.askyesno("Clear All", 
                                 f"Remove all {len(self.bookmarked_questions)} bookmarks?"):
                self.bookmarked_questions.clear()
                bookmark_listbox.delete(0, tk.END)
                self.update_bookmark_stats()
                self.auto_save_progress()
                messagebox.showinfo("Cleared", "All bookmarks cleared!")
        
        # Buttons
        tk.Button(button_frame, text="Remove Selected", command=remove_bookmark,
                 bg='#f44336', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(button_frame, text="Clear All", command=clear_all_bookmarks,
                 bg='#ff5722', fg='white', font=('Arial', 10)).pack(side='left', padx=5)
        tk.Button(button_frame, text="Close", command=manager_window.destroy,
                 bg='#4caf50', fg='white', font=('Arial', 10)).pack(side='right', padx=5)

    def update_bookmark_stats(self):
        """Update bookmark statistics display"""
        bookmark_count = len(self.bookmarked_questions)
        if hasattr(self, 'bookmark_stats_label'):
            self.bookmark_stats_label.config(text=f"📖 Bookmarks: {bookmark_count}")

    def bookmark_current_question(self):
        """Bookmark the current question"""
        if not self.current_question:
            return
        
        # Check if already bookmarked
        question_id = self.generate_question_id()
        for bookmark in self.bookmarked_questions:
            if bookmark.get('question_id') == question_id:
                # Already bookmarked - remove it
                self.bookmarked_questions.remove(bookmark)
                self.current_question_bookmarked = False
                self.bookmark_var.set("🔖 Bookmark")
                self.bookmark_button.config(bg='#2196f3')
                self.update_bookmark_stats()
                self.auto_save_progress()
                messagebox.showinfo("Bookmark Removed", "Question removed from bookmarks!")
                return
        
        # Add new bookmark
        bookmark_data = {
            'question_id': question_id,
            'level': self.current_level,
            'question_text': self.current_question['question'],
            'question_type': self.current_question['type'],
            'correct_answer': self.current_question['correct_answer'],
            'bookmarked_date': datetime.now().isoformat(),
            'review_count': 0,
            'last_reviewed': None,
            'difficulty_note': ""  # Students can add notes later
        }
        
        self.bookmarked_questions.append(bookmark_data)
        self.current_question_bookmarked = True
        self.bookmark_var.set("⭐ Bookmarked")
        self.bookmark_button.config(bg='#ff9800')
        self.update_bookmark_stats()
        self.auto_save_progress()
        
        # Show confirmation with option to add note
        if messagebox.askyesno("Question Bookmarked", 
                             "Question added to bookmarks!\n\nWould you like to add a difficulty note?"):
            self.add_bookmark_note(bookmark_data)

    def add_bookmark_note(self, bookmark_data):
        """Add a difficulty note to a bookmark"""
        note_window = tk.Toplevel(self.window)
        note_window.title("Add Note")
        note_window.geometry("400x200")
        note_window.resizable(False, False)
        note_window.transient(self.window)
        note_window.grab_set()
        
        main_frame = tk.Frame(note_window, bg='white')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(main_frame, text="Add a note about why this question is difficult:",
                font=('Arial', 11), bg='white').pack(pady=(0, 10))
        
        note_text = tk.Text(main_frame, height=5, font=('Arial', 10))
        note_text.pack(fill='both', expand=True, pady=(0, 10))
        
        def save_note():
            note = note_text.get('1.0', tk.END).strip()
            if note:
                bookmark_data['difficulty_note'] = note
                self.auto_save_progress()
                messagebox.showinfo("Note Saved", "Difficulty note saved with bookmark!")
            note_window.destroy()
        
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(fill='x')
        
        tk.Button(button_frame, text="Save", command=save_note,
                 bg='#4caf50', fg='white').pack(side='right', padx=5)
        tk.Button(button_frame, text="Skip", command=note_window.destroy,
                 bg='#f44336', fg='white').pack(side='right')

    def generate_question_id(self):
        """Generate unique ID for current question"""
        return f"{self.topic}_level{self.current_level}_q{self.current_question['question'][:20]}"

    def check_if_bookmarked(self):
        """Check if current question is bookmarked"""
        if not self.current_question:
            return False
        
        question_id = self.generate_question_id()
        for bookmark in self.bookmarked_questions:
            if bookmark.get('question_id') == question_id:
                return True
        return False

    def update_bookmark_button(self):
        """Update bookmark button appearance"""
        if self.check_if_bookmarked():
            self.current_question_bookmarked = True
            self.bookmark_var.set("⭐ Bookmarked")
            if self.bookmark_button:
                self.bookmark_button.config(bg='#ff9800')
        else:
            self.current_question_bookmarked = False
            self.bookmark_var.set("🔖 Bookmark")
            if self.bookmark_button:
                self.bookmark_button.config(bg='#2196f3')

    # ===== AUTO-SAVE METHODS (Existing) =====

    def start_auto_save_monitoring(self):
        """Start background auto-save monitoring"""
        def monitor_auto_save():
            while hasattr(self, 'window') and self.window and self.window.winfo_exists():
                try:
                    # Check if it's been more than 30 seconds since last save
                    time_since_save = datetime.now() - self.last_auto_save
                    if time_since_save > timedelta(seconds=30):
                        self.auto_save_progress()
                    
                    # Update UI every 5 seconds
                    if hasattr(self, 'window') and self.window and self.window.winfo_exists():
                        self.window.after(0, self.update_save_status)
                    
                    threading.Event().wait(5)  # Wait 5 seconds
                except:
                    break
        
        # Start monitoring in background thread
        monitor_thread = threading.Thread(target=monitor_auto_save, daemon=True)
        monitor_thread.start()

    def update_save_status(self):
        """Update the auto-save status display"""
        if hasattr(self, 'last_saved_label') and self.last_saved_label.winfo_exists():
            self.last_saved_label.config(text=f"Last saved: {self.last_auto_save.strftime('%H:%M:%S')}")

    def auto_save_progress(self):
        """Enhanced auto-save with visual feedback"""
        try:
            # Show saving status
            self.save_status_var.set("💾 Saving...")
            if hasattr(self, 'save_status_label') and self.save_status_label.winfo_exists():
                self.save_status_label.config(fg='orange')
            
            # Create backup before saving
            self.create_backup()
            
            # Save progress
            self.save_progress()
            
            # Update auto-save tracking
            self.last_auto_save = datetime.now()
            self.auto_save_count += 1
            
            # Show success status
            self.save_status_var.set(f"✅ Saved ({self.auto_save_count})")
            if hasattr(self, 'save_status_label') and self.save_status_label.winfo_exists():
                self.save_status_label.config(fg='green')
            
            # Reset to ready after 2 seconds
            if hasattr(self, 'window') and self.window and self.window.winfo_exists():
                self.window.after(2000, lambda: self.save_status_var.set("💾 Ready"))
                self.window.after(2000, lambda: self.save_status_label.config(fg='green') if hasattr(self, 'save_status_label') and self.save_status_label.winfo_exists() else None)
            
        except Exception as e:
            # Show error status
            self.save_status_var.set("❌ Save Error")
            if hasattr(self, 'save_status_label') and self.save_status_label.winfo_exists():
                self.save_status_label.config(fg='red')
            print(f"Auto-save error: {e}")

    def create_backup(self):
        """Create timestamped backup files"""
        try:
            filename = f"quiz_progress_{self.topic}_{self.user_data['email'].replace('@', '_').replace('.', '_')}.json"
            
            if os.path.exists(filename):
                # Create backups directory if it doesn't exist
                backup_dir = "quiz_backups"
                if not os.path.exists(backup_dir):
                    os.makedirs(backup_dir)
                
                # Create timestamped backup
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_filename = f"{backup_dir}/quiz_progress_{self.topic}_{self.user_data['email'].replace('@', '_').replace('.', '_')}_{timestamp}.json"
                
                shutil.copy2(filename, backup_filename)
                
                # Clean old backups (keep only last 10)
                self.cleanup_old_backups(backup_dir)
                
        except Exception as e:
            print(f"Backup creation error: {e}")

    def cleanup_old_backups(self, backup_dir):
        """Clean up old backup files, keeping only the most recent 10"""
        try:
            user_email_safe = self.user_data['email'].replace('@', '_').replace('.', '_')
            pattern = f"quiz_progress_{self.topic}_{user_email_safe}_"
            
            # Get all backup files for this user/topic
            backup_files = [f for f in os.listdir(backup_dir) if f.startswith(pattern)]
            backup_files.sort(reverse=True)  # Most recent first
            
            # Remove files beyond the 10 most recent
            for old_file in backup_files[10:]:
                try:
                    os.remove(os.path.join(backup_dir, old_file))
                except:
                    pass
        except Exception as e:
            print(f"Backup cleanup error: {e}")

    def recover_from_backup(self):
        """Recover data from most recent backup if needed"""
        try:
            backup_dir = "quiz_backups"
            if not os.path.exists(backup_dir):
                return False
            
            user_email_safe = self.user_data['email'].replace('@', '_').replace('.', '_')
            pattern = f"quiz_progress_{self.topic}_{user_email_safe}_"
            
            # Find most recent backup
            backup_files = [f for f in os.listdir(backup_dir) if f.startswith(pattern)]
            if not backup_files:
                return False
            
            backup_files.sort(reverse=True)  # Most recent first
            latest_backup = os.path.join(backup_dir, backup_files[0])
            
            # Copy backup to main file
            main_filename = f"quiz_progress_{self.topic}_{self.user_data['email'].replace('@', '_').replace('.', '_')}.json"
            shutil.copy2(latest_backup, main_filename)
            
            return True
        except Exception as e:
            print(f"Recovery error: {e}")
            return False

    def load_progress(self):
        """Enhanced load_progress with recovery option"""
        filename = f"quiz_progress_{self.topic}_{self.user_data['email'].replace('@', '_').replace('.', '_')}.json"
        
        # Try to load main file
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    # Validate the loaded data
                    if self.validate_progress_data(data):
                        return data
                    else:
                        print("Invalid data detected, attempting recovery...")
            except Exception as e:
                print(f"Error loading progress: {e}")
        
        # If main file doesn't exist or is corrupt, try recovery
        if self.recover_from_backup():
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    if self.validate_progress_data(data):
                        messagebox.showinfo("Recovery", "Progress recovered from backup!")
                        return data
            except:
                pass
        
        return None

    def validate_progress_data(self, data):
        """Validate progress data integrity"""
        try:
            # Check required fields
            required_fields = ['user_email', 'demo_topic', 'score_data', 'used_questions', 'last_updated']
            for field in required_fields:
                if field not in data:
                    return False
            
            # Check data types
            if not isinstance(data['score_data'], dict):
                return False
            if not isinstance(data['used_questions'], dict):
                return False
            
            return True
        except:
            return False

    def save_progress(self):
        """Enhanced save_progress with timer, bookmark, and analytics data"""
        filename = f"quiz_progress_{self.topic}_{self.user_data['email'].replace('@', '_').replace('.', '_')}.json"
        
        # Convert integer keys to strings for JSON compatibility
        score_data_str_keys = {str(k): v for k, v in self.level_scores.items()}
        used_questions_str_keys = {str(k): v for k, v in self.used_questions.items()}
        
        # Calculate speed stats
        speed_stats = self.calculate_speed_stats()
        
        progress_data = {
            'user_email': self.user_data['email'],
            'demo_topic': self.topic,
            'score_data': score_data_str_keys,
            'used_questions': used_questions_str_keys,
            'last_updated': datetime.now().isoformat(),
            'save_count': getattr(self, 'auto_save_count', 0),
            'session_start': getattr(self, 'session_start', datetime.now().isoformat()),
            
            # Timer and timing data
            'timer_settings': self.timer_settings,
            'session_timing': self.session_timing,
            'speed_stats': speed_stats,
            
            # Bookmark data
            'bookmarked_questions': self.bookmarked_questions,
            'bookmark_stats': {
                'total_bookmarks': len(self.bookmarked_questions),
                'bookmarks_by_level': self.get_bookmarks_by_level(),
                'last_bookmark_date': self.get_last_bookmark_date()
            },
            
            # NEW: Detailed analytics data
            'detailed_analytics': self.detailed_analytics
        }
        
        try:
            # Write to temporary file first
            temp_filename = filename + '.tmp'
            with open(temp_filename, 'w') as f:
                json.dump(progress_data, f, indent=2)
            
            # If write successful, replace main file
            if os.path.exists(temp_filename):
                shutil.move(temp_filename, filename)
                
        except Exception as e:
            print(f"Failed to save progress: {e}")
            # Clean up temp file if it exists
            if os.path.exists(temp_filename):
                try:
                    os.remove(temp_filename)
                except:
                    pass
            raise

    def get_bookmarks_by_level(self):
        """Get bookmark count by difficulty level"""
        level_counts = {str(i): 0 for i in range(1, 6)}
        for bookmark in self.bookmarked_questions:
            level = str(bookmark.get('level', 1))
            if level in level_counts:
                level_counts[level] += 1
        return level_counts

    def get_last_bookmark_date(self):
        """Get date of most recent bookmark"""
        if not self.bookmarked_questions:
            return None
        
        dates = [bookmark.get('bookmarked_date') for bookmark in self.bookmarked_questions if bookmark.get('bookmarked_date')]
        return max(dates) if dates else None

    # ===== QUIZ FLOW METHODS (Enhanced with analytics) =====

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
        
        self.progress_text = tk.Text(self.progress_frame, height=6, font=('Arial', 9),
                                    bg='#f8f8f8', relief='flat', wrap='word',
                                    state='disabled')
        self.progress_text.pack(fill='x', padx=10, pady=5)
        
        self.update_progress_display()

    def create_question_area(self):
        self.question_frame = tk.LabelFrame(self.main_frame, text="Question", 
                                          font=('Arial', 10, 'bold'), bg='white')
        self.question_frame.pack(fill='both', expand=True, pady=(0, 10))

    def create_result_area(self):
        self.result_frame = tk.Frame(self.main_frame, bg='white')
        self.result_frame.pack(fill='x', pady=(0, 10))

    def create_control_buttons(self):
        """Create control buttons including bookmark button"""
        button_frame = tk.Frame(self.main_frame, bg='white')
        button_frame.pack(fill='x', pady=(10, 0))
        
        # Left side buttons
        left_frame = tk.Frame(button_frame, bg='white')
        left_frame.pack(side='left')
        
        skip_btn = tk.Button(left_frame,
                            text="⏭ Skip Question",
                            font=('Arial', 10),
                            command=self.skip_question,
                            bg='#FF9800',
                            fg='white',
                            relief='raised',
                            bd=2)
        skip_btn.pack(side='left', padx=(0, 10))
        
        # Bookmark button
        self.bookmark_button = tk.Button(left_frame,
                                        textvariable=self.bookmark_var,
                                        font=('Arial', 10),
                                        command=self.bookmark_current_question,
                                        bg='#2196f3',
                                        fg='white',
                                        relief='raised',
                                        bd=2)
        self.bookmark_button.pack(side='left', padx=(0, 10))
        
        # Right side button
        exit_btn = tk.Button(button_frame,
                            text="❌ Exit Quiz",
                            font=('Arial', 10),
                            command=self.close,
                            bg='#f44336',
                            fg='white',
                            relief='raised',
                            bd=2)
        exit_btn.pack(side='right')

    def select_level(self, level):
        # Stop any running timer
        self.timer_running = False
        
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
        
        # Add timing summary if available
        speed_stats = self.calculate_speed_stats()
        if speed_stats and speed_stats['total_questions'] > 0:
            progress_lines.append("")
            progress_lines.append(f"⏱️ Session Stats: {speed_stats['total_questions']} questions, "
                                f"avg {speed_stats['average_time']}s, "
                                f"fastest {speed_stats['fastest_time']}s")
        
        # Add bookmark summary
        if self.bookmarked_questions:
            progress_lines.append("")
            progress_lines.append(f"🔖 Bookmarks: {len(self.bookmarked_questions)} saved for review")
        
        # Add analytics summary
        accuracy = self.calculate_overall_accuracy()
        if accuracy > 0:
            trend = self.get_accuracy_trend()
            progress_lines.append("")
            progress_lines.append(f"📊 Analytics: {accuracy:.1f}% accuracy | {trend}")
        
        self.progress_text.insert('1.0', '\n'.join(progress_lines))
        self.progress_text.config(state='disabled')

    def load_next_question(self):
        # Stop any running timer
        self.timer_running = False
        
        # Clear result display
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        if self.review_mode:
            # Review mode: use bookmarked questions
            if not self.review_questions:
                messagebox.showinfo("Review Complete", 
                                  "You've reviewed all your bookmarked questions!\n"
                                  "Turn off Review Mode to continue with regular questions.")
                return
            
            # Get next review question
            if not hasattr(self, 'review_index'):
                self.review_index = 0
            
            if self.review_index >= len(self.review_questions):
                messagebox.showinfo("Review Complete", 
                                  "You've completed reviewing all bookmarked questions!\n"
                                  "Starting over or turn off Review Mode.")
                self.review_index = 0
            
            self.current_question = self.review_questions[self.review_index]
            self.review_index += 1
            
            # Update bookmark count for reviewed question
            question_id = self.generate_question_id()
            for bookmark in self.bookmarked_questions:
                if bookmark.get('question_id') == question_id:
                    bookmark['review_count'] = bookmark.get('review_count', 0) + 1
                    bookmark['last_reviewed'] = datetime.now().isoformat()
                    break
        
        else:
            # Regular mode: normal question flow
            level_questions = [q for q in self.questions if q['level'] == self.current_level]
            
            # Check if level is completed
            if len(self.used_questions[self.current_level]) >= 15:
                self.level_scores[self.current_level]['completed'] = True
                self.update_level_buttons()
                self.update_progress_display()
                self.auto_save_progress()
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
        
        # Update bookmark button
        self.update_bookmark_button()
        
        # Start timer for new question
        self.start_question_timer()

    def display_question(self):
        # Clear previous question
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        
        # Add review mode indicator if active
        if self.review_mode:
            review_label = tk.Label(self.question_frame,
                                  text="📚 REVIEW MODE - Practicing Bookmarked Question",
                                  font=('Arial', 10, 'bold'),
                                  bg='#e3f2fd',
                                  fg='#1976d2',
                                  relief='raised',
                                  bd=1)
            review_label.pack(fill='x', padx=5, pady=5)
        
        # Get question type and create appropriate interface
        question_type = self.current_question['type']
        if question_type in self.question_handlers:
            self.question_handlers[question_type]()
        else:
            self.create_multiple_choice()  # Default fallback

    def process_answer(self):
        """Process the answer and show result - Enhanced with analytics"""
        if self.answer_submitted:
            return
        
        self.answer_submitted = True
        
        # Stop timer and record timing
        self.timer_running = False
        self.record_question_timing()
        
        is_correct = self.check_answer()
        correct_answer = self.get_correct_answer()
        
        # Record analytics data
        self.record_analytics_data(is_correct)
        
        # Only update scores in regular mode (not review mode)
        if not self.review_mode:
            if is_correct:
                self.level_scores[self.current_level]['correct'] += 1
            else:
                self.level_scores[self.current_level]['incorrect'] += 1
            
            # Update displays
            self.update_progress_display()
        
        # AUTO-SAVE after each answer
        self.auto_save_progress()
        
        # Show result with timing feedback
        self.show_result(is_correct, correct_answer if not is_correct else None)

    def show_result(self, is_correct, correct_answer=None):
        # Clear previous result
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        # Get timing feedback
        time_feedback = ""
        if self.question_start_time and self.timer_enabled:
            time_taken = time.time() - self.question_start_time
            if time_taken < 15:
                time_feedback = " ⚡ Lightning fast!"
            elif time_taken < 30:
                time_feedback = " 🚀 Quick thinking!"
            elif time_taken > 60:
                time_feedback = " 🤔 Took your time!"
        
        # Add review mode feedback
        review_feedback = ""
        if self.review_mode:
            review_feedback = " 📚 (Review Mode)"
        
        if is_correct:
            result_label = tk.Label(self.result_frame,
                                   text=f"✅ Correct! Well done!{time_feedback}{review_feedback}",
                                   font=('Arial', 12, 'bold'),
                                   bg='#e8f5e8',
                                   fg='#2e7d32',
                                   relief='raised',
                                   bd=2)
        else:
            result_text = "❌ Incorrect."
            if correct_answer:
                result_text += f" The correct answer is: {correct_answer}"
            result_text += time_feedback + review_feedback
            
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

    def skip_question(self):
        """Skip current question and move to next - Enhanced with analytics"""
        # Stop timer and record timing
        self.timer_running = False
        self.record_question_timing()
        
        # Record analytics for skip (incorrect)
        self.record_analytics_data(False)
        
        # Only count as incorrect in regular mode
        if not self.review_mode:
            self.level_scores[self.current_level]['incorrect'] += 1
            self.update_progress_display()
        
        # AUTO-SAVE after skip
        self.auto_save_progress()
        
        # Show skip message briefly then move to next
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        skip_text = "⏭ Question Skipped"
        if self.review_mode:
            skip_text += " (Review Mode)"
        
        skip_label = tk.Label(self.result_frame,
                             text=skip_text,
                             font=('Arial', 12, 'bold'),
                             bg='#fff3e0',
                             fg='#f57c00',
                             relief='raised',
                             bd=2)
        skip_label.pack(fill='x', pady=5)
        
        # Move to next question after 1 second
        self.window.after(1000, self.load_next_question)

    def close(self):
        """Enhanced close method with comprehensive summary including analytics"""
        # Stop timer
        self.timer_running = False
        
        if self.window and self.window.winfo_exists():
            # Calculate final stats
            speed_stats = self.calculate_speed_stats()
            accuracy = self.calculate_overall_accuracy()
            
            # Final save with backup
            try:
                self.auto_save_progress()
                
                # Show enhanced completion message with analytics
                completion_msg = f"Your progress has been saved!\nTotal saves this session: {self.auto_save_count}"
                
                # Add analytics summary
                if accuracy > 0:
                    completion_msg += f"\n\n📊 Session Analytics:"
                    completion_msg += f"\n• Overall accuracy: {accuracy:.1f}%"
                    
                    # Bloom's taxonomy breakdown
                    blooms_data = self.detailed_analytics['blooms_performance']
                    best_level = max(blooms_data.items(), 
                                   key=lambda x: (x[1]['correct']/(x[1]['correct']+x[1]['incorrect'])) if (x[1]['correct']+x[1]['incorrect']) > 0 else 0)
                    if best_level[1]['correct'] + best_level[1]['incorrect'] > 0:
                        best_accuracy = (best_level[1]['correct']/(best_level[1]['correct']+best_level[1]['incorrect']))*100
                        completion_msg += f"\n• Best difficulty level: Level {best_level[0]} ({best_accuracy:.1f}%)"
                
                if speed_stats and speed_stats['total_questions'] > 0:
                    completion_msg += f"\n\n⏱️ Timing Summary:"
                    completion_msg += f"\n• Questions answered: {speed_stats['total_questions']}"
                    completion_msg += f"\n• Average time: {speed_stats['average_time']} seconds"
                    completion_msg += f"\n• Fastest answer: {speed_stats['fastest_time']} seconds"
                    if speed_stats['timeout_count'] > 0:
                        completion_msg += f"\n• Timeouts: {speed_stats['timeout_count']}"
                
                if self.bookmarked_questions:
                    completion_msg += f"\n\n🔖 Bookmarks:"
                    completion_msg += f"\n• Total bookmarked: {len(self.bookmarked_questions)}"
                    completion_msg += f"\n• Available for review anytime!"
                
                # Add study recommendations
                recommendations = self.generate_study_recommendations()
                if recommendations:
                    top_rec = recommendations[0]
                    completion_msg += f"\n\n💡 Top Recommendation:"
                    completion_msg += f"\n{top_rec['text'][:100]}..."
                
                messagebox.showinfo("Quiz Complete", completion_msg)
                
            except Exception as e:
                messagebox.showerror("Save Error", 
                                   f"Error saving progress: {e}\n"
                                   f"Your progress may not be fully saved.")
            
            self.window.destroy()

    # ===== QUESTION TYPE HANDLERS (Existing methods) =====

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
        
        # Question text
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Entry field
        entry_frame = tk.Frame(self.question_frame, bg='white')
        entry_frame.pack(anchor='w', padx=20, pady=10)
        
        tk.Label(entry_frame, text="Answer:", font=('Arial', 10), bg='white').pack(side='left')
        
        self.missing_word_entry = tk.Entry(entry_frame, font=('Arial', 10), width=30)
        self.missing_word_entry.pack(side='left', padx=5)
        self.missing_word_entry.bind('<Return>', lambda e: self.process_answer())
        
        # Submit button
        submit_btn = tk.Button(entry_frame, text="Submit", 
                              command=self.process_answer,
                              bg='#4CAF50', fg='white')
        submit_btn.pack(side='left', padx=5)

    def create_syntax_error(self):
        question_text = self.current_question['question']
        code = self.current_question.get('code', '')
        
        # Question text
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Code display
        if code:
            code_frame = tk.Frame(self.question_frame, bg='#f8f8f8', relief='sunken', bd=1)
            code_frame.pack(fill='x', padx=20, pady=5)
            
            code_label = tk.Label(code_frame, text=code, font=('Courier', 9),
                                 bg='#f8f8f8', justify='left')
            code_label.pack(anchor='w', padx=5, pady=5)
        
        # Entry field
        entry_frame = tk.Frame(self.question_frame, bg='white')
        entry_frame.pack(anchor='w', padx=20, pady=10)
        
        tk.Label(entry_frame, text="Fix:", font=('Arial', 10), bg='white').pack(side='left')
        
        self.syntax_error_entry = tk.Entry(entry_frame, font=('Arial', 10), width=40)
        self.syntax_error_entry.pack(side='left', padx=5)
        self.syntax_error_entry.bind('<Return>', lambda e: self.process_answer())
        
        # Submit button
        submit_btn = tk.Button(entry_frame, text="Submit", 
                              command=self.process_answer,
                              bg='#4CAF50', fg='white')
        submit_btn.pack(side='left', padx=5)

    def create_one_word(self):
        question_text = self.current_question['question']
        
        # Question text
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Entry field
        entry_frame = tk.Frame(self.question_frame, bg='white')
        entry_frame.pack(anchor='w', padx=20, pady=10)
        
        tk.Label(entry_frame, text="Answer:", font=('Arial', 10), bg='white').pack(side='left')
        
        self.one_word_entry = tk.Entry(entry_frame, font=('Arial', 10), width=20)
        self.one_word_entry.pack(side='left', padx=5)
        self.one_word_entry.bind('<Return>', lambda e: self.process_answer())
        
        # Submit button
        submit_btn = tk.Button(entry_frame, text="Submit", 
                              command=self.process_answer,
                              bg='#4CAF50', fg='white')
        submit_btn.pack(side='left', padx=5)

    def create_mix_match(self):
        question_text = self.current_question['question']
        options = self.current_question['options']
        
        # Question text
        q_label = tk.Label(self.question_frame, text=question_text,
                          font=('Arial', 11), bg='white', wraplength=750,
                          justify='left')
        q_label.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Mix and match interface
        match_frame = tk.Frame(self.question_frame, bg='white')
        match_frame.pack(fill='x', padx=20, pady=10)
        
        self.match_vars = {}
        
        for i, option in enumerate(options):
            row_frame = tk.Frame(match_frame, bg='white')
            row_frame.pack(fill='x', pady=2)
            
            tk.Label(row_frame, text=f"{i+1}. {option}", 
                    font=('Arial', 10), bg='white', width=30, anchor='w').pack(side='left')
            
            var = tk.StringVar()
            self.match_vars[i] = var
            
            combo = ttk.Combobox(row_frame, textvariable=var, width=15, state='readonly')
            combo['values'] = ['A', 'B', 'C', 'D', 'E'][:len(options)]
            combo.pack(side='left', padx=10)
            combo.bind('<<ComboboxSelected>>', lambda e: self.check_mix_match_complete())

    def check_mix_match_complete(self):
        """Check if all mix-match selections are complete, then auto-submit"""
        if not self.answer_submitted:
            # Check if all combos have selections
            all_selected = all(var.get() for var in self.match_vars.values())
            if all_selected:
                self.process_answer()

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

    def get_questions(self):
        # This method should be overridden by specific quiz modules
        return []