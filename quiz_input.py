# =================================Input Function Quiz Module==================================
# quiz_input.py - Comprehensive input() function quiz with 75 questions across 5 Bloom's levels
from quiz_base import QuizBase

class QuizInput(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "input", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - KNOWLEDGE/REMEMBER (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is the basic function used to get user input in Python?',
                'options': ['get()', 'read()', 'input()', 'scan()'],
                'correct_answer': 'input()'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What data type does input() always return?',
                'options': ['Integer', 'String', 'Float', 'Boolean'],
                'correct_answer': 'String'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What function converts string input to an integer?',
                'correct_answer': 'int'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which is the correct syntax for input with a prompt?',
                'options': ['input("Enter name: ")', 'input["Enter name: "]', 'input{Enter name: }', 'input<Enter name: >'],
                'correct_answer': 'input("Enter name: ")'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'input() waits for the user to press the _____ key.',
                'correct_answer': ['Enter', 'return']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What happens when you call input() without arguments?',
                'options': ['Error occurs', 'Returns empty string', 'Waits for user input', 'Returns None'],
                'correct_answer': 'Waits for user input'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What function converts string input to a floating-point number?',
                'correct_answer': 'float'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Where does the input() prompt message appear?',
                'options': ['On a new line', 'At the cursor position', 'At the top of screen', 'In a dialog box'],
                'correct_answer': 'At the cursor position'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To store user input in a variable: name = _____("Enter your name: ")',
                'correct_answer': ['input']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does input("Age: ") do?',
                'options': ['Displays "Age: " and waits for input', 'Returns "Age: "', 'Sets age to a value', 'Creates an age variable'],
                'correct_answer': 'Displays "Age: " and waits for input'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What character is typically used at the end of input prompts?',
                'correct_answer': 'colon'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which statement about input() is true?',
                'options': ['It can only read numbers', 'It automatically converts types', 'It always returns strings', 'It requires a prompt'],
                'correct_answer': 'It always returns strings'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'input() reads user input from the _____ device.',
                'correct_answer': ['keyboard', 'console', 'stdin']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What happens to the newline character when using input()?',
                'options': ['It is included in the result', 'It is automatically removed', 'It causes an error', 'It is converted to space'],
                'correct_answer': 'It is automatically removed'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What method removes leading and trailing whitespace from input?',
                'correct_answer': 'strip'
            },

            # LEVEL 2 - COMPREHENSION/UNDERSTAND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this code do?',
                'code': 'name = input("Enter your name: ")\nprint("Hello", name)',
                'options': ['Display prompt, wait for input, greet user', 'Display only the prompt', 'Print "Hello name"', 'Cause an error'],
                'correct_answer': 'Display prompt, wait for input, greet user'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why do you need int() when getting numeric input?',
                'options': ['input() returns strings', 'For better performance', 'To avoid errors', 'For memory efficiency'],
                'correct_answer': 'input() returns strings'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'age = int(input("Age: ")) converts the input string to an _____.',
                'correct_answer': ['integer', 'int', 'number']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What type of data does this variable contain?',
                'code': 'user_input = input("Enter a number: ")',
                'options': ['Integer', 'String', 'Float', 'Number'],
                'correct_answer': 'String'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the difference between input("5") and the number 5?',
                'options': ['No difference', 'input("5") shows prompt, 5 is a number', 'input("5") is faster', 'input("5") saves memory'],
                'correct_answer': 'input("5") shows prompt, 5 is a number'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What happens if user enters "hello" here?',
                'code': 'number = int(input("Enter number: "))',
                'options': ['Stores "hello"', 'Converts to 0', 'Causes ValueError', 'Works normally'],
                'correct_answer': 'Causes ValueError'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'input()._____ removes extra spaces from user input.',
                'correct_answer': ['strip']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why might you use input().lower()?',
                'options': ['To reduce file size', 'For case-insensitive comparison', 'To improve speed', 'To fix errors'],
                'correct_answer': 'For case-insensitive comparison'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this accomplish?',
                'code': 'response = input("Continue? (y/n): ").lower()',
                'options': ['Gets yes/no input in lowercase', 'Validates the input', 'Converts to boolean', 'Checks for errors'],
                'correct_answer': 'Gets yes/no input in lowercase'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is input validation?',
                'options': ['Converting input types', 'Checking if input meets requirements', 'Storing input safely', 'Displaying input prompts'],
                'correct_answer': 'Checking if input meets requirements'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'float(input()) converts string input to a _____ number.',
                'correct_answer': ['floating-point', 'decimal', 'float']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this print if user enters "  Bob  "?',
                'code': 'name = input("Name: ").strip()\nprint(f"Hello {name}!")',
                'options': ['Hello   Bob  !', 'Hello Bob!', 'Hello Bob', 'Error'],
                'correct_answer': 'Hello Bob!'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does input() return when user just presses Enter?',
                'options': ['None', 'Empty string ""', 'Single space " "', 'Error'],
                'correct_answer': 'Empty string ""'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'To check if input is numeric, use the _____ method.',
                'correct_answer': ['isdigit', 'isnumeric']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this code pattern accomplish?',
                'code': 'while True:\n    user_input = input("Enter command: ")\n    if user_input == "quit":\n        break',
                'options': ['Single input request', 'Continuous input loop', 'Input validation', 'Error handling'],
                'correct_answer': 'Continuous input loop'
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this input statement:',
                'code': 'age = input("Enter age: ") + 5',
                'correct_answer': ['int(input("Enter age: ")) + 5', 'convert to int', 'use int()']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this input validation do?',
                'code': 'while True:\n    age = input("Age: ")\n    if age.isdigit():\n        break\n    print("Please enter a number")',
                'options': ['Ensures numeric input', 'Checks for positive numbers', 'Validates age range', 'Converts to integer'],
                'correct_answer': 'Ensures numeric input'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To get multiple inputs on one line: name, age = input()._____(",")',
                'correct_answer': ['split']
            },
            {
                'level': 3,
                'type': 'mix_match',
                'question': 'Match input methods with their purposes:',
                'left_items': ['input().strip()', 'input().lower()', 'int(input())', 'input().split()'],
                'right_items': ['Convert to integer', 'Remove whitespace', 'Make lowercase', 'Split into list'],
                'correct_answer': {0: 'Remove whitespace', 1: 'Make lowercase', 2: 'Convert to integer', 3: 'Split into list'}
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this create?',
                'code': 'numbers = []\nfor i in range(3):\n    num = int(input(f"Enter number {i+1}: "))\n    numbers.append(num)',
                'options': ['List of 3 integers from user', 'Single number input', 'Range of numbers', 'Validation loop'],
                'correct_answer': 'List of 3 integers from user'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this yes/no input check:',
                'code': 'answer = input("Continue? (y/n): ")\nif answer == "Y" or "y":\n    continue',
                'correct_answer': ['answer.lower() == "y"', 'answer in ["y", "Y"]', 'proper comparison']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this password input pattern do?',
                'code': 'import getpass\npassword = getpass.getpass("Password: ")',
                'options': ['Hides password while typing', 'Validates password strength', 'Encrypts the password', 'Stores password securely'],
                'correct_answer': 'Hides password while typing'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To handle input errors: try: int(input()) except _____: print("Invalid")',
                'correct_answer': ['ValueError']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How do you get integer input with error handling?',
                'options': ['int(input()) only', 'Use try/except with int(input())', 'Use isdigit() only', 'Use float(input())'],
                'correct_answer': 'Use try/except with int(input())'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this menu system create?',
                'code': 'while True:\n    print("1. Add\\n2. Delete\\n3. Quit")\n    choice = input("Choose: ")\n    if choice == "3":\n        break',
                'options': ['Simple menu loop', 'Input validation', 'Error handling', 'Data processing'],
                'correct_answer': 'Simple menu loop'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this input range validation:',
                'code': 'score = int(input("Score (0-100): "))\nif score < 0 and score > 100:\n    print("Invalid range")',
                'correct_answer': ['or instead of and', 'score < 0 or score > 100']
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To check if input is empty: if not input()._____()',
                'correct_answer': ['strip']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this input processing do?',
                'code': 'text = input("Enter words: ")\nwords = text.split()\nprint(f"You entered {len(words)} words")',
                'options': ['Counts characters', 'Counts words in input', 'Validates text format', 'Processes sentences'],
                'correct_answer': 'Counts words in input'
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How do you create a default value for input?',
                'options': ['input(default="value")', 'input() or "default"', 'Use if statement after input', 'Cannot set defaults'],
                'correct_answer': 'Use if statement after input'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What validation does this perform?',
                'code': 'email = input("Email: ")\nif "@" in email and "." in email:\n    print("Valid format")',
                'options': ['Email format validation', 'Domain checking', 'Character counting', 'Input sanitization'],
                'correct_answer': 'Email format validation'
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What security issue does this demonstrate?',
                'code': 'filename = input("Enter filename: ")\nwith open(filename, "r") as f:\n    content = f.read()',
                'options': ['Path traversal vulnerability', 'Memory leak', 'Type conversion error', 'Invalid syntax'],
                'correct_answer': 'Path traversal vulnerability'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why is input validation critical in production applications?',
                'options': ['Performance optimization', 'Security and data integrity', 'Memory management', 'Code readability'],
                'correct_answer': 'Security and data integrity'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What problem does this input handling have?',
                'code': 'while True:\n    try:\n        age = int(input("Age: "))\n        break\n    except:\n        pass',
                'options': ['No user feedback on errors', 'Infinite loop risk', 'Poor exception handling', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Input _____ attacks involve malicious data designed to exploit vulnerabilities.',
                'correct_answer': ['injection']
            },
            {
                'level': 4,
                'type': 'mix_match',
                'question': 'Match input security concepts:',
                'left_items': ['Sanitization', 'Validation', 'Encoding', 'Escaping'],
                'right_items': ['Check format/range', 'Clean malicious content', 'Convert special chars', 'Handle dangerous chars'],
                'correct_answer': {0: 'Clean malicious content', 1: 'Check format/range', 2: 'Convert special chars', 3: 'Handle dangerous chars'}
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What input validation principle does this violate?',
                'code': 'data = input("Enter data: ")\neval(data)',
                'options': ['Never trust user input', 'Always validate types', 'Use proper encoding', 'Limit input length'],
                'correct_answer': 'Never trust user input'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the main difference between client-side and server-side input validation?',
                'options': ['Speed vs accuracy', 'Security vs convenience', 'Local vs remote processing', 'User experience vs security'],
                'correct_answer': 'User experience vs security'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the logical flaw in this validation:',
                'code': 'password = input("Password: ")\nif len(password) > 8:\n    print("Password too long")\nelif len(password) < 8:\n    print("Password too short")',
                'correct_answer': ['missing exactly 8 case', 'no case for length 8', 'incomplete logic']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue might this cause?',
                'code': 'while True:\n    large_input = input("Enter data: ")\n    if len(large_input) > 1000000:\n        continue',
                'options': ['Memory exhaustion', 'CPU overload', 'Infinite loop', 'File system stress'],
                'correct_answer': 'Memory exhaustion'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Input _____ involves restricting what characters or patterns are allowed.',
                'correct_answer': ['filtering', 'sanitization']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Which input validation approach is most secure?',
                'options': ['Blacklist forbidden inputs', 'Whitelist allowed inputs', 'Trust user input', 'Convert all to strings'],
                'correct_answer': 'Whitelist allowed inputs'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What usability principle does this violate?',
                'code': 'while True:\n    num = input("Enter number between 1-100: ")\n    if not num.isdigit() or int(num) < 1 or int(num) > 100:\n        print("ERROR")\n        continue',
                'options': ['Clear error messages', 'User guidance', 'Input format hints', 'Error recovery'],
                'correct_answer': 'Clear error messages'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Input _____ testing involves trying unexpected inputs to find vulnerabilities.',
                'correct_answer': ['fuzzing', 'stress']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why should you limit input length in applications?',
                'options': ['Improve performance', 'Prevent buffer overflow attacks', 'Save memory', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What race condition issue might this have?',
                'code': 'import threading\ndef get_input():\n    global user_data\n    user_data = input("Enter data: ")',
                'options': ['Multiple threads accessing input', 'Shared variable conflicts', 'Input buffer corruption', 'Synchronization issues'],
                'correct_answer': 'Shared variable conflicts'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced input system does this create?',
                'code': 'class InputValidator:\n    def __init__(self, input_type, min_val=None, max_val=None):\n        self.type = input_type\n        self.min = min_val\n        self.max = max_val\n    \n    def get_input(self, prompt):\n        while True:\n            try:\n                value = self.type(input(prompt))\n                if self.min is not None and value < self.min:\n                    continue\n                if self.max is not None and value > self.max:\n                    continue\n                return value\n            except ValueError:\n                print("Invalid input type")',
                'options': ['Generic input validator class', 'Type conversion system', 'Error handling framework', 'User interface builder'],
                'correct_answer': 'Generic input validator class'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a robust command-line interface, you would combine:',
                'options': ['input() and print() only', 'input(), validation, help system, and error handling', 'Basic input with file I/O', 'Simple menu loops'],
                'correct_answer': 'input(), validation, help system, and error handling'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A sophisticated input system would implement _____ to remember user preferences.',
                'correct_answer': ['persistence', 'storage', 'memory']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What design pattern does this input system implement?',
                'code': 'class InputCommand:\n    def execute(self, data): pass\n\nclass SaveCommand(InputCommand):\n    def execute(self, data):\n        save_file(data)\n\nclass PrintCommand(InputCommand):\n    def execute(self, data):\n        print(data)\n\ncommands = {"save": SaveCommand(), "print": PrintCommand()}\nuser_input = input("Command: ")\ncommands[user_input].execute(data)',
                'options': ['Command pattern', 'Observer pattern', 'Factory pattern', 'Strategy pattern'],
                'correct_answer': 'Command pattern'
            },
            {
                'level': 5,
                'type': 'mix_match',
                'question': 'Match advanced input techniques with their applications:',
                'left_items': ['Auto-completion', 'Input history', 'Masked input', 'Real-time validation'],
                'right_items': ['Password fields', 'Form validation', 'Command recall', 'IDE features'],
                'correct_answer': {0: 'IDE features', 1: 'Command recall', 2: 'Password fields', 3: 'Form validation'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What input processing architecture does this represent?',
                'code': 'class InputProcessor:\n    def __init__(self):\n        self.filters = []\n        self.validators = []\n    \n    def add_filter(self, filter_func):\n        self.filters.append(filter_func)\n    \n    def process(self, raw_input):\n        data = raw_input\n        for filter_func in self.filters:\n            data = filter_func(data)\n        return data',
                'options': ['Pipeline processing', 'Event-driven system', 'State machine', 'Observer pattern'],
                'correct_answer': 'Pipeline processing'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a natural language input processor, you would primarily need:',
                'options': ['Regular expressions and parsing', 'Machine learning and NLP libraries', 'Database connections', 'Web frameworks'],
                'correct_answer': 'Machine learning and NLP libraries'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'To create input auto-completion, you would implement a _____ data structure.',
                'correct_answer': ['trie', 'tree', 'prefix tree']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What input management system does this create?',
                'code': 'class InputManager:\n    def __init__(self):\n        self.history = []\n        self.current_pos = 0\n    \n    def get_input_with_history(self, prompt):\n        # Implementation for arrow key navigation\n        pass\n    \n    def add_to_history(self, command):\n        self.history.append(command)',
                'options': ['Command history system', 'Input validation system', 'Error logging system', 'User preference system'],
                'correct_answer': 'Command history system'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For building a secure web form input system, you would implement:',
                'options': ['CSRF protection, input sanitization, and validation', 'Only client-side validation', 'Basic HTML forms', 'Simple input() calls'],
                'correct_answer': 'CSRF protection, input sanitization, and validation'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this input rate limiting system:',
                'code': 'import time\nclass RateLimiter:\n    def __init__(self, max_attempts, window):\n        self.max_attempts = max_attempts\n        self.window = window\n        self.attempts = []\n    \n    def allow_input(self):\n        now = time.time()\n        # Remove old attempts\n        self.attempts = [t for t in self.attempts if now - t < self.window]\n        if len(self.attempts) _____ self.max_attempts:\n            return False\n        self.attempts.append(now)\n        return True',
                'correct_answer': ['>=', 'greater than or equal']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What input security framework does this implement?',
                'code': 'class SecureInput:\n    def __init__(self):\n        self.sanitizers = []\n        self.validators = []\n        self.rate_limiter = RateLimiter()\n    \n    def process_input(self, raw_input):\n        if not self.rate_limiter.check():\n            raise SecurityError("Rate limit exceeded")\n        \n        clean_input = self.sanitize(raw_input)\n        if not self.validate(clean_input):\n            raise ValidationError("Invalid input")\n        \n        return clean_input',
                'options': ['Comprehensive input security system', 'Simple validation wrapper', 'Error handling system', 'Performance monitoring'],
                'correct_answer': 'Comprehensive input security system'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A machine learning input system would use _____ to predict user intentions.',
                'correct_answer': ['algorithms', 'models', 'classification']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create an intelligent chatbot input processor, you would combine:',
                'options': ['NLP, intent recognition, and context management', 'Simple string matching', 'Basic input validation', 'Regular expressions only'],
                'correct_answer': 'NLP, intent recognition, and context management'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What adaptive system does this represent?',
                'code': 'class AdaptiveInput:\n    def __init__(self):\n        self.user_patterns = {}\n        self.suggestions = []\n    \n    def learn_from_input(self, user_id, input_data):\n        if user_id not in self.user_patterns:\n            self.user_patterns[user_id] = []\n        self.user_patterns[user_id].append(input_data)\n        self.update_suggestions(user_id)\n    \n    def get_suggestions(self, user_id, partial_input):\n        # Generate suggestions based on learned patterns\n        pass',
                'options': ['Machine learning input system', 'User preference tracker', 'Input validation system', 'Performance monitor'],
                'correct_answer': 'Machine learning input system'
            }
        ]