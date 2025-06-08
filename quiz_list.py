# =================================List Function Quiz Module==================================
# quiz_list.py - Comprehensive list() function quiz with 75 questions across 5 Bloom's levels
from quiz_base import QuizBase

class QuizList(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "list", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - KNOWLEDGE/REMEMBER (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does list() without arguments create?',
                'options': ['Empty list', 'List with None', 'List with 0', 'Error'],
                'correct_answer': 'Empty list'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is list("abc")?',
                'options': ["['abc']", "['a', 'b', 'c']", "['a b c']", 'Error'],
                'correct_answer': "['a', 'b', 'c']"
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What type of object does list() return?',
                'correct_answer': 'list'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does list([1, 2, 3]) create?',
                'options': ['Copy of the list', 'Reference to original', 'Nested list', 'Error'],
                'correct_answer': 'Copy of the list'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'list() converts any _____ into a list.',
                'correct_answer': ['iterable']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is list(range(3))?',
                'options': ['[0, 1, 2]', '[1, 2, 3]', '[0, 1, 2, 3]', 'range(3)'],
                'correct_answer': '[0, 1, 2]'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What method adds an item to the end of a list?',
                'correct_answer': 'append'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which creates a list from a tuple?',
                'options': ['list((1, 2, 3))', 'list{1, 2, 3}', 'list[1, 2, 3]', 'list<1, 2, 3>'],
                'correct_answer': 'list((1, 2, 3))'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'Lists are _____, meaning they can be changed after creation.',
                'correct_answer': ['mutable']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does list({1, 2, 3}) create?',
                'options': ['Set in list form', 'List with set elements', 'List of numbers 1,2,3', 'Error'],
                'correct_answer': 'List of numbers 1,2,3'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What method removes an item from a list by value?',
                'correct_answer': 'remove'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is the difference between [] and list()?',
                'options': ['No difference', '[] is faster', 'list() is more explicit', 'list() creates copy'],
                'correct_answer': 'No difference'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'list() can convert strings, tuples, sets, and other _____ to lists.',
                'correct_answer': ['iterables', 'sequences']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does list(enumerate(["a", "b"])) create?',
                'options': ["[(0, 'a'), (1, 'b')]", "['a', 'b']", "[0, 1]", "['0a', '1b']"],
                'correct_answer': "[(0, 'a'), (1, 'b')]"
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What operator adds two lists together?',
                'correct_answer': '+'
            },

            # LEVEL 2 - COMPREHENSION/UNDERSTAND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this code output?',
                'code': 'original = [1, 2, 3]\ncopy = list(original)\ncopy.append(4)\nprint(len(original))',
                'options': ['3', '4', 'Error', 'None'],
                'correct_answer': '3'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why would you use list() instead of []?',
                'options': ['Better performance', 'To convert other iterables', 'To create nested lists', 'No reason'],
                'correct_answer': 'To convert other iterables'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'list() creates a _____ copy of the iterable.',
                'correct_answer': ['shallow']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this accomplish?',
                'code': 'words = "hello world".split()\nletters = list("".join(words))',
                'options': ['Creates list of all letters without spaces', 'Creates list of words', 'Creates list of characters', 'Causes error'],
                'correct_answer': 'Creates list of all letters without spaces'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the difference between list(x) and x[:]?',
                'options': ['No difference for sequences', 'list() works with any iterable', 'x[:] is always faster', 'list() creates deeper copy'],
                'correct_answer': 'list() works with any iterable'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this return?',
                'code': 'data = {"a": 1, "b": 2}\nkeys_list = list(data.keys())\nprint(keys_list)',
                'options': ["['a', 'b']", "[1, 2]", "['a': 1, 'b': 2]", 'Error'],
                'correct_answer': "['a', 'b']"
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'list() with a generator expression creates a list by _____ all values.',
                'correct_answer': ['consuming', 'evaluating']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What happens when you call list() on a file object?',
                'options': ['Creates list of filenames', 'Creates list of lines', 'Creates empty list', 'Causes error'],
                'correct_answer': 'Creates list of lines'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this filtering accomplish?',
                'code': 'numbers = [1, 2, 3, 4, 5]\neven = list(filter(lambda x: x % 2 == 0, numbers))\nprint(even)',
                'options': ['[2, 4]', '[1, 3, 5]', '[1, 2, 3, 4, 5]', 'Error'],
                'correct_answer': '[2, 4]'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why might list(range(n)) be memory intensive?',
                'options': ['Range is slow', 'Creates all values in memory at once', 'Range uses more memory', 'No difference'],
                'correct_answer': 'Creates all values in memory at once'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'list() with map() forces _____ evaluation of the map object.',
                'correct_answer': ['eager', 'immediate']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this nested structure create?',
                'code': 'matrix = list([1, 2], [3, 4], [5, 6])',
                'options': ['2D list/matrix', 'Flat list', 'Error - invalid syntax', 'List of tuples'],
                'correct_answer': 'Error - invalid syntax'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the relationship between list() and list comprehensions?',
                'options': ['Same thing', 'list() is faster', 'List comprehensions are more readable', 'No relationship'],
                'correct_answer': 'List comprehensions are more readable'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'list() can convert _____ objects like zip() and enumerate() to lists.',
                'correct_answer': ['iterator']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this type conversion accomplish?',
                'code': 'user_input = "1,2,3,4"\nnumbers = list(map(int, user_input.split(",")))\nprint(numbers)',
                'options': ['[1, 2, 3, 4]', "['1', '2', '3', '4']", '[1234]', 'Error'],
                'correct_answer': '[1, 2, 3, 4]'
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this list creation from user input:',
                'code': 'user_data = input("Enter numbers: ")\nnumbers = list(user_data.split())\nprint(sum(numbers))',
                'correct_answer': ['list(map(int, user_data.split()))', 'convert to int', 'map to integers']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this data processing create?',
                'code': 'text = "Hello World Python"\nwords = text.split()\ncapitalized = list(map(str.upper, words))\nprint(capitalized)',
                'options': ["['HELLO', 'WORLD', 'PYTHON']", "['Hello', 'World', 'Python']", "['hello', 'world', 'python']", 'Error'],
                'correct_answer': "['HELLO', 'WORLD', 'PYTHON']"
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To flatten a list of lists: flat = list(_____)',
                'correct_answer': ['itertools.chain(*nested)', 'chain.from_iterable']
            },
            {
                'level': 3,
                'type': 'mix_match',
                'question': 'Match list creation patterns with their use cases:',
                'left_items': ['list(range(n))', 'list(map(func, data))', 'list(filter(pred, data))', 'list(zip(a, b))'],
                'right_items': ['Transform elements', 'Pair elements', 'Generate sequence', 'Select elements'],
                'correct_answer': {0: 'Generate sequence', 1: 'Transform elements', 2: 'Select elements', 3: 'Pair elements'}
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this validation system create?',
                'code': 'def validate_inputs(data):\n    valid_items = list(filter(lambda x: isinstance(x, int) and x > 0, data))\n    return valid_items\n\nresult = validate_inputs([1, -2, "3", 4, 0])\nprint(result)',
                'options': ['[1, 4]', '[1, 3, 4]', '[1, -2, 4]', 'Error'],
                'correct_answer': '[1, 4]'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this matrix row extraction:',
                'code': 'matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\nfirst_column = list(row[0] for row in matrix)\nprint(first_column)',
                'correct_answer': ['code is correct', 'no error', 'syntax is valid']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this batch processing accomplish?',
                'code': 'def create_batches(data, batch_size):\n    batches = []\n    for i in range(0, len(data), batch_size):\n        batch = list(data[i:i+batch_size])\n        batches.append(batch)\n    return batches',
                'options': ['Splits data into fixed-size chunks', 'Sorts data into groups', 'Filters data by size', 'Validates data format'],
                'correct_answer': 'Splits data into fixed-size chunks'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To remove duplicates while preserving order: unique = list(_____)',
                'correct_answer': ['dict.fromkeys(data)', 'OrderedDict.fromkeys']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How would you create a list of squared numbers from 1 to 10?',
                'options': ['list(x**2 for x in range(1, 11))', 'list(map(lambda x: x**2, range(1, 11)))', '[x**2 for x in range(1, 11)]', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this data transformation create?',
                'code': 'coordinates = [(1, 2), (3, 4), (5, 6)]\nx_coords = list(zip(*coordinates))[0]\nprint(list(x_coords))',
                'options': ['[1, 3, 5]', '[(1, 2), (3, 4), (5, 6)]', '[2, 4, 6]', 'Error'],
                'correct_answer': '[1, 3, 5]'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this CSV row processing:',
                'code': 'csv_row = "John,25,Engineer"\ndata = list(csv_row.split(","))\nage = data[1] + 1',
                'correct_answer': ['int(data[1]) + 1', 'convert age to int', 'age = int(data[1]) + 1']
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To transpose a matrix: transposed = list(zip(*_____)))',
                'correct_answer': ['matrix']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this recursive flattening do?',
                'code': 'def flatten(nested_list):\n    result = []\n    for item in nested_list:\n        if isinstance(item, list):\n            result.extend(flatten(item))\n        else:\n            result.append(item)\n    return result\n\ndata = [1, [2, 3], [4, [5, 6]]]\nflat = flatten(data)\nprint(flat)',
                'options': ['[1, 2, 3, 4, 5, 6]', '[1, [2, 3], [4, [5, 6]]]', '[1, 2, 3, 4]', 'Error'],
                'correct_answer': '[1, 2, 3, 4, 5, 6]'
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'Which approach is most efficient for creating a large list of consecutive numbers?',
                'options': ['list(range(n))', '[i for i in range(n)]', 'list(map(lambda x: x, range(n)))', '[*range(n)]'],
                'correct_answer': 'list(range(n))'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this data aggregation accomplish?',
                'code': 'students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]\nnames = list(zip(*students))[0]\nscores = list(zip(*students))[1]\nprint(f"Average: {sum(scores)/len(scores)}")',
                'options': ['Calculates average score', 'Sorts students by score', 'Finds highest score', 'Validates score format'],
                'correct_answer': 'Calculates average score'
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue does this have?',
                'code': 'def process_large_iterator(data_iterator):\n    all_data = list(data_iterator)  # Could be millions of items\n    for item in all_data:\n        if complex_condition(item):\n            process_item(item)',
                'options': ['Unnecessary memory consumption', 'Slow iteration', 'Poor error handling', 'Type conversion overhead'],
                'correct_answer': 'Unnecessary memory consumption'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'When should you avoid using list() with large iterators?',
                'options': ['Never', 'When memory is limited', 'When speed is important', 'Always'],
                'correct_answer': 'When memory is limited'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What design pattern issue does this reveal?',
                'code': 'def get_user_data():\n    users = get_all_users()  # Returns iterator\n    return list(users)  # Always converts to list\n\ndef process_users():\n    user_list = get_user_data()\n    for user in user_list:  # Could have used iterator directly\n        process_user(user)',
                'options': ['Premature optimization', 'Unnecessary materialization', 'Poor abstraction', 'Memory leak'],
                'correct_answer': 'Unnecessary materialization'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Converting iterators to lists breaks the _____ evaluation benefit.',
                'correct_answer': ['lazy']
            },
            {
                'level': 4,
                'type': 'mix_match',
                'question': 'Match list operations with their time complexities:',
                'left_items': ['list(iterator)', 'list.append()', 'list.insert(0, x)', 'list[i]'],
                'right_items': ['O(1)', 'O(n)', 'O(n)', 'O(1)'],
                'correct_answer': {0: 'O(n)', 1: 'O(1)', 2: 'O(n)', 3: 'O(1)'}
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What memory pattern does this demonstrate?',
                'code': 'def memory_inefficient():\n    # Creating multiple intermediate lists\n    data = list(range(1000000))\n    filtered = list(filter(lambda x: x % 2 == 0, data))\n    mapped = list(map(lambda x: x * 2, filtered))\n    return mapped',
                'options': ['Multiple memory allocations for intermediate results', 'Memory leaks', 'Garbage collection issues', 'Stack overflow'],
                'correct_answer': 'Multiple memory allocations for intermediate results'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the main trade-off when using list() with generators?',
                'options': ['Speed vs readability', 'Memory vs lazy evaluation', 'Type safety vs performance', 'Syntax vs functionality'],
                'correct_answer': 'Memory vs lazy evaluation'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the scalability issue in this code:',
                'code': 'def process_file_lines(filename):\n    with open(filename) as f:\n        all_lines = list(f)  # Loads entire file into memory\n    return process_lines(all_lines)',
                'correct_answer': ['memory issues with large files', 'should process line by line', 'avoid list(f)']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What concurrency issue might this create?',
                'code': 'import threading\n\ndef worker(shared_iterator):\n    local_data = list(shared_iterator)  # Multiple threads consuming same iterator\n    process_data(local_data)',
                'options': ['Iterator consumption race condition', 'Memory corruption', 'Deadlock potential', 'Thread safety violation'],
                'correct_answer': 'Iterator consumption race condition'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'list() creates a _____ copy, which may not copy nested objects deeply.',
                'correct_answer': ['shallow']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Which approach is more memory-efficient for processing large datasets?',
                'options': ['list(process(x) for x in data)', 'process(x) for x in data', '[process(x) for x in data]', 'list(map(process, data))'],
                'correct_answer': 'process(x) for x in data'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance anti-pattern does this show?',
                'code': 'def combine_results(*iterators):\n    combined = []\n    for it in iterators:\n        combined.extend(list(it))  # Converting each iterator to list\n    return combined',
                'options': ['Unnecessary list conversions in loop', 'Poor error handling', 'Type safety issues', 'Infinite loop risk'],
                'correct_answer': 'Unnecessary list conversions in loop'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'The _____ principle suggests keeping data as iterators until materialization is needed.',
                'correct_answer': ['lazy evaluation', 'deferred execution']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the primary reason to avoid list() in data pipelines?',
                'options': ['Syntax complexity', 'Type conversion errors', 'Memory consumption and loss of streaming', 'Poor performance'],
                'correct_answer': 'Memory consumption and loss of streaming'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What architectural issue does this represent?',
                'code': 'class DataProcessor:\n    def __init__(self):\n        self.cache = {}\n    \n    def process(self, data_iterator):\n        data_list = list(data_iterator)  # Forces materialization\n        cache_key = hash(tuple(data_list))  # Expensive operation\n        if cache_key not in self.cache:\n            self.cache[cache_key] = expensive_computation(data_list)\n        return self.cache[cache_key]',
                'options': ['Caching defeats iterator benefits', 'Poor cache design', 'Hash collision risk', 'Thread safety issues'],
                'correct_answer': 'Caching defeats iterator benefits'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced data structure does this implement?',
                'code': 'class LazyList:\n    def __init__(self, iterable):\n        self._iterator = iter(iterable)\n        self._cache = []\n        self._exhausted = False\n    \n    def __getitem__(self, index):\n        self._ensure_index(index)\n        return self._cache[index]\n    \n    def _ensure_index(self, index):\n        while len(self._cache) <= index and not self._exhausted:\n            try:\n                self._cache.append(next(self._iterator))\n            except StopIteration:\n                self._exhausted = True\n                break\n        if index >= len(self._cache):\n            raise IndexError("Index out of range")',
                'options': ['Lazy-loading list with caching', 'Memory-mapped list', 'Compressed list', 'Distributed list'],
                'correct_answer': 'Lazy-loading list with caching'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create an efficient data processing framework, you would combine list() with:',
                'options': ['Simple loops only', 'Streaming iterators, lazy evaluation, and memory management', 'File I/O operations', 'Network protocols'],
                'correct_answer': 'Streaming iterators, lazy evaluation, and memory management'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A sophisticated data pipeline might implement _____ to materialize lists only when necessary.',
                'correct_answer': ['lazy evaluation', 'deferred materialization']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What design pattern does this factory implement?',
                'code': 'class ListFactory:\n    @staticmethod\n    def from_csv(filename):\n        with open(filename) as f:\n            return list(csv.reader(f))\n    \n    @staticmethod\n    def from_json(filename):\n        with open(filename) as f:\n            data = json.load(f)\n            return list(data) if isinstance(data, (list, tuple)) else [data]\n    \n    @staticmethod\n    def from_database(query):\n        cursor = db.execute(query)\n        return list(cursor.fetchall())\n    \n    @staticmethod\n    def from_api(url):\n        response = requests.get(url)\n        return list(response.json())',
                'options': ['Multi-source data list factory', 'Simple file reader', 'Data validator', 'Format converter'],
                'correct_answer': 'Multi-source data list factory'
            },
            {
                'level': 5,
                'type': 'mix_match',
                'question': 'Match advanced list concepts with their applications:',
                'left_items': ['Memory pools', 'Copy-on-write', 'Lazy materialization', 'Chunked processing'],
                'right_items': ['Large dataset handling', 'Efficient copying', 'Memory optimization', 'Deferred evaluation'],
                'correct_answer': {0: 'Memory optimization', 1: 'Efficient copying', 2: 'Deferred evaluation', 3: 'Large dataset handling'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What streaming architecture does this implement?',
                'code': 'class StreamingList:\n    def __init__(self, chunk_size=1000):\n        self.chunk_size = chunk_size\n        self.chunks = []\n        self.current_chunk = []\n    \n    def append(self, item):\n        self.current_chunk.append(item)\n        if len(self.current_chunk) >= self.chunk_size:\n            self.chunks.append(list(self.current_chunk))\n            self.current_chunk = []\n    \n    def materialize(self):\n        result = []\n        for chunk in self.chunks:\n            result.extend(chunk)\n        result.extend(self.current_chunk)\n        return result\n    \n    def stream_process(self, func):\n        for chunk in self.chunks:\n            for item in chunk:\n                yield func(item)\n        for item in self.current_chunk:\n            yield func(item)',
                'options': ['Chunked streaming list processor', 'Simple list wrapper', 'Memory cache', 'Data validator'],
                'correct_answer': 'Chunked streaming list processor'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For building a high-performance data analytics system, list operations would be optimized using:',
                'options': ['Simple Python lists', 'NumPy arrays and vectorized operations', 'String concatenation', 'File systems'],
                'correct_answer': 'NumPy arrays and vectorized operations'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A distributed computing system might use _____ to partition list operations across nodes.',
                'correct_answer': ['sharding', 'partitioning']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What caching strategy does this implement?',
                'code': 'class MemoizedList:\n    def __init__(self, generator_func):\n        self.generator_func = generator_func\n        self.cache = {}\n        self.generation = 0\n    \n    def get_list(self, *args, **kwargs):\n        key = (args, tuple(sorted(kwargs.items())))\n        if key not in self.cache:\n            self.cache[key] = list(self.generator_func(*args, **kwargs))\n        return self.cache[key]\n    \n    def invalidate(self):\n        self.cache.clear()\n        self.generation += 1',
                'options': ['Memoized list generation with cache invalidation', 'Simple caching', 'Data persistence', 'Error recovery'],
                'correct_answer': 'Memoized list generation with cache invalidation'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a memory-efficient machine learning data loader, you would use:',
                'options': ['Large list() conversions', 'Streaming iterators with batch list creation', 'File-based storage only', 'Network protocols'],
                'correct_answer': 'Streaming iterators with batch list creation'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this efficient parallel list processor:',
                'code': 'import multiprocessing\n\nclass ParallelListProcessor:\n    def __init__(self, num_workers=4):\n        self.num_workers = num_workers\n        self.pool = multiprocessing.Pool(num_workers)\n    \n    def process_chunks(self, data, chunk_size, process_func):\n        chunks = [list(data[i:i+chunk_size]) \n                 for i in range(0, len(data), chunk_size)]\n        \n        results = self.pool._____(process_func, chunks)\n        return list(itertools.chain.from_iterable(results))',
                'correct_answer': ['map']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced optimization does this implement?',
                'code': 'class COWList:  # Copy-On-Write List\n    def __init__(self, data=None):\n        self._data = data or []\n        self._refs = 1\n        self._copied = False\n    \n    def _ensure_unique(self):\n        if self._refs > 1 and not self._copied:\n            self._data = list(self._data)\n            self._copied = True\n    \n    def append(self, item):\n        self._ensure_unique()\n        self._data.append(item)\n    \n    def copy(self):\n        new_list = COWList(self._data)\n        self._refs += 1\n        new_list._refs = self._refs\n        return new_list',
                'options': ['Copy-on-write optimization for memory efficiency', 'Thread-safe list', 'Compressed storage', 'Distributed list'],
                'correct_answer': 'Copy-on-write optimization for memory efficiency'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A real-time system might implement _____ lists to handle continuous data streams.',
                'correct_answer': ['circular', 'ring', 'bounded']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For creating a database ORM with efficient list operations, you would implement:',
                'options': ['Simple list conversions', 'Lazy loading, pagination, and query result caching', 'File-based storage', 'Memory mapping only'],
                'correct_answer': 'Lazy loading, pagination, and query result caching'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What scalable architecture does this represent?',
                'code': 'class DistributedList:\n    def __init__(self, nodes):\n        self.nodes = nodes\n        self.local_lists = {node: [] for node in nodes}\n    \n    def append(self, item):\n        # Distribute items across nodes using consistent hashing\n        node = self._get_node(hash(item))\n        self.local_lists[node].append(item)\n    \n    def materialize(self):\n        all_items = []\n        for node in self.nodes:\n            remote_list = self._fetch_from_node(node)\n            all_items.extend(remote_list)\n        return all_items\n    \n    def _get_node(self, hash_value):\n        return self.nodes[hash_value % len(self.nodes)]',
                'options': ['Distributed list with consistent hashing', 'Simple load balancer', 'Cache system', 'Message queue'],
                'correct_answer': 'Distributed list with consistent hashing'
            }
        ]