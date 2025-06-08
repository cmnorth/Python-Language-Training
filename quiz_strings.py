# =================================Strings and Text Processing Quiz==================================
# quiz_strings.py - Comprehensive quiz covering string operations, methods, and text processing
from quiz_base import QuizBase

class StringsQuiz(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "Strings and Text Processing", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - REMEMBER/RECALL (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does str() function do?',
                'options': ['Creates strings', 'Converts values to strings', 'Measures string length', 'Splits strings'],
                'correct_answer': 'Converts values to strings'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'How do you create a string in Python?',
                'options': ['Using quotes', 'Using str()', 'Using brackets', 'Both A and B'],
                'correct_answer': 'Both A and B'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'Strings in Python are _____ (cannot be changed).',
                'correct_answer': ['immutable']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which quotes can create strings?',
                'options': ['Single quotes only', 'Double quotes only', 'Both single and double', 'Square brackets'],
                'correct_answer': 'Both single and double'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To get a character at position 0: text[___]',
                'correct_answer': ['0']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is string concatenation?',
                'options': ['Joining strings together', 'Splitting strings apart', 'Converting to uppercase', 'Measuring length'],
                'correct_answer': 'Joining strings together'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To join strings use the _____ operator.',
                'correct_answer': ['+', 'plus']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does len() return for strings?',
                'options': ['Number of words', 'Number of characters', 'Number of lines', 'Memory usage'],
                'correct_answer': 'Number of characters'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'String slicing uses _____ notation.',
                'correct_answer': ['bracket', 'square bracket']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which method converts to uppercase?',
                'options': ['upper()', 'capitalize()', 'title()', 'All of these'],
                'correct_answer': 'upper()'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To check if string contains text: "text" _____ string',
                'correct_answer': ['in']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does strip() remove?',
                'options': ['All spaces', 'Leading/trailing whitespace', 'All characters', 'Numbers only'],
                'correct_answer': 'Leading/trailing whitespace'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To split string into list: text._____(" ")',
                'correct_answer': ['split']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'String formatting with {} uses which method?',
                'options': ['format()', 'replace()', 'join()', 'split()'],
                'correct_answer': 'format()'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'f-strings start with the letter _____',
                'correct_answer': ['f']
            },

            # LEVEL 2 - UNDERSTAND/COMPREHEND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this string operation produce?',
                'code': 'text = "Hello"\nresult = text + " World"\nprint(result)',
                'options': ['Hello World', 'HelloWorld', 'Hello + World', 'Error'],
                'correct_answer': 'Hello World'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why are strings immutable in Python?',
                'options': ['Performance optimization', 'Memory safety', 'Hash consistency', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this slicing return?',
                'code': 'text = "Python"\nprint(text[1:4])',
                'options': ['Pyt', 'yth', 'ytho', 'Pyth'],
                'correct_answer': 'yth'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'Negative indexing starts from the _____ of the string.',
                'correct_answer': ['end', 'right']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this expression evaluate to?',
                'code': 'text = "Hello"\nprint(text[-1])',
                'options': ['H', 'e', 'l', 'o'],
                'correct_answer': 'o'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What happens when you multiply a string by an integer?',
                'options': ['Error occurs', 'String repeats', 'String converts to number', 'Nothing happens'],
                'correct_answer': 'String repeats'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this produce?',
                'code': 'name = "Alice"\nage = 25\ntext = f"Hello {name}, you are {age}"\nprint(text)',
                'options': ['Hello Alice, you are 25', 'Hello {name}, you are {age}', 'Error', 'Hello Alice25'],
                'correct_answer': 'Hello Alice, you are 25'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'The _____ method joins list elements into a string.',
                'correct_answer': ['join']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this string method return?',
                'code': 'text = "  Hello World  "\nresult = text.strip()\nprint(result)',
                'options': ['  Hello World  ', 'Hello World', 'HelloWorld', 'Hello  World'],
                'correct_answer': 'Hello World'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does the replace() method do?',
                'options': ['Changes original string', 'Returns new string with replacements', 'Deletes characters', 'Converts case'],
                'correct_answer': 'Returns new string with replacements'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this membership test return?',
                'code': 'text = "Python Programming"\nresult = "gram" in text\nprint(result)',
                'options': ['True', 'False', 'Error', 'None'],
                'correct_answer': 'True'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'String methods that check conditions return _____ values.',
                'correct_answer': ['boolean', 'True/False']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this case conversion produce?',
                'code': 'text = "hello WORLD"\nresult = text.title()\nprint(result)',
                'options': ['Hello World', 'HELLO WORLD', 'hello world', 'Hello WORLD'],
                'correct_answer': 'Hello World'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What\'s the difference between split() and split(" ")?',
                'options': ['No difference', 'split() handles multiple whitespace', 'split(" ") is faster', 'split() only works on spaces'],
                'correct_answer': 'split() handles multiple whitespace'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'Escape sequences in strings start with _____',
                'correct_answer': ['backslash', '\\']
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this string formatting:',
                'code': 'name = "Bob"\nage = 30\ntext = "Hello {}, you are {} years old".format(name)\nprint(text)',
                'correct_answer': ['add age parameter', '.format(name, age)', 'include both arguments']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this text processing create?',
                'code': 'words = ["Python", "is", "awesome"]\nsentence = " ".join(words)\nprint(sentence)',
                'options': ['Python is awesome', 'Python,is,awesome', 'Pythonisawesome', 'Error'],
                'correct_answer': 'Python is awesome'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To count occurrences of substring: text._____(substring)',
                'correct_answer': ['count']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What validation does this perform?',
                'code': 'user_input = input("Enter email: ")\nif "@" in user_input and "." in user_input:\n    print("Valid format")',
                'options': ['Email format validation', 'Character counting', 'Case checking', 'Length validation'],
                'correct_answer': 'Email format validation'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this string slicing:',
                'code': 'text = "Programming"\nfirst_five = text[0,5]\nprint(first_five)',
                'correct_answer': ['text[0:5]', 'use colon', 'slice with :']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this password checker do?',
                'code': 'password = "MyPass123"\nhas_upper = any(c.isupper() for c in password)\nhas_digit = any(c.isdigit() for c in password)\nprint(has_upper and has_digit)',
                'options': ['Checks for uppercase and digits', 'Counts characters', 'Validates length', 'Encrypts password'],
                'correct_answer': 'Checks for uppercase and digits'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To check if string starts with prefix: text._____(prefix)',
                'correct_answer': ['startswith']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this text cleaner produce?',
                'code': 'text = "  Hello,   World!  "\ncleaned = " ".join(text.split())\nprint(cleaned)',
                'options': ['Hello, World!', '  Hello,   World!  ', 'Hello,World!', 'HelloWorld'],
                'correct_answer': 'Hello, World!'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this string comparison:',
                'code': 'name1 = "Alice"\nname2 = "alice"\nif name1 == name2:\n    print("Same")',
                'correct_answer': ['name1.lower() == name2.lower()', 'case insensitive comparison', 'convert to same case']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What pattern does this URL extractor find?',
                'code': 'text = "Visit https://python.org for more info"\nstart = text.find("https://")\nend = text.find(" ", start)\nurl = text[start:end]\nprint(url)',
                'options': ['Extracts URL from text', 'Counts URLs', 'Validates URLs', 'Removes URLs'],
                'correct_answer': 'Extracts URL from text'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To pad string with zeros: text._____(width, "0")',
                'correct_answer': ['zfill', 'rjust']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this name formatter create?',
                'code': 'first = "john"\nlast = "DOE"\nfull = f"{first.title()} {last.title()}"\nprint(full)',
                'options': ['John Doe', 'john DOE', 'JOHN DOE', 'John DOE'],
                'correct_answer': 'John Doe'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this multi-line string:',
                'code': 'message = "Hello\nThis is line 2\nThis is line 3"\nprint(message)',
                'correct_answer': ['correct as is', 'no error', 'already proper format']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this CSV parser create?',
                'code': 'data = "apple,banana,orange"\nfruits = data.split(",")\nprint(fruits)',
                'options': ["['apple', 'banana', 'orange']", 'apple banana orange', 'Error', 'apple,banana,orange'],
                'correct_answer': "['apple', 'banana', 'orange']"
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To find last occurrence: text._____(substring)',
                'correct_answer': ['rfind', 'rindex']
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue does this demonstrate?',
                'code': 'result = ""\nfor i in range(1000):\n    result += str(i)\nprint(result)',
                'options': ['String concatenation inefficiency', 'Memory leaks', 'Infinite loops', 'Type errors'],
                'correct_answer': 'String concatenation inefficiency'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why is string concatenation with + slow for many operations?',
                'options': ['Creates new objects each time', 'Uses too much memory', 'Causes type errors', 'All of the above'],
                'correct_answer': 'Creates new objects each time'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What encoding issue might this cause?',
                'code': 'text = "Café résumé naïve"\nwith open("file.txt", "w") as f:\n    f.write(text)',
                'options': ['Unicode encoding problems', 'File permission errors', 'Memory issues', 'Syntax errors'],
                'correct_answer': 'Unicode encoding problems'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the security vulnerability:',
                'code': 'user_input = input("Enter SQL: ")\nquery = f"SELECT * FROM users WHERE name = \'{user_input}\'"\nexecute_query(query)',
                'correct_answer': ['SQL injection vulnerability', 'use parameterized queries', 'unsanitized input']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What memory optimization does this use?',
                'code': 'words = ["hello", "world", "python"]\nresult = "".join(words)\nprint(result)',
                'options': ['Efficient string joining', 'Memory recycling', 'Garbage collection', 'String interning'],
                'correct_answer': 'Efficient string joining'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'When should you use format() vs f-strings?',
                'options': ['Always use f-strings', 'format() for templates, f-strings for simple cases', 'No difference', 'format() is deprecated'],
                'correct_answer': 'format() for templates, f-strings for simple cases'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What internationalization issue does this have?',
                'code': 'name = "müller"\nprint(name.upper())',
                'options': ['Locale-specific case conversion', 'Character encoding', 'String length calculation', 'Memory usage'],
                'correct_answer': 'Locale-specific case conversion'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'String _____ occurs when Python reuses identical string objects.',
                'correct_answer': ['interning']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What thread safety issue might this cause?',
                'code': 'import threading\nglobal_text = ""\ndef append_text(text):\n    global global_text\n    global_text += text',
                'options': ['Race conditions on shared string', 'Memory corruption', 'Deadlocks', 'String fragmentation'],
                'correct_answer': 'Race conditions on shared string'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What\'s the time complexity of string concatenation with +?',
                'options': ['O(1)', 'O(n)', 'O(n²)', 'O(log n)'],
                'correct_answer': 'O(n²)'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What validation weakness does this show?',
                'code': 'def validate_email(email):\n    return "@" in email and email.count("@") == 1',
                'options': ['Insufficient email validation', 'Performance issues', 'Memory leaks', 'Type errors'],
                'correct_answer': 'Insufficient email validation'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Fix this regex alternative for better performance:',
                'code': 'import re\nfor line in huge_file:\n    if re.search(r"pattern", line):\n        process(line)',
                'correct_answer': ['compile regex outside loop', 'pattern = re.compile()', 'avoid recompilation']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What scalability issue does this demonstrate?',
                'code': 'def process_large_text(text):\n    words = text.split()\n    for word in words:\n        if word.lower() in ["bad", "words"]:\n            text = text.replace(word, "***")\n    return text',
                'options': ['Repeated string operations on large text', 'Memory allocation', 'CPU intensive operations', 'I/O bottlenecks'],
                'correct_answer': 'Repeated string operations on large text'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'For large text processing, use _____ instead of string concatenation.',
                'correct_answer': ['StringIO', 'list.join', 'buffer']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why might string.strip() be dangerous with user input?',
                'options': ['Removes too much', 'Can cause errors', 'Security implications', 'Performance issues'],
                'correct_answer': 'Removes too much'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced text processor does this create?',
                'code': 'class TextProcessor:\n    def __init__(self):\n        self.filters = []\n    \n    def add_filter(self, func):\n        self.filters.append(func)\n    \n    def process(self, text):\n        for filter_func in self.filters:\n            text = filter_func(text)\n        return text',
                'options': ['Configurable text processing pipeline', 'String validator', 'Text encoder', 'File processor'],
                'correct_answer': 'Configurable text processing pipeline'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'What design pattern would best handle multiple string encoding formats?',
                'options': ['Strategy Pattern', 'Factory Pattern', 'Observer Pattern', 'Singleton Pattern'],
                'correct_answer': 'Strategy Pattern'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What text analysis system does this implement?',
                'code': 'from collections import Counter\ndef analyze_text(text):\n    words = text.lower().split()\n    return {\n        "word_count": len(words),\n        "unique_words": len(set(words)),\n        "most_common": Counter(words).most_common(5)\n    }',
                'options': ['Comprehensive text statistics analyzer', 'Word frequency counter only', 'Text similarity checker', 'Language detector'],
                'correct_answer': 'Comprehensive text statistics analyzer'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'To create efficient string builders in Python, use _____ class.',
                'correct_answer': ['StringIO', 'io.StringIO']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What template system does this create?',
                'code': 'class Template:\n    def __init__(self, template):\n        self.template = template\n    \n    def render(self, **kwargs):\n        result = self.template\n        for key, value in kwargs.items():\n            result = result.replace(f"{{{key}}}", str(value))\n        return result',
                'options': ['Simple template engine', 'String formatter', 'Text replacer', 'Variable substitution'],
                'correct_answer': 'Simple template engine'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For processing millions of strings, which approach is most efficient?',
                'options': ['String concatenation', 'list.join()', 'StringIO', 'Both B and C'],
                'correct_answer': 'Both B and C'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What natural language processing foundation does this create?',
                'code': 'import re\nclass TextTokenizer:\n    def __init__(self):\n        self.patterns = {\n            "words": r"\\b\\w+\\b",\n            "sentences": r"[.!?]+",\n            "emails": r"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"\n        }\n    \n    def tokenize(self, text, pattern_type):\n        return re.findall(self.patterns[pattern_type], text)',
                'options': ['Flexible text tokenization system', 'Email validator', 'Sentence splitter', 'Word counter'],
                'correct_answer': 'Flexible text tokenization system'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Design a string cache system for frequently used strings:',
                'code': 'class StringCache:\n    def __init__(self):\n        self.cache = {}\n    \n    def get_string(self, key):\n        if key not in self.cache:\n            self.cache[key] = expensive_string_operation(key)\n        return self.cache[key]',
                'correct_answer': ['add LRU eviction', 'implement size limits', 'add thread safety']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What internationalization system does this build?',
                'code': 'class I18nString:\n    def __init__(self, translations):\n        self.translations = translations\n        self.locale = "en"\n    \n    def set_locale(self, locale):\n        self.locale = locale\n    \n    def __str__(self):\n        return self.translations.get(self.locale, self.translations["en"])',
                'options': ['Localized string management system', 'Translation cache', 'Language detector', 'Text converter'],
                'correct_answer': 'Localized string management system'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'For streaming text processing, implement a _____ pattern to handle large files.',
                'correct_answer': ['generator', 'iterator', 'lazy evaluation']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'What would be the best architecture for a text processing microservice?',
                'options': ['Monolithic string handler', 'Pipeline of specialized processors', 'Single large function', 'Global string operations'],
                'correct_answer': 'Pipeline of specialized processors'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced search system does this implement?',
                'code': 'class FuzzyStringMatcher:\n    def __init__(self, strings):\n        self.strings = strings\n    \n    def find_similar(self, target, threshold=0.8):\n        matches = []\n        for string in self.strings:\n            similarity = self.calculate_similarity(target, string)\n            if similarity >= threshold:\n                matches.append((string, similarity))\n        return sorted(matches, key=lambda x: x[1], reverse=True)',
                'options': ['Fuzzy string matching system', 'Exact string search', 'String validator', 'Text indexer'],
                'correct_answer': 'Fuzzy string matching system'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this streaming text processor:',
                'code': 'def process_large_file(filename):\n    with open(filename, "r") as f:\n        for line in f:\n            # Process line by line\n            yield process_line(line)',
                'correct_answer': ['add error handling', 'implement buffering', 'add encoding specification']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What text validation framework does this establish?',
                'code': 'class StringValidator:\n    def __init__(self):\n        self.rules = []\n    \n    def add_rule(self, rule_func, error_msg):\n        self.rules.append((rule_func, error_msg))\n    \n    def validate(self, text):\n        errors = []\n        for rule, msg in self.rules:\n            if not rule(text):\n                errors.append(msg)\n        return errors',
                'options': ['Configurable string validation framework', 'Error logger', 'Text formatter', 'Rule engine'],
                'correct_answer': 'Configurable string validation framework'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'To handle billions of strings efficiently, consider using _____ data structures.',
                'correct_answer': ['trie', 'suffix tree', 'hash table']
            }
        ]