# error_handler.py
import logging
import traceback
from tkinter import messagebox

class ErrorHandler:
    def __init__(self):
        logging.basicConfig(
            filename='app_errors.log',
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def handle_error(self, error, context="Unknown"):
        logging.error(f"Error in {context}: {str(error)}")
        logging.error(traceback.format_exc())
        
        messagebox.showerror(
            "Error", 
            f"An error occurred: {str(error)}\n\nPlease check the log file for details."
        )