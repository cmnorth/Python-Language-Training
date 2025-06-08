# =================================Version 02==================================
# app_config.py - Shared configuration and constants
"""
Application configuration and constants
"""

# Window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 700  # Updated for expanded login window

# Colors
COLORS = {
    'primary': '#4CAF50',
    'secondary': '#2196F3',
    'warning': '#FF9800',
    'danger': '#f44336',
    'logout': '#9C27B0',
    'background': 'white',
    'text': 'black'
}

# Fonts
FONTS = {
    'title': ('Arial', 16, 'bold'),
    'subtitle': ('Arial', 14, 'bold'),
    'normal': ('Arial', 11),
    'small': ('Arial', 10)
}

# Demo commands list
DEMO_COMMANDS = [
    'str - Strings and text data',
    'print() - Display output',
    'input() - Get user input', 
    'len() - Get length',
    'type() - Check data type',
    'range() - Create number sequence',
    'list() - Create list',
    'dict() - Create dictionary',
    'for loop - Iterate over items',
    'if statement - Conditional logic',
    'def - Define function'
]

# Quiz list
AVAILABLE_QUIZZES = [
    "Basic Python Syntax Quiz",
    "Data Types and Variables Quiz", 
    "Control Structures Quiz",
    "Functions and Modules Quiz"
]