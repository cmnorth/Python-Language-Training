# =================================File Handling and Advanced Topics Quiz==================================
# quiz_advanced.py - Comprehensive quiz covering file operations, exceptions, modules, and advanced concepts
from quiz_base import QuizBase

class AdvancedQuiz(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "File Handling and Advanced Topics", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - REMEMBER/RECALL (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What function opens a file in Python?',
                'options': ['open()', 'file()', 'read()', 'load()'],
                'correct_answer': 'open()'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does "r" mode mean when opening a file?',
                'options': ['Read mode', 'Write mode', 'Append mode', 'Binary mode'],
                'correct_answer': 'Read mode'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'The _____ statement automatically closes files.',
                'correct_answer': ['with']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What keyword handles exceptions in Python?',
                'options': ['try', 'catch', 'handle', 'error'],
                'correct_answer': 'try'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To import a module: _____ module_name',
                'correct_answer': ['import']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does "w" mode do when opening a file?',
                'options': ['Reads file', 'Writes file (overwrites)', 'Appends to file', 'Creates backup'],
                'correct_answer': 'Writes file (overwrites)'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'The _____ block catches exceptions.',
                'correct_answer': ['except']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does the finally block do?',
                'options': ['Runs only on errors', 'Runs only on success', 'Always runs', 'Never runs'],
                'correct_answer': 'Always runs'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To read entire file content: file._____',
                'correct_answer': ['read()']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What creates a package in Python?',
                'options': ['__init__.py file', 'package.py file', 'folder only', 'import statement'],
                'correct_answer': '__init__.py file'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'To write text to file: file._____(text)',
                'correct_answer': ['write']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does readline() return?',
                'options': ['All lines', 'One line', 'File size', 'Line count'],
                'correct_answer': 'One line'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'The _____ keyword raises exceptions manually.',
                'correct_answer': ['raise']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does "a" mode do?',
                'options': ['Appends to file', 'Reads file', 'Creates new file', 'Deletes file'],
                'correct_answer': 'Appends to file'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'JSON files are handled with the _____ module.',
                'correct_answer': ['json']
            },

            # LEVEL 2 - UNDERSTAND/COMPREHEND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this file operation do?',
                'code': 'with open("data.txt", "r") as f:\n    content = f.read()\nprint(content)',
                'options': ['Reads and prints file content', 'Writes to file', 'Deletes file', 'Creates new file'],
                'correct_answer': 'Reads and prints file content'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why use "with" statement for files?',
                'options': ['Faster reading', 'Automatic file closing', 'Better formatting', 'Error prevention'],
                'correct_answer': 'Automatic file closing'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this exception handler do?',
                'code': 'try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")',
                'options': ['Catches division by zero error', 'Prevents all errors', 'Fixes the calculation', 'Ignores the error'],
                'correct_answer': 'Catches division by zero error'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'File objects are _____ and should be closed after use.',
                'correct_answer': ['resources']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this file writing produce?',
                'code': 'with open("output.txt", "w") as f:\n    f.write("Hello\\n")\n    f.write("World")',
                'options': ['Hello on line 1, World on line 2', 'HelloWorld on one line', 'Error', 'Empty file'],
                'correct_answer': 'Hello on line 1, World on line 2'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What happens if you open a non-existent file in "r" mode?',
                'options': ['Creates new file', 'Returns empty content', 'Raises FileNotFoundError', 'Returns None'],
                'correct_answer': 'Raises FileNotFoundError'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this module import do?',
                'code': 'import math\nresult = math.sqrt(16)\nprint(result)',
                'options': ['Prints 4.0', 'Prints 16', 'Prints 256', 'Error'],
                'correct_answer': 'Prints 4.0'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'The _____ function converts Python objects to JSON.',
                'correct_answer': ['dumps', 'json.dumps']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this exception chain show?',
                'code': 'try:\n    int("abc")\nexcept ValueError as e:\n    print(f"Error: {e}")',
                'options': ['Catches and displays error message', 'Fixes the conversion', 'Ignores the error', 'Retries the operation'],
                'correct_answer': 'Catches and displays error message'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What\'s the difference between read() and readlines()?',
                'options': ['No difference', 'read() returns string, readlines() returns list', 'readlines() is faster', 'read() is for binary files'],
                'correct_answer': 'read() returns string, readlines() returns list'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this CSV processing do?',
                'code': 'import csv\nwith open("data.csv") as f:\n    reader = csv.reader(f)\n    for row in reader:\n        print(row)',
                'options': ['Reads and prints CSV rows', 'Writes CSV data', 'Validates CSV format', 'Counts CSV rows'],
                'correct_answer': 'Reads and prints CSV rows'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'Binary files are opened with _____ mode suffix.',
                'correct_answer': ['b', '"b"']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this finally block ensure?',
                'code': 'try:\n    f = open("file.txt")\n    data = f.read()\nexcept:\n    print("Error")\nfinally:\n    f.close()',
                'options': ['File is always closed', 'Error is fixed', 'Data is saved', 'Exception is ignored'],
                'correct_answer': 'File is always closed'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does the os module provide?',
                'options': ['Math functions', 'Operating system interface', 'Web requests', 'Database access'],
                'correct_answer': 'Operating system interface'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'To handle multiple exception types: except (Type1, Type2) _____:',
                'correct_answer': ['as e', 'as error']
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this file handling code:',
                'code': 'f = open("data.txt", "r")\ncontent = f.read()\nprint(content)',
                'correct_answer': ['add f.close()', 'use with statement', 'close the file']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this backup system create?',
                'code': 'import shutil\ntry:\n    shutil.copy("important.txt", "important_backup.txt")\n    print("Backup created")\nexcept IOError:\n    print("Backup failed")',
                'options': ['File backup with error handling', 'File deletion system', 'File validator', 'File compressor'],
                'correct_answer': 'File backup with error handling'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To check if file exists: os.path._____(filename)',
                'correct_answer': ['exists']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What validation does this input system perform?',
                'code': 'while True:\n    try:\n        age = int(input("Enter age: "))\n        if age > 0:\n            break\n    except ValueError:\n        print("Please enter a number")',
                'options': ['Validates integer input with retry', 'Counts input attempts', 'Saves user data', 'Generates random numbers'],
                'correct_answer': 'Validates integer input with retry'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this JSON handling:',
                'code': 'import json\ndata = {"name": "Alice"}\nwith open("data.json", "w") as f:\n    f.write(data)',
                'correct_answer': ['json.dump(data, f)', 'use json.dump', 'serialize with json']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this log processing create?',
                'code': 'error_count = 0\nwith open("server.log") as f:\n    for line in f:\n        if "ERROR" in line:\n            error_count += 1\nprint(f"Errors found: {error_count}")',
                'options': ['Error counter for log analysis', 'Log file creator', 'Error fixer', 'Performance monitor'],
                'correct_answer': 'Error counter for log analysis'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To create custom exceptions: class MyError(_____):',
                'correct_answer': ['Exception']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this configuration loader do?',
                'code': 'import json\ntry:\n    with open("config.json") as f:\n        config = json.load(f)\nexcept FileNotFoundError:\n    config = {"debug": True}  # Default config',
                'options': ['Loads config with fallback defaults', 'Creates new config file', 'Validates config format', 'Backs up config'],
                'correct_answer': 'Loads config with fallback defaults'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this directory listing:',
                'code': 'import os\nfiles = os.list(".")\nprint(files)',
                'correct_answer': ['os.listdir(".")', 'use listdir', 'correct function name']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this CSV writer create?',
                'code': 'import csv\ndata = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]\nwith open("people.csv", "w", newline="") as f:\n    writer = csv.writer(f)\n    writer.writerows(data)',
                'options': ['Creates CSV file from data', 'Reads CSV file', 'Validates CSV format', 'Sorts CSV data'],
                'correct_answer': 'Creates CSV file from data'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To get file size: os.path._____(filename)',
                'correct_answer': ['getsize']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What pattern does this database connection use?',
                'code': 'import sqlite3\ntry:\n    conn = sqlite3.connect("data.db")\n    cursor = conn.cursor()\n    cursor.execute("SELECT * FROM users")\n    results = cursor.fetchall()\nfinally:\n    conn.close()',
                'options': ['Database connection with cleanup', 'Database creation', 'Data validation', 'Query optimization'],
                'correct_answer': 'Database connection with cleanup'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this path joining:',
                'code': 'import os\npath = "folder" + "/" + "file.txt"\nprint(path)',
                'correct_answer': ['os.path.join("folder", "file.txt")', 'use os.path.join', 'cross-platform path']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this file processor create?',
                'code': 'def process_files(directory):\n    import os\n    for filename in os.listdir(directory):\n        if filename.endswith(".txt"):\n            filepath = os.path.join(directory, filename)\n            with open(filepath) as f:\n                content = f.read()\n                yield filename, len(content)',
                'options': ['Text file analyzer generator', 'File copier', 'Directory creator', 'File validator'],
                'correct_answer': 'Text file analyzer generator'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To handle any exception: except _____ as e:',
                'correct_answer': ['Exception']
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What security issue does this demonstrate?',
                'code': 'filename = input("Enter filename: ")\nwith open(filename) as f:\n    content = f.read()\nprint(content)',
                'options': ['Path traversal vulnerability', 'Memory overflow', 'Type error', 'Syntax error'],
                'correct_answer': 'Path traversal vulnerability'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why might this exception handling be problematic?',
                'options': ['except: pass', 'It hides all errors', 'It\'s too slow', 'It uses too much memory'],
                'correct_answer': 'It hides all errors'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue does this file processing have?',
                'code': 'def count_words(filename):\n    word_count = 0\n    with open(filename) as f:\n        for line in f:\n            words = line.split()\n            word_count += len(words)\n    return word_count',
                'options': ['Inefficient for large files', 'Memory leak', 'Infinite loop', 'Type errors'],
                'correct_answer': 'Inefficient for large files'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the race condition:',
                'code': 'import threading\ndef write_log(message):\n    with open("app.log", "a") as f:\n        f.write(f"{time.time()}: {message}\\n")',
                'correct_answer': ['concurrent file access', 'multiple threads writing', 'need file locking']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What memory issue might this cause with large files?',
                'code': 'with open("huge_file.txt") as f:\n    content = f.read()  # Loads entire file\n    words = content.split()\n    return len(words)',
                'options': ['Memory exhaustion from loading entire file', 'CPU overhead', 'Disk space issues', 'Network problems'],
                'correct_answer': 'Memory exhaustion from loading entire file'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'When should you use buffered I/O vs unbuffered?',
                'options': ['Always use buffered', 'Buffered for large files, unbuffered for real-time', 'Always use unbuffered', 'No difference'],
                'correct_answer': 'Buffered for large files, unbuffered for real-time'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What encoding issue might this cause?',
                'code': 'with open("international.txt") as f:\n    content = f.read()\n    # File contains non-ASCII characters',
                'options': ['Unicode decode errors', 'File permission errors', 'Memory issues', 'Syntax errors'],
                'correct_answer': 'Unicode decode errors'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'File _____ occurs when too many files are opened simultaneously.',
                'correct_answer': ['descriptor exhaustion', 'handle leakage']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What scalability problem does this backup system have?',
                'code': 'def backup_files(source_dir, backup_dir):\n    for filename in os.listdir(source_dir):\n        src = os.path.join(source_dir, filename)\n        dst = os.path.join(backup_dir, filename)\n        shutil.copy2(src, dst)',
                'options': ['No error handling for individual files', 'Memory usage', 'CPU intensive', 'Network issues'],
                'correct_answer': 'No error handling for individual files'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What\'s the main risk of catching all exceptions with "except:"?',
                'options': ['Performance degradation', 'Hiding critical errors', 'Memory leaks', 'Syntax issues'],
                'correct_answer': 'Hiding critical errors'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What concurrency issue does this logger have?',
                'code': 'import threading\nlog_file = open("app.log", "a")\n\ndef log_message(msg):\n    log_file.write(f"{msg}\\n")\n    log_file.flush()',
                'options': ['Shared file handle across threads', 'Memory corruption', 'Deadlocks', 'CPU bottleneck'],
                'correct_answer': 'Shared file handle across threads'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Fix this resource leak in exception handling:',
                'code': 'f = open("data.txt")\ntry:\n    data = process_file(f)\nexcept:\n    print("Error occurred")\nreturn data',
                'correct_answer': ['add finally block', 'ensure f.close()', 'use with statement']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What security vulnerability does this CSV processor have?',
                'code': 'import csv\ndef process_csv(filename):\n    with open(filename) as f:\n        reader = csv.reader(f)\n        for row in reader:\n            eval(row[0])  # Executes code from CSV',
                'options': ['Code injection vulnerability', 'File permission issue', 'Memory overflow', 'Type conversion error'],
                'correct_answer': 'Code injection vulnerability'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Atomic file operations prevent _____ conditions in concurrent access.',
                'correct_answer': ['race', 'corruption']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why might pickle be dangerous for untrusted data?',
                'options': ['Slow performance', 'Large file sizes', 'Can execute arbitrary code', 'Format incompatibility'],
                'correct_answer': 'Can execute arbitrary code'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced file system does this implement?',
                'code': 'class ManagedFileSystem:\n    def __init__(self):\n        self.open_files = {}\n        self.file_locks = {}\n    \n    def open_file(self, path, mode, timeout=30):\n        if path in self.file_locks:\n            raise FileInUseError(path)\n        \n        self.file_locks[path] = threading.Lock()\n        handle = open(path, mode)\n        self.open_files[handle] = path\n        return handle\n    \n    def close_file(self, handle):\n        if handle in self.open_files:\n            path = self.open_files[handle]\n            handle.close()\n            del self.open_files[handle]\n            del self.file_locks[path]',
                'options': ['Thread-safe file management system', 'Simple file opener', 'File validator', 'Performance monitor'],
                'correct_answer': 'Thread-safe file management system'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'What design pattern best handles multiple file formats?',
                'options': ['Strategy Pattern', 'Factory Pattern', 'Observer Pattern', 'Adapter Pattern'],
                'correct_answer': 'Strategy Pattern'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What streaming processor does this create?',
                'code': 'class StreamingFileProcessor:\n    def __init__(self, chunk_size=8192):\n        self.chunk_size = chunk_size\n        self.processors = []\n    \n    def add_processor(self, func):\n        self.processors.append(func)\n    \n    def process_file(self, filename):\n        with open(filename, "rb") as f:\n            while chunk := f.read(self.chunk_size):\n                for processor in self.processors:\n                    chunk = processor(chunk)\n                yield chunk',
                'options': ['Configurable streaming file processor', 'Simple file reader', 'File validator', 'Backup system'],
                'correct_answer': 'Configurable streaming file processor'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'For handling massive files, implement _____ processing to avoid memory issues.',
                'correct_answer': ['streaming', 'chunked', 'lazy']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What fault-tolerant system does this establish?',
                'code': 'class ResilientFileProcessor:\n    def __init__(self, max_retries=3, backoff_factor=2):\n        self.max_retries = max_retries\n        self.backoff_factor = backoff_factor\n    \n    def process_with_retry(self, operation, *args, **kwargs):\n        for attempt in range(self.max_retries):\n            try:\n                return operation(*args, **kwargs)\n            except (IOError, OSError) as e:\n                if attempt == self.max_retries - 1:\n                    raise\n                sleep_time = self.backoff_factor ** attempt\n                time.sleep(sleep_time)\n                logging.warning(f"Retry {attempt + 1} after {e}")',
                'options': ['Fault-tolerant file operation system', 'Simple retry mechanism', 'Error logger', 'Performance monitor'],
                'correct_answer': 'Fault-tolerant file operation system'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For processing terabytes of log files, which architecture is best?',
                'options': ['Load all into memory', 'Streaming with generators', 'Random access', 'Sequential buffering'],
                'correct_answer': 'Streaming with generators'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What distributed file system does this implement?',
                'code': 'class DistributedFileProcessor:\n    def __init__(self, worker_nodes):\n        self.worker_nodes = worker_nodes\n    \n    def process_large_file(self, filename):\n        file_size = os.path.getsize(filename)\n        chunk_size = file_size // len(self.worker_nodes)\n        \n        futures = []\n        for i, node in enumerate(self.worker_nodes):\n            start = i * chunk_size\n            end = start + chunk_size if i < len(self.worker_nodes) - 1 else file_size\n            future = node.process_chunk(filename, start, end)\n            futures.append(future)\n        \n        return self.combine_results(futures)',
                'options': ['Distributed file processing system', 'Simple file splitter', 'Load balancer', 'File validator'],
                'correct_answer': 'Distributed file processing system'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this asynchronous file processor:',
                'code': 'import asyncio\nimport aiofiles\n\nasync def process_files_async(filenames):\n    tasks = []\n    for filename in filenames:\n        task = asyncio.create_task(process_single_file(filename))\n        tasks.append(task)\n    \n    results = await asyncio.gather(*tasks)\n    return results',
                'correct_answer': ['add async file operations', 'use aiofiles.open', 'implement async context managers']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What versioning system does this file manager create?',
                'code': 'class VersionedFileManager:\n    def __init__(self, base_path):\n        self.base_path = base_path\n        self.versions = {}\n    \n    def save_file(self, filename, content):\n        version = self.versions.get(filename, 0) + 1\n        versioned_name = f"{filename}.v{version}"\n        full_path = os.path.join(self.base_path, versioned_name)\n        \n        with open(full_path, "w") as f:\n            f.write(content)\n        \n        self.versions[filename] = version\n        return version\n    \n    def get_file_versions(self, filename):\n        return list(range(1, self.versions.get(filename, 0) + 1))',
                'options': ['File versioning management system', 'Simple file saver', 'Backup creator', 'File validator'],
                'correct_answer': 'File versioning management system'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'To handle file operations across different storage backends, implement the _____ pattern.',
                'correct_answer': ['adapter', 'bridge', 'strategy']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'What architecture best handles real-time file monitoring?',
                'options': ['Polling every second', 'Event-driven with file system watches', 'Continuous scanning', 'Manual checking'],
                'correct_answer': 'Event-driven with file system watches'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What caching system does this file loader implement?',
                'code': 'class CachedFileLoader:\n    def __init__(self, cache_size=100):\n        self.cache = {}\n        self.access_order = []\n        self.cache_size = cache_size\n    \n    def load_file(self, filename):\n        if filename in self.cache:\n            self.access_order.remove(filename)\n            self.access_order.append(filename)\n            return self.cache[filename]\n        \n        with open(filename) as f:\n            content = f.read()\n        \n        if len(self.cache) >= self.cache_size:\n            oldest = self.access_order.pop(0)\n            del self.cache[oldest]\n        \n        self.cache[filename] = content\n        self.access_order.append(filename)\n        return content',
                'options': ['LRU cache for file contents', 'Simple file cache', 'File validator', 'Performance monitor'],
                'correct_answer': 'LRU cache for file contents'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Design a secure file upload system:',
                'code': 'def secure_upload(file_data, filename):\n    # Validate filename\n    if ".." in filename or filename.startswith("/"):\n        raise SecurityError("Invalid filename")\n    \n    # Check file type\n    allowed_extensions = [".txt", ".jpg", ".png"]\n    if not any(filename.endswith(ext) for ext in allowed_extensions):\n        raise SecurityError("File type not allowed")',
                'correct_answer': ['add file size limits', 'validate content type', 'sanitize filename']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What configuration management system does this create?',
                'code': 'class ConfigurationManager:\n    def __init__(self, config_dir):\n        self.config_dir = config_dir\n        self.watchers = {}\n        self.configs = {}\n    \n    def load_config(self, name, reload_on_change=True):\n        config_path = os.path.join(self.config_dir, f"{name}.json")\n        \n        with open(config_path) as f:\n            config = json.load(f)\n        \n        self.configs[name] = config\n        \n        if reload_on_change:\n            self.setup_file_watcher(config_path, name)\n        \n        return config\n    \n    def setup_file_watcher(self, path, name):\n        # Monitor file for changes and reload automatically\n        pass',
                'options': ['Dynamic configuration management system', 'Simple config loader', 'File validator', 'Settings manager'],
                'correct_answer': 'Dynamic configuration management system'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'For high-performance file I/O, consider using _____ mapped files.',
                'correct_answer': ['memory', 'mmap']
            }
        ]