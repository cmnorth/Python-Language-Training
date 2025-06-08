# =================================Length Function Quiz Module==================================
# quiz_len.py - Comprehensive len() function quiz with 75 questions across 5 Bloom's levels
from quiz_base import QuizBase

class QuizLen(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "len", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - KNOWLEDGE/REMEMBER (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does the len() function return?',
                'options': ['The size in bytes', 'The number of items', 'The data type', 'The memory address'],
                'correct_answer': 'The number of items'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is len("Hello")?',
                'options': ['4', '5', '6', 'Error'],
                'correct_answer': '5'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What data type does len() return?',
                'correct_answer': 'int'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which of these can you use len() with?',
                'options': ['Strings only', 'Lists only', 'Strings and lists', 'All sequences and collections'],
                'correct_answer': 'All sequences and collections'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'len() is a _____ function in Python.',
                'correct_answer': ['built-in', 'builtin']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is len([1, 2, 3, 4])?',
                'options': ['3', '4', '5', '10'],
                'correct_answer': '4'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What does len() count in a string?',
                'correct_answer': 'characters'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is len("")?',
                'options': ['1', '0', 'None', 'Error'],
                'correct_answer': '0'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'len() returns the _____ of a sequence.',
                'correct_answer': ['length', 'size', 'count']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which is the correct syntax for len()?',
                'options': ['length(object)', 'len(object)', 'size(object)', 'count(object)'],
                'correct_answer': 'len(object)'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What does len() count in a list?',
                'correct_answer': 'elements'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is len({1, 2, 3})?',
                'options': ['0', '1', '2', '3'],
                'correct_answer': '3'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'len() works with strings, lists, tuples, and _____.',
                'correct_answer': ['dictionaries', 'sets', 'collections']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What happens when you call len() on a number like len(42)?',
                'options': ['Returns 2', 'Returns 42', 'Causes TypeError', 'Returns None'],
                'correct_answer': 'Causes TypeError'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What does len() count in a dictionary?',
                'correct_answer': 'keys'
            },

            # LEVEL 2 - COMPREHENSION/UNDERSTAND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this code output?',
                'code': 'text = "Python"\nprint(len(text))',
                'options': ['5', '6', '7', 'Error'],
                'correct_answer': '6'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why does len("\\n") return 1?',
                'options': ['\\n is two characters', '\\n is treated as one newline character', 'It\'s an error', 'Backslash is ignored'],
                'correct_answer': '\\n is treated as one newline character'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'len() counts _____ characters, not visual characters.',
                'correct_answer': ['actual', 'individual', 'literal']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this return?',
                'code': 'nested_list = [[1, 2], [3, 4], [5]]\nlen(nested_list)',
                'options': ['5', '3', '6', '2'],
                'correct_answer': '3'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the difference between len(my_list) and my_list.count()?',
                'options': ['No difference', 'len() counts all items, count() needs an argument', 'len() is faster', 'count() is more accurate'],
                'correct_answer': 'len() counts all items, count() needs an argument'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this print?',
                'code': 'data = {"name": "Alice", "age": 25}\nprint(len(data))',
                'options': ['1', '2', '5', 'Error'],
                'correct_answer': '2'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'len() on a dictionary counts the number of _____ pairs.',
                'correct_answer': ['key-value', 'key value']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why might len() be useful in loops?',
                'options': ['To control iteration count', 'To validate data', 'To check for empty collections', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this accomplish?',
                'code': 'if len(user_input) == 0:\n    print("No input provided")',
                'options': ['Checks for empty input', 'Validates input type', 'Counts characters', 'Handles errors'],
                'correct_answer': 'Checks for empty input'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does len() return for range(10)?',
                'options': ['9', '10', '11', 'Error'],
                'correct_answer': '10'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'len() is often used to check if a collection is _____ before processing.',
                'correct_answer': ['empty', 'non-empty']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What pattern does this demonstrate?',
                'code': 'for i in range(len(my_list)):\n    print(f"Item {i}: {my_list[i]}")',
                'options': ['Index-based iteration', 'Value-based iteration', 'Error handling', 'List comprehension'],
                'correct_answer': 'Index-based iteration'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the difference between len() and the __len__() method?',
                'options': ['No difference', 'len() calls __len__() internally', 'len() is faster', '__len__() is deprecated'],
                'correct_answer': 'len() calls __len__() internally'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'Empty collections have a length of _____.',
                'correct_answer': ['0', 'zero']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this validate?',
                'code': 'password = input("Password: ")\nif len(password) < 8:\n    print("Password too short")',
                'options': ['Password strength', 'Password length requirement', 'Password content', 'Password format'],
                'correct_answer': 'Password length requirement'
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this length validation:',
                'code': 'name = input("Name: ")\nif len(name = 0):\n    print("Name required")',
                'correct_answer': ['==', 'double equals', 'len(name) == 0']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this function do?',
                'code': 'def is_valid_length(text, min_len, max_len):\n    return min_len <= len(text) <= max_len',
                'options': ['Validates text length within range', 'Counts characters', 'Formats text', 'Checks text type'],
                'correct_answer': 'Validates text length within range'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To check if a list is not empty: if _____:',
                'correct_answer': ['len(my_list)', 'my_list', 'len(my_list) > 0']
            },
            {
                'level': 3,
                'type': 'mix_match',
                'question': 'Match len() applications with their use cases:',
                'left_items': ['len(password) >= 8', 'len(items) == 0', 'len(data) > 1000', 'len(name.split())'],
                'right_items': ['Count words', 'Check empty', 'Large dataset', 'Password strength'],
                'correct_answer': {0: 'Password strength', 1: 'Check empty', 2: 'Large dataset', 3: 'Count words'}
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this create?',
                'code': 'def truncate_string(text, max_length):\n    if len(text) > max_length:\n        return text[:max_length] + "..."\n    return text',
                'options': ['String shortening function', 'String validation', 'String formatting', 'String encryption'],
                'correct_answer': 'String shortening function'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this list processing:',
                'code': 'for i in range(len(my_list) + 1):\n    print(my_list[i])',
                'correct_answer': ['remove + 1', 'range(len(my_list))', 'off by one error']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this accomplish?',
                'code': 'def get_longest_word(words):\n    longest = ""\n    for word in words:\n        if len(word) > len(longest):\n            longest = word\n    return longest',
                'options': ['Finds word with most characters', 'Counts total characters', 'Validates word list', 'Sorts words'],
                'correct_answer': 'Finds word with most characters'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To iterate with both index and value: for i, item in _____:',
                'correct_answer': ['enumerate(my_list)', 'enumerate']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'Which is more Pythonic for checking empty lists?',
                'options': ['if len(my_list) == 0:', 'if not my_list:', 'if my_list == []:', 'if my_list is None:'],
                'correct_answer': 'if not my_list:'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this pagination logic do?',
                'code': 'def paginate(items, page_size):\n    total_pages = (len(items) + page_size - 1) // page_size\n    return total_pages',
                'options': ['Calculates number of pages needed', 'Divides items into pages', 'Validates page size', 'Counts items per page'],
                'correct_answer': 'Calculates number of pages needed'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this boundary check:',
                'code': 'if index >= 0 and index <= len(my_list):\n    return my_list[index]',
                'correct_answer': ['< len(my_list)', 'index < len(my_list)', 'off by one']
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To safely access the last element: my_list[len(my_list) - _____]',
                'correct_answer': ['1']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this input validation do?',
                'code': 'def validate_input(data, min_items=1, max_items=100):\n    items = data.split(",")\n    if not (min_items <= len(items) <= max_items):\n        raise ValueError("Invalid number of items")\n    return items',
                'options': ['Validates comma-separated input length', 'Splits and formats data', 'Counts commas in input', 'Validates data types'],
                'correct_answer': 'Validates comma-separated input length'
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How would you check if two lists have the same length?',
                'options': ['len(list1) == len(list2)', 'list1.length == list2.length', 'size(list1) == size(list2)', 'count(list1) == count(list2)'],
                'correct_answer': 'len(list1) == len(list2)'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this progress indicator create?',
                'code': 'def show_progress(current, total):\n    percent = (current / len(total)) * 100\n    print(f"Progress: {percent:.1f}%")',
                'options': ['Percentage completion display', 'Item counter', 'Time estimator', 'Error tracker'],
                'correct_answer': 'Percentage completion display'
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue does this code have?',
                'code': 'def process_large_list(items):\n    for i in range(len(items)):\n        if len(items) > 1000:  # Recalculating length each iteration\n            expensive_operation(items[i])',
                'options': ['Redundant length calculation', 'Memory leak', 'Index out of bounds', 'Type conversion error'],
                'correct_answer': 'Redundant length calculation'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the time complexity of len() for most Python collections?',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'correct_answer': 'O(1)'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What design flaw does this reveal?',
                'code': 'def unsafe_access(data, index):\n    if index < len(data):\n        return data[index]\n    return None',
                'options': ['Missing negative index check', 'Inefficient length check', 'Poor error handling', 'Memory waste'],
                'correct_answer': 'Missing negative index check'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Python stores length as an _____ field, making len() very fast.',
                'correct_answer': ['internal', 'cached', 'stored']
            },
            {
                'level': 4,
                'type': 'mix_match',
                'question': 'Match length-related concepts with their implications:',
                'left_items': ['O(1) complexity', 'Length caching', 'Dynamic sizing', 'Memory overhead'],
                'right_items': ['Storage for length info', 'Fast length retrieval', 'List can grow/shrink', 'Constant time access'],
                'correct_answer': {0: 'Constant time access', 1: 'Fast length retrieval', 2: 'List can grow/shrink', 3: 'Storage for length info'}
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What anti-pattern does this demonstrate?',
                'code': 'def find_item(items, target):\n    for i in range(len(items)):\n        if items[i] == target:\n            return i\n    return -1',
                'options': ['Unnecessary index-based iteration', 'Poor variable naming', 'Missing error handling', 'Inefficient search'],
                'correct_answer': 'Unnecessary index-based iteration'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why is "if my_list:" preferred over "if len(my_list) > 0:"?',
                'options': ['Better performance', 'More readable and Pythonic', 'Handles None values', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the logical error in this boundary check:',
                'code': 'def safe_slice(data, start, end):\n    if 0 <= start < len(data) and 0 <= end < len(data):\n        return data[start:end]',
                'correct_answer': ['end can equal len(data)', 'end <= len(data)', 'slice end can be length']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What memory consideration does this highlight?',
                'code': 'def create_chunks(large_list, chunk_size):\n    chunks = []\n    for i in range(0, len(large_list), chunk_size):\n        chunks.append(large_list[i:i+chunk_size])\n    return chunks',
                'options': ['Creates multiple copies of data', 'Efficient memory usage', 'Memory leak risk', 'Optimal performance'],
                'correct_answer': 'Creates multiple copies of data'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Using len() in a loop condition can create _____ when modifying the collection.',
                'correct_answer': ['bugs', 'errors', 'issues']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Which approach is most efficient for checking if a collection has items?',
                'options': ['len(collection) > 0', 'bool(collection)', 'if collection:', 'collection != []'],
                'correct_answer': 'if collection:'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What concurrency issue might this have?',
                'code': 'def process_shared_list(shared_list):\n    for i in range(len(shared_list)):\n        # Another thread might modify shared_list here\n        process_item(shared_list[i])',
                'options': ['Race condition with list modification', 'Deadlock potential', 'Memory corruption', 'Performance degradation'],
                'correct_answer': 'Race condition with list modification'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Generator objects don\'t have a len() because they are _____ computed.',
                'correct_answer': ['lazily', 'dynamically']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the main advantage of Python\'s len() implementation?',
                'options': ['Accuracy', 'Constant time complexity', 'Memory efficiency', 'Type safety'],
                'correct_answer': 'Constant time complexity'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What validation weakness does this show?',
                'code': 'def process_user_data(data):\n    if len(data) > 0:  # Only checks non-empty\n        return process(data)\n    return None',
                'options': ['Missing type validation', 'Inadequate length validation', 'Poor error handling', 'Security vulnerability'],
                'correct_answer': 'Missing type validation'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced data structure does this implement?',
                'code': 'class BoundedList:\n    def __init__(self, max_size):\n        self.max_size = max_size\n        self.items = []\n    \n    def append(self, item):\n        if len(self.items) >= self.max_size:\n            self.items.pop(0)\n        self.items.append(item)\n    \n    def __len__(self):\n        return len(self.items)',
                'options': ['Fixed-size circular buffer', 'Dynamic array', 'Stack implementation', 'Queue implementation'],
                'correct_answer': 'Fixed-size circular buffer'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a smart pagination system, you would combine len() with:',
                'options': ['Simple division', 'Ceiling division and range validation', 'Modulo operations only', 'Basic arithmetic'],
                'correct_answer': 'Ceiling division and range validation'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A custom collection class should implement _____ to work with len().',
                'correct_answer': ['__len__']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What design pattern does this length-aware cache implement?',
                'code': 'class LRUCache:\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self.cache = {}\n        self.access_order = []\n    \n    def get(self, key):\n        if len(self.cache) > self.capacity:\n            oldest = self.access_order.pop(0)\n            del self.cache[oldest]\n        # ... rest of implementation',
                'options': ['Least Recently Used cache', 'Most Recently Used cache', 'First In First Out cache', 'Random replacement cache'],
                'correct_answer': 'Least Recently Used cache'
            },
            {
                'level': 5,
                'type': 'mix_match',
                'question': 'Match advanced len() applications with their domains:',
                'left_items': ['Memory management', 'Data validation', 'Algorithm optimization', 'User interface'],
                'right_items': ['Progress bars', 'Buffer sizing', 'Input constraints', 'Loop optimization'],
                'correct_answer': {0: 'Buffer sizing', 1: 'Input constraints', 2: 'Loop optimization', 3: 'Progress bars'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What adaptive algorithm does this implement?',
                'code': 'class AdaptiveProcessor:\n    def __init__(self):\n        self.batch_size = 10\n    \n    def process(self, data):\n        if len(data) > 1000:\n            self.batch_size = len(data) // 50\n        elif len(data) < 100:\n            self.batch_size = max(1, len(data) // 10)\n        \n        for i in range(0, len(data), self.batch_size):\n            self.process_batch(data[i:i+self.batch_size])',
                'options': ['Dynamic batch processing', 'Load balancing', 'Memory optimization', 'Performance tuning'],
                'correct_answer': 'Dynamic batch processing'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For building a text analysis system, len() would be most useful for:',
                'options': ['Character counting, word limits, and document metrics', 'Spell checking only', 'Grammar analysis only', 'Translation features'],
                'correct_answer': 'Character counting, word limits, and document metrics'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A streaming data processor might use len() to implement _____ window algorithms.',
                'correct_answer': ['sliding', 'fixed', 'moving']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What data structure optimization does this represent?',
                'code': 'class SmartList:\n    def __init__(self):\n        self.data = []\n        self._length = 0\n    \n    def append(self, item):\n        self.data.append(item)\n        self._length += 1\n    \n    def __len__(self):\n        return self._length  # O(1) instead of counting',
                'options': ['Length caching optimization', 'Memory compression', 'Access pattern optimization', 'Type safety enhancement'],
                'correct_answer': 'Length caching optimization'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a distributed system that processes large datasets, len() would help with:',
                'options': ['Data partitioning and load balancing', 'Network communication only', 'Error handling only', 'Security validation'],
                'correct_answer': 'Data partitioning and load balancing'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this efficient bulk processor:',
                'code': 'class BulkProcessor:\n    def process_efficiently(self, data):\n        chunk_size = max(1, len(data) _____ 100)\n        for i in range(0, len(data), chunk_size):\n            self.process_chunk(data[i:i+chunk_size])',
                'correct_answer': ['//', 'floor division']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What machine learning concept does this implement?',
                'code': 'class DatasetSplitter:\n    def split(self, data, train_ratio=0.8):\n        total_len = len(data)\n        train_size = int(total_len * train_ratio)\n        \n        train_data = data[:train_size]\n        test_data = data[train_size:]\n        \n        return train_data, test_data',
                'options': ['Train/test data splitting', 'Feature extraction', 'Model validation', 'Data normalization'],
                'correct_answer': 'Train/test data splitting'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A real-time system might use len() to implement _____ control mechanisms.',
                'correct_answer': ['flow', 'rate', 'buffer']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For building a high-performance database query system, len() would be crucial for:',
                'options': ['Query optimization and result set management', 'Connection pooling only', 'Transaction management only', 'Security validation only'],
                'correct_answer': 'Query optimization and result set management'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What scalability pattern does this implement?',
                'code': 'class ScalableWorker:\n    def __init__(self):\n        self.max_queue_size = 1000\n        self.queue = []\n    \n    def add_task(self, task):\n        if len(self.queue) >= self.max_queue_size:\n            self.spawn_additional_worker()\n        self.queue.append(task)\n    \n    def spawn_additional_worker(self):\n        # Create new worker when queue is full\n        pass',
                'options': ['Auto-scaling based on queue length', 'Load balancing', 'Circuit breaker pattern', 'Bulkhead pattern'],
                'correct_answer': 'Auto-scaling based on queue length'
            }
        ]