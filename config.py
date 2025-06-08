# config.py
class Config:
    # Window dimensions
    MAIN_WINDOW_WIDTH = 450
    MAIN_WINDOW_HEIGHT = 700
    DEMO_WINDOW_WIDTH = 600
    
    # Database settings
    DATABASE_FILE = "student_data.db"
    
    # Quiz settings
    QUESTIONS_PER_LEVEL = 15
    AUTO_ADVANCE_DELAY = 2000  # milliseconds
    
    # File paths
    PROGRESS_DIR = "user_progress"
    BACKUP_DIR = "backups"