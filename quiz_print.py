# =================================Print Function Quiz Module==================================
# quiz_print.py - Comprehensive print() function quiz with 75 questions across 5 Bloom's levels
from quiz_base import QuizBase

class QuizPrint(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "print", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - KNOWLEDGE/REMEMBER (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is the basic function used to display output in Python?',
                'options': ['output()', 'display()', 'print()', 'show()'],
                'correct_answer': 'print()'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does print("Hello") display?',
                'options': ['Hello', '"Hello"', 'print("Hello")', 'Error'],
                'correct_answer': 'Hello'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What character automatically appears at the end of print() output?',
                'correct_answer': 'newline'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which of these is the correct syntax for print?',
                'options': ['print "Hello"', 'print("Hello")', 'Print("Hello")', 'PRINT("Hello")'],
                'correct_answer': 'print("Hello")'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'print() is a built-in _____ in Python.',
                'correct_answer': ['function']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What separates multiple items in print() by default?',
                'options': ['Comma', 'Space', 'Tab', 'Nothing'],
                'correct_answer': 'Space'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What parameter controls what appears between print() arguments?',
                'correct_answer': 'sep'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does print() return?',
                'options': ['The printed text', 'True', 'None', '0'],
                'correct_answer': 'None'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'print() sends output to _____ by default.',
                'correct_answer': ['stdout', 'console', 'screen']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which parameter controls what appears at the end of print() output?',
                'options': ['sep', 'end', 'finish', 'close'],
                'correct_answer': 'end'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What is the default value of the end parameter?',
                'correct_answer': 'newline'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What happens when you call print() with no arguments?',
                'options': ['Error', 'Prints "None"', 'Prints empty line', 'Does nothing'],
                'correct_answer': 'Prints empty line'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To print multiple values, separate them with _____.',
                'correct_answer': ['commas', 'comma']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which of these prints a variable correctly?',
                'options': ['print(variable)', 'print("variable")', 'print[variable]', 'print{variable}'],
                'correct_answer': 'print(variable)'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What type of quotes can surround strings in print()?',
                'correct_answer': ['both']
            },

            # LEVEL 2 - COMPREHENSION/UNDERSTAND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this code output?',
                'code': 'print("Hello", "World")',
                'options': ['HelloWorld', 'Hello World', 'Hello,World', 'Hello\nWorld'],
                'correct_answer': 'Hello World'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why would you use print() in debugging?',
                'options': ['To fix errors', 'To see variable values', 'To speed up code', 'To save memory'],
                'correct_answer': 'To see variable values'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this print?',
                'code': 'name = "Alice"\nage = 25\nprint("Name:", name, "Age:", age)',
                'options': ['Name: Alice Age: 25', 'Name:Alice Age:25', 'NameAliceAge25', 'Error'],
                'correct_answer': 'Name: Alice Age: 25'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'print(1, 2, 3, sep="-") will output: 1_____2_____3',
                'correct_answer': ['-']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What happens here?',
                'code': 'print("Hello", end="")\nprint("World")',
                'options': ['Hello World', 'HelloWorld', 'Hello\nWorld', 'Error'],
                'correct_answer': 'HelloWorld'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the difference between print(5) and print("5")?',
                'options': ['No difference', 'First prints integer, second prints string', 'First is faster', 'Second causes error'],
                'correct_answer': 'First prints integer, second prints string'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this display?',
                'code': 'result = 10 + 5\nprint("Result:", result)',
                'options': ['Result: 10 + 5', 'Result: 15', 'Result:15', 'Error'],
                'correct_answer': 'Result: 15'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'To print without a newline at the end, use print("text", end="_____")',
                'correct_answer': ['""', 'empty string']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does print(f"Hello {name}") demonstrate?',
                'options': ['Regular print', 'F-string formatting', 'Error syntax', 'Variable concatenation'],
                'correct_answer': 'F-string formatting'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What is the output?',
                'code': 'print("Line 1")\nprint()\nprint("Line 3")',
                'options': ['Line 1\n\nLine 3', 'Line 1Line 3', 'Line 1\nLine 3', 'Error'],
                'correct_answer': 'Line 1\n\nLine 3'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why might you use print(*items)?',
                'options': ['To print a list as separate items', 'To print faster', 'To save memory', 'To avoid errors'],
                'correct_answer': 'To print a list as separate items'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this show?',
                'code': 'items = ["a", "b", "c"]\nprint(*items)',
                'options': ['["a", "b", "c"]', 'a b c', 'abc', 'Error'],
                'correct_answer': 'a b c'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'print("Hello\\nWorld") will display Hello and World on _____ lines.',
                'correct_answer': ['separate', 'different']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does the file parameter in print() control?',
                'options': ['Input source', 'Output destination', 'File name', 'Print speed'],
                'correct_answer': 'Output destination'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What is displayed?',
                'code': 'print("Value:", 42, "Type:", type(42).__name__)',
                'options': ['Value: 42 Type: int', 'Value:42Type:int', 'Error', 'Value: 42 Type: integer'],
                'correct_answer': 'Value: 42 Type: int'
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this print statement:',
                'code': 'print("Hello World"',
                'correct_answer': ['missing parenthesis', 'add )', 'closing parenthesis']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'Create output "A-B-C" using this list:',
                'code': 'letters = ["A", "B", "C"]\nprint(*letters, sep="-")',
                'options': ['A-B-C', 'A B C', '["A", "B", "C"]', 'Error'],
                'correct_answer': 'A-B-C'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To print "Loading..." without newline: print("Loading...", end="_____")',
                'correct_answer': ['""', 'empty string']
            },
            {
                'level': 3,
                'type': 'mix_match',
                'question': 'Match print parameters with their functions:',
                'left_items': ['sep', 'end', 'file', 'flush'],
                'right_items': ['Force output immediately', 'Separator between items', 'End character', 'Output destination'],
                'correct_answer': {0: 'Separator between items', 1: 'End character', 2: 'Output destination', 3: 'Force output immediately'}
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What creates this output: "Score: 95/100"?',
                'code': 'score = 95\ntotal = 100\nprint(f"Score: {score}/{total}")',
                'options': ['Score: 95/100', 'Score: {score}/{total}', 'Error', 'Score: score/total'],
                'correct_answer': 'Score: 95/100'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this f-string print:',
                'code': 'name = "Bob"\nprint(f"Hello [name]")',
                'correct_answer': ['curly braces', 'use {}', '{name}']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'How do you print a dictionary nicely?',
                'code': 'data = {"a": 1, "b": 2}\nfor k, v in data.items():\n    print(f"{k}: {v}")',
                'options': ['a: 1\nb: 2', 'a:1\nb:2', '{"a": 1, "b": 2}', 'Error'],
                'correct_answer': 'a: 1\nb: 2'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To print to a file: print("text", file=_____)',
                'correct_answer': ['file_object', 'file handle', 'open file']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How do you print a progress bar effect?',
                'options': ['Use sep parameter', 'Use end="" and flush=True', 'Use file parameter', 'Not possible with print'],
                'correct_answer': 'Use end="" and flush=True'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What formats this as currency?',
                'code': 'price = 19.99\nprint(f"Price: ${price:.2f}")',
                'options': ['Price: $19.99', 'Price: $19.990', 'Price: ${price:.2f}', 'Error'],
                'correct_answer': 'Price: $19.99'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this multi-line print:',
                'code': 'print("Line 1"\n"Line 2")',
                'correct_answer': ['add comma', 'comma between strings', 'missing comma']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'How to print numbers 1-5 on one line?',
                'code': 'for i in range(1, 6):\n    print(i, end=" ")',
                'options': ['1 2 3 4 5 ', '12345', '1\n2\n3\n4\n5', 'Error'],
                'correct_answer': '1 2 3 4 5 '
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To center text in print: print("Hello"._____(20))',
                'correct_answer': ['center']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How do you print without buffering?',
                'options': ['flush=True', 'buffer=False', 'immediate=True', 'direct=True'],
                'correct_answer': 'flush=True'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What prints a table-like structure?',
                'code': 'print("Name".ljust(10), "Age".rjust(3))\nprint("Alice".ljust(10), "25".rjust(3))',
                'options': ['Name      Age\nAlice      25', 'Name Age\nAlice 25', 'NameAge\nAlice25', 'Error'],
                'correct_answer': 'Name      Age\nAlice      25'
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'Why might this cause performance issues?',
                'code': 'for i in range(10000):\n    print(f"Processing {i}")',
                'options': ['Too many print calls', 'F-string overhead', 'Loop inefficiency', 'Memory usage'],
                'correct_answer': 'Too many print calls'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the main difference between print() in Python 2 vs Python 3?',
                'options': ['Speed difference', 'Print is a statement vs function', 'Output format', 'Memory usage'],
                'correct_answer': 'Print is a statement vs function'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What security concern does this demonstrate?',
                'code': 'user_input = input("Enter data: ")\nprint(f"You entered: {user_input}")',
                'options': ['XSS vulnerability', 'Input injection', 'No security issue', 'Memory leak'],
                'correct_answer': 'No security issue'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Print buffering can be controlled by the _____ parameter for immediate output.',
                'correct_answer': ['flush']
            },
            {
                'level': 4,
                'type': 'mix_match',
                'question': 'Match output redirection concepts:',
                'left_items': ['sys.stdout', 'sys.stderr', 'file object', 'StringIO'],
                'right_items': ['Standard error', 'In-memory string', 'Standard output', 'File on disk'],
                'correct_answer': {0: 'Standard output', 1: 'Standard error', 2: 'File on disk', 3: 'In-memory string'}
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What principle does this logging approach demonstrate?',
                'code': 'import sys\nprint("Error occurred", file=sys.stderr)',
                'options': ['Error separation', 'Performance optimization', 'Memory management', 'Code organization'],
                'correct_answer': 'Error separation'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why might you redirect print() output to a file?',
                'options': ['Faster execution', 'Logging and persistence', 'Better formatting', 'Memory efficiency'],
                'correct_answer': 'Logging and persistence'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What threading issue might this cause?',
                'code': 'import threading\ndef worker():\n    for i in range(100):\n        print(f"Thread: {i}")',
                'options': ['Race condition in output', 'Deadlock', 'Memory corruption', 'No issues'],
                'correct_answer': 'Race condition in output'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'The _____ method can replace multiple print calls for better performance.',
                'correct_answer': ['join']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the overhead of f-strings compared to other formatting?',
                'options': ['Much slower', 'Slightly slower', 'About the same', 'Faster'],
                'correct_answer': 'Faster'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What encoding issue might this reveal?',
                'code': 'print("Hello 世界")',
                'options': ['UTF-8 encoding needed', 'ASCII limitation', 'Memory issue', 'No issues in Python 3'],
                'correct_answer': 'No issues in Python 3'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'When should you avoid using print() in production code?',
                'options': ['Never', 'For debugging output', 'For user interfaces', 'For file operations'],
                'correct_answer': 'For debugging output'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What design pattern does this represent?',
                'code': 'class Logger:\n    def __init__(self, file):\n        self.file = file\n    def log(self, msg):\n        print(msg, file=self.file)',
                'options': ['Adapter pattern', 'Observer pattern', 'Factory pattern', 'Singleton pattern'],
                'correct_answer': 'Adapter pattern'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Print statements in production should often be replaced with proper _____ systems.',
                'correct_answer': ['logging']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the impact of print() on program performance?',
                'options': ['No impact', 'I/O bound operations are slow', 'CPU intensive', 'Memory intensive'],
                'correct_answer': 'I/O bound operations are slow'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What does this progress bar implementation create?',
                'code': 'import time\nfor i in range(101):\n    print(f"\\rProgress: {i}%", end="", flush=True)\n    time.sleep(0.1)',
                'options': ['Real-time progress indicator', 'Static progress bar', 'Error message', 'Performance counter'],
                'correct_answer': 'Real-time progress indicator'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a custom print function with timestamp, you would:',
                'options': ['Modify print()', 'Create wrapper function', 'Use decorators only', 'Cannot be done'],
                'correct_answer': 'Create wrapper function'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'To create a table formatter, you would use string methods like _____ and _____.',
                'correct_answer': ['ljust', 'rjust']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What does this colored output system implement?',
                'code': 'class ColorPrint:\n    RED = "\\033[91m"\n    GREEN = "\\033[92m"\n    END = "\\033[0m"\n    \n    @classmethod\n    def red(cls, text):\n        print(f"{cls.RED}{text}{cls.END}")',
                'options': ['ANSI color codes for terminal', 'HTML color system', 'CSS styling', 'RGB color model'],
                'correct_answer': 'ANSI color codes for terminal'
            },
            {
                'level': 5,
                'type': 'mix_match',
                'question': 'Match advanced print techniques with their use cases:',
                'left_items': ['Context manager', 'Decorator pattern', 'Class method', 'Generator function'],
                'right_items': ['Lazy printing', 'Color printing', 'File redirection', 'Logging wrapper'],
                'correct_answer': {0: 'File redirection', 1: 'Logging wrapper', 2: 'Color printing', 3: 'Lazy printing'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What pattern does this multi-destination printer implement?',
                'code': 'class MultiPrint:\n    def __init__(self, *files):\n        self.files = files\n    \n    def print(self, *args, **kwargs):\n        for f in self.files:\n            print(*args, file=f, **kwargs)',
                'options': ['Observer pattern', 'Command pattern', 'Builder pattern', 'Proxy pattern'],
                'correct_answer': 'Observer pattern'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a print buffer that batches output, you would:',
                'options': ['Use threading', 'Collect strings and join', 'Modify sys.stdout', 'Use generators'],
                'correct_answer': 'Collect strings and join'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A context manager for print redirection would use _____ and _____ methods.',
                'correct_answer': ['__enter__', '__exit__']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What does this debugging print system create?',
                'code': 'import functools\n\ndef debug_print(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        print(f"Calling {func.__name__} with {args}, {kwargs}")\n        return func(*args, **kwargs)\n    return wrapper',
                'options': ['Function call tracer', 'Performance monitor', 'Error handler', 'Cache system'],
                'correct_answer': 'Function call tracer'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a print-based data visualization, you would primarily use:',
                'options': ['ASCII characters and spacing', 'Color codes only', 'Unicode symbols only', 'HTML formatting'],
                'correct_answer': 'ASCII characters and spacing'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What type of data structure does this create?',
                'code': 'def print_tree(node, level=0):\n    print("  " * level + str(node.value))\n    for child in node.children:\n        print_tree(child, level + 1)',
                'options': ['Visual tree representation', 'Linked list', 'Hash table', 'Binary search tree'],
                'correct_answer': 'Visual tree representation'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'To create animated console output, you would use _____ characters and time delays.',
                'correct_answer': ['escape', 'control']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'A sophisticated logging system would replace print() with:',
                'options': ['More print statements', 'Logging module with levels', 'File operations only', 'Database writes'],
                'correct_answer': 'Logging module with levels'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What architectural pattern does this implement?',
                'code': 'class PrintStrategy:\n    def print_data(self, data): pass\n\nclass JSONPrinter(PrintStrategy):\n    def print_data(self, data):\n        print(json.dumps(data, indent=2))\n\nclass TablePrinter(PrintStrategy):\n    def print_data(self, data):\n        for row in data:\n            print("\\t".join(str(x) for x in row))',
                'options': ['Strategy pattern', 'Factory pattern', 'Template pattern', 'State pattern'],
                'correct_answer': 'Strategy pattern'
            }
        ]