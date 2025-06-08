# =================================Dictionary Function Quiz Module==================================
# quiz_dict.py - Comprehensive dict() function quiz with 75 questions across 5 Bloom's levels
from quiz_base import QuizBase

class QuizDict(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "dict", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - KNOWLEDGE/REMEMBER (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does dict() without arguments create?',
                'options': ['Empty dictionary', 'Dictionary with None', 'Dictionary with 0', 'Error'],
                'correct_answer': 'Empty dictionary'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is dict(name="Alice", age=25)?',
                'options': ["{'name': 'Alice', 'age': 25}", "('name', 'Alice', 'age', 25)", "['name', 'Alice', 'age', 25]", 'Error'],
                'correct_answer': "{'name': 'Alice', 'age': 25}"
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What type of object does dict() return?',
                'correct_answer': 'dict'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does dict([("a", 1), ("b", 2)]) create?',
                'options': ["{'a': 1, 'b': 2}", "['a', 1, 'b', 2]", "('a', 1, 'b', 2)", 'Error'],
                'correct_answer': "{'a': 1, 'b': 2}"
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'Dictionaries store data as _____ pairs.',
                'correct_answer': ['key-value', 'key value']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is the difference between {} and dict()?',
                'options': ['No difference', '{} is faster', 'dict() is more explicit', 'dict() creates copy'],
                'correct_answer': 'No difference'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What method returns all keys from a dictionary?',
                'correct_answer': 'keys'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which creates a dictionary from keyword arguments?',
                'options': ['dict(a=1, b=2)', 'dict["a"=1, "b"=2]', 'dict{"a": 1, "b": 2}', 'dict<a=1, b=2>'],
                'correct_answer': 'dict(a=1, b=2)'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'Dictionaries are _____, meaning they can be changed after creation.',
                'correct_answer': ['mutable']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does dict({"a": 1, "b": 2}) create?',
                'options': ['Copy of the dictionary', 'Reference to original', 'Nested dictionary', 'Error'],
                'correct_answer': 'Copy of the dictionary'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What method returns all values from a dictionary?',
                'correct_answer': 'values'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does dict.fromkeys(["a", "b"], 0) create?',
                'options': ["{'a': 0, 'b': 0}", "['a', 'b', 0]", "{'a': 'b': 0}", 'Error'],
                'correct_answer': "{'a': 0, 'b': 0}"
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'Dictionary keys must be _____ (unchangeable) objects.',
                'correct_answer': ['immutable', 'hashable']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What method returns key-value pairs as tuples?',
                'options': ['items()', 'pairs()', 'tuples()', 'entries()'],
                'correct_answer': 'items()'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What operator checks if a key exists in a dictionary?',
                'correct_answer': 'in'
            },

            # LEVEL 2 - COMPREHENSION/UNDERSTAND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this code output?',
                'code': 'data = dict(zip(["a", "b", "c"], [1, 2, 3]))\nprint(data)',
                'options': ["{'a': 1, 'b': 2, 'c': 3}", "['a', 1, 'b', 2, 'c', 3]", "[('a', 1), ('b', 2), ('c', 3)]", 'Error'],
                'correct_answer': "{'a': 1, 'b': 2, 'c': 3}"
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why would you use dict() instead of {}?',
                'options': ['Better performance', 'To create from other iterables', 'To create nested dictionaries', 'No reason'],
                'correct_answer': 'To create from other iterables'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'dict() creates a _____ copy of the dictionary.',
                'correct_answer': ['shallow']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this accomplish?',
                'code': 'words = ["apple", "banana", "cherry"]\nword_lengths = dict((word, len(word)) for word in words)\nprint(word_lengths)',
                'options': ["{'apple': 5, 'banana': 6, 'cherry': 6}", "['apple', 5, 'banana', 6, 'cherry', 6]", "[5, 6, 6]", 'Error'],
                'correct_answer': "{'apple': 5, 'banana': 6, 'cherry': 6}"
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What happens when you use dict() with duplicate keys?',
                'options': ['Error occurs', 'All values kept', 'Last value wins', 'First value wins'],
                'correct_answer': 'Last value wins'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this return?',
                'code': 'config = dict(debug=True, port=8080, host="localhost")\nprint(list(config.keys()))',
                'options': ["['debug', 'port', 'host']", "[True, 8080, 'localhost']", "dict_keys(['debug', 'port', 'host'])", 'Error'],
                'correct_answer': "['debug', 'port', 'host']"
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'dict() with keyword arguments creates keys as _____.',
                'correct_answer': ['strings']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the advantage of dict() over manual dictionary creation?',
                'options': ['Faster execution', 'More readable for certain patterns', 'Uses less memory', 'Better type safety'],
                'correct_answer': 'More readable for certain patterns'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this conversion accomplish?',
                'code': 'pairs = [("name", "Alice"), ("age", 30), ("city", "NYC")]\nperson = dict(pairs)\nprint(person["name"])',
                'options': ['Alice', 'name', '("name", "Alice")', 'Error'],
                'correct_answer': 'Alice'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does dict.fromkeys() do differently than dict()?',
                'options': ['Creates from values', 'Creates keys with same value', 'Creates nested dictionaries', 'Creates immutable dict'],
                'correct_answer': 'Creates keys with same value'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'Dictionary comprehensions can be converted to dict() using _____ expressions.',
                'correct_answer': ['generator']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this merging accomplish?',
                'code': 'dict1 = {"a": 1, "b": 2}\ndict2 = {"c": 3, "d": 4}\nmerged = dict(dict1, **dict2)\nprint(merged)',
                'options': ["{'a': 1, 'b': 2, 'c': 3, 'd': 4}", "{'c': 3, 'd': 4}", "{'a': 1, 'b': 2}", 'Error'],
                'correct_answer': "{'a': 1, 'b': 2, 'c': 3, 'd': 4}"
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why are lists not valid dictionary keys?',
                'options': ['Too large', 'Not immutable/hashable', 'Wrong type', 'Syntax error'],
                'correct_answer': 'Not immutable/hashable'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'dict() can accept an iterable of _____ to create key-value mappings.',
                'correct_answer': ['pairs', 'tuples']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this counting pattern create?',
                'code': 'text = "hello"\ncounter = dict((char, text.count(char)) for char in set(text))\nprint(counter)',
                'options': ["{'h': 1, 'e': 1, 'l': 2, 'o': 1}", "{'h': 1, 'e': 1, 'l': 1, 'o': 1}", "[1, 1, 2, 1]", 'Error'],
                'correct_answer': "{'h': 1, 'e': 1, 'l': 2, 'o': 1}"
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this dictionary creation from CSV data:',
                'code': 'csv_row = "name,Alice,age,25"\ndata = csv_row.split(",")\nresult = dict(data)',
                'correct_answer': ['dict(zip(data[::2], data[1::2]))', 'pair up keys and values', 'use zip']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this configuration system create?',
                'code': 'defaults = {"debug": False, "port": 8000}\nuser_config = {"port": 9000, "host": "localhost"}\nfinal_config = dict(defaults, **user_config)\nprint(final_config)',
                'options': ["{'debug': False, 'port': 9000, 'host': 'localhost'}", "{'debug': False, 'port': 8000}", "{'port': 9000, 'host': 'localhost'}", 'Error'],
                'correct_answer': "{'debug': False, 'port': 9000, 'host': 'localhost'}"
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To invert a dictionary (swap keys/values): inverted = dict(_____ for k, v in original.items())',
                'correct_answer': ['(v, k)', 'reversed pairs']
            },
            {
                'level': 3,
                'type': 'mix_match',
                'question': 'Match dictionary creation patterns with their use cases:',
                'left_items': ['dict(zip(keys, values))', 'dict.fromkeys(keys, default)', 'dict(**kwargs)', 'dict(pairs)'],
                'right_items': ['Initialize with same value', 'From keyword arguments', 'From parallel sequences', 'From tuple pairs'],
                'correct_answer': {0: 'From parallel sequences', 1: 'Initialize with same value', 2: 'From keyword arguments', 3: 'From tuple pairs'}
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this grouping function create?',
                'code': 'def group_by_length(words):\n    groups = {}\n    for word in words:\n        length = len(word)\n        if length not in groups:\n            groups[length] = []\n        groups[length].append(word)\n    return groups\n\nresult = group_by_length(["cat", "dog", "elephant", "bee"])\nprint(result)',
                'options': ['{3: ["cat", "dog", "bee"], 8: ["elephant"]}', '{3: ["cat", "dog"], 8: ["elephant"], 3: ["bee"]}', 'Error', '{3: 3, 8: 1}'],
                'correct_answer': '{3: ["cat", "dog", "bee"], 8: ["elephant"]}'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this frequency counter:',
                'code': 'text = "hello world"\nfrequency = dict()\nfor char in text:\n    frequency[char] += 1',
                'correct_answer': ['frequency[char] = frequency.get(char, 0) + 1', 'use get with default', 'initialize with 0']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this data transformation accomplish?',
                'code': 'students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]\nstudent_dict = dict(students)\nprint(student_dict["Bob"])',
                'options': ['92', 'Bob', '("Bob", 92)', 'Error'],
                'correct_answer': '92'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To safely get a value with default: value = dictionary._____(key, default_value)',
                'correct_answer': ['get']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How would you create a dictionary mapping numbers 1-5 to their squares?',
                'options': ['dict((i, i**2) for i in range(1, 6))', '{i: i**2 for i in range(1, 6)}', 'dict(zip(range(1, 6), [i**2 for i in range(1, 6)]))', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this lookup table create?',
                'code': 'grade_scale = dict(zip(range(90, 101), ["A"] * 11))\ngrade_scale.update(dict(zip(range(80, 90), ["B"] * 10)))\nprint(grade_scale[85])',
                'options': ['B', 'A', '85', 'Error'],
                'correct_answer': 'B'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this configuration merger:',
                'code': 'config1 = {"db": "mysql", "port": 3306}\nconfig2 = {"port": 5432, "host": "localhost"}\nmerged = dict(config1 + config2)',
                'correct_answer': ['dict(config1, **config2)', 'use ** to unpack', 'cannot use + with dicts']
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To count occurrences efficiently: from collections import _____',
                'correct_answer': ['Counter']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this caching pattern implement?',
                'code': 'cache = {}\ndef expensive_function(x):\n    if x not in cache:\n        cache[x] = x ** 2 + x * 3 + 1  # Expensive calculation\n    return cache[x]\n\nresult = expensive_function(5)\nprint(result)',
                'options': ['41', '25', '15', 'Error'],
                'correct_answer': '41'
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'Which is the most efficient way to create a dictionary from two lists?',
                'options': ['dict(zip(keys, values))', 'Manual loop with index', '{keys[i]: values[i] for i in range(len(keys))}', 'Using enumerate'],
                'correct_answer': 'dict(zip(keys, values))'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this data pivot accomplish?',
                'code': 'data = [("sales", "Q1", 100), ("sales", "Q2", 150), ("marketing", "Q1", 80)]\npivot = {}\nfor dept, quarter, value in data:\n    if dept not in pivot:\n        pivot[dept] = {}\n    pivot[dept][quarter] = value\nprint(pivot)',
                'options': ["{'sales': {'Q1': 100, 'Q2': 150}, 'marketing': {'Q1': 80}}", "{'Q1': 180, 'Q2': 150}", "[(sales, Q1, 100), ...]", 'Error'],
                'correct_answer': "{'sales': {'Q1': 100, 'Q2': 150}, 'marketing': {'Q1': 80}}"
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue does this have?',
                'code': 'def merge_many_dicts(dict_list):\n    result = {}\n    for d in dict_list:\n        result = dict(result, **d)  # Creates new dict each time\n    return result',
                'options': ['Excessive object creation', 'Memory leaks', 'Key conflicts', 'Type errors'],
                'correct_answer': 'Excessive object creation'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the time complexity of dict() creation from n key-value pairs?',
                'options': ['O(1)', 'O(n)', 'O(n log n)', 'O(n²)'],
                'correct_answer': 'O(n)'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What memory pattern does this demonstrate?',
                'code': 'def inefficient_grouping(items):\n    groups = {}\n    for item in items:\n        key = item.category\n        if key not in groups:\n            groups[key] = []  # Creates new list each time\n        groups[key].append(item)\n    return groups',
                'options': ['Memory fragmentation from many small allocations', 'Memory leaks', 'Stack overflow', 'Garbage collection issues'],
                'correct_answer': 'Memory fragmentation from many small allocations'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Dictionary key _____ determines performance of lookups and insertions.',
                'correct_answer': ['hashing']
            },
            {
                'level': 4,
                'type': 'mix_match',
                'question': 'Match dictionary operations with their time complexities:',
                'left_items': ['dict[key]', 'dict.get(key)', 'key in dict', 'dict.items()'],
                'right_items': ['O(n)', 'O(1)', 'O(1)', 'O(1)'],
                'correct_answer': {0: 'O(1)', 1: 'O(1)', 2: 'O(1)', 3: 'O(n)'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What hash collision issue might this cause?',
                'code': 'class BadHash:\n    def __init__(self, value):\n        self.value = value\n    def __hash__(self):\n        return 1  # All objects have same hash!\n    def __eq__(self, other):\n        return self.value == other.value\n\ndata = dict((BadHash(i), i) for i in range(1000))',
                'options': ['Degraded O(n) performance due to hash collisions', 'Memory corruption', 'Infinite loops', 'Type errors'],
                'correct_answer': 'Degraded O(n) performance due to hash collisions'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why should mutable objects not be used as dictionary keys?',
                'options': ['Performance reasons', 'They are not hashable', 'Memory consumption', 'Syntax limitations'],
                'correct_answer': 'They are not hashable'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the performance anti-pattern:',
                'code': 'def update_config(base_config, updates):\n    for key, value in updates.items():\n        base_config = dict(base_config, **{key: value})  # Inefficient\n    return base_config',
                'correct_answer': ['use update() method', 'base_config.update(updates)', 'avoid recreating dict']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What design flaw does this caching show?',
                'code': 'class Cache:\n    def __init__(self):\n        self.data = dict()\n    \n    def get(self, key, compute_func):\n        if key not in self.data:\n            self.data[key] = compute_func(key)\n        return self.data[key]\n        # No size limit - memory leak potential',
                'options': ['Unbounded cache growth', 'Thread safety issues', 'Hash collision problems', 'Poor error handling'],
                'correct_answer': 'Unbounded cache growth'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Dictionary _____ can cause memory issues if objects have circular references.',
                'correct_answer': ['references', 'values']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Which approach is more memory-efficient for large datasets?',
                'options': ['dict() with all data at once', 'Incremental dict building', 'List of tuples', 'Multiple small dicts'],
                'correct_answer': 'Incremental dict building'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What concurrency issue might this have?',
                'code': 'shared_dict = dict()\n\ndef worker_thread(data):\n    for item in data:\n        key = item.id\n        if key not in shared_dict:  # Race condition here\n            shared_dict[key] = process_item(item)',
                'options': ['Race condition on dictionary modification', 'Deadlock potential', 'Memory corruption', 'Hash table corruption'],
                'correct_answer': 'Race condition on dictionary modification'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Python dictionaries maintain _____ order since Python 3.7.',
                'correct_answer': ['insertion']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the main advantage of dict() over manual iteration for creation?',
                'options': ['Always faster', 'More readable and less error-prone', 'Uses less memory', 'Better type safety'],
                'correct_answer': 'More readable and less error-prone'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What scalability issue does this have?',
                'code': 'def create_lookup_table(large_dataset):\n    lookup = dict()  # No size estimation\n    for item in large_dataset:\n        lookup[item.key] = expensive_transform(item)\n    return lookup\n    # May cause memory exhaustion',
                'options': ['No memory management for large datasets', 'Poor algorithm choice', 'Inefficient data structure', 'Excessive computation'],
                'correct_answer': 'No memory management for large datasets'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced data structure does this implement?',
                'code': 'class MultiDict:\n    def __init__(self):\n        self._data = dict()\n    \n    def add(self, key, value):\n        if key not in self._data:\n            self._data[key] = []\n        self._data[key].append(value)\n    \n    def get_all(self, key):\n        return self._data.get(key, [])\n    \n    def get_first(self, key):\n        values = self._data.get(key, [])\n        return values[0] if values else None\n    \n    def to_dict(self):\n        return dict((k, v[0] if len(v) == 1 else v) for k, v in self._data.items())',
                'options': ['Multi-value dictionary with multiple values per key', 'Nested dictionary structure', 'Thread-safe dictionary', 'Compressed dictionary'],
                'correct_answer': 'Multi-value dictionary with multiple values per key'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a high-performance configuration system, you would combine dict() with:',
                'options': ['Simple key-value storage', 'Layered configs, type validation, and change notification', 'File I/O only', 'String processing'],
                'correct_answer': 'Layered configs, type validation, and change notification'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A sophisticated caching system might implement _____ using custom dict subclasses.',
                'correct_answer': ['LRU eviction', 'cache policies']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What design pattern does this registry implement?',
                'code': 'class ServiceRegistry:\n    def __init__(self):\n        self._services = dict()\n        self._factories = dict()\n    \n    def register_service(self, name, instance):\n        self._services[name] = instance\n    \n    def register_factory(self, name, factory_func):\n        self._factories[name] = factory_func\n    \n    def get_service(self, name):\n        if name in self._services:\n            return self._services[name]\n        elif name in self._factories:\n            instance = self._factories[name]()\n            self._services[name] = instance\n            return instance\n        raise KeyError(f"Service {name} not found")',
                'options': ['Service locator with lazy instantiation', 'Simple factory pattern', 'Observer pattern', 'Command pattern'],
                'correct_answer': 'Service locator with lazy instantiation'
            },
            {
                'level': 5,
                'type': 'mix_match',
                'question': 'Match advanced dictionary concepts with their applications:',
                'left_items': ['WeakValueDict', 'ChainMap', 'OrderedDict', 'defaultdict'],
                'right_items': ['Automatic default values', 'Hierarchical lookups', 'Memory-efficient references', 'Insertion order preservation'],
                'correct_answer': {0: 'Memory-efficient references', 1: 'Hierarchical lookups', 2: 'Insertion order preservation', 3: 'Automatic default values'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What caching strategy does this implement?',
                'code': 'class LRUDict:\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self.data = dict()\n        self.access_order = []\n    \n    def get(self, key):\n        if key in self.data:\n            self.access_order.remove(key)\n            self.access_order.append(key)\n            return self.data[key]\n        return None\n    \n    def put(self, key, value):\n        if len(self.data) >= self.capacity and key not in self.data:\n            oldest = self.access_order.pop(0)\n            del self.data[oldest]\n        \n        if key in self.data:\n            self.access_order.remove(key)\n        else:\n            self.data[key] = value\n        self.access_order.append(key)',
                'options': ['Least Recently Used cache with dict backing', 'Simple cache implementation', 'Memory-mapped storage', 'Distributed cache'],
                'correct_answer': 'Least Recently Used cache with dict backing'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For building a real-time analytics system, dict operations would be optimized using:',
                'options': ['Simple Python dicts', 'Memory-mapped dicts, partitioning, and concurrent access patterns', 'File-based storage', 'Network protocols'],
                'correct_answer': 'Memory-mapped dicts, partitioning, and concurrent access patterns'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A distributed key-value store might implement _____ using consistent hashing.',
                'correct_answer': ['partitioning', 'sharding']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced pattern does this observer system implement?',
                'code': 'class ObservableDict(dict):\n    def __init__(self, *args, **kwargs):\n        super().__init__(*args, **kwargs)\n        self._observers = dict()\n    \n    def observe(self, key, callback):\n        if key not in self._observers:\n            self._observers[key] = []\n        self._observers[key].append(callback)\n    \n    def __setitem__(self, key, value):\n        old_value = self.get(key)\n        super().__setitem__(key, value)\n        \n        if key in self._observers:\n            for callback in self._observers[key]:\n                callback(key, old_value, value)\n    \n    def __delitem__(self, key):\n        old_value = self.get(key)\n        super().__delitem__(key)\n        \n        if key in self._observers:\n            for callback in self._observers[key]:\n                callback(key, old_value, None)',
                'options': ['Observable dictionary with change notifications', 'Thread-safe dictionary', 'Cached dictionary', 'Validated dictionary'],
                'correct_answer': 'Observable dictionary with change notifications'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a database ORM with efficient relationship mapping, you would use:',
                'options': ['Simple dict lookups', 'Lazy-loading dicts, foreign key caching, and relationship graphs', 'File-based storage', 'Array indexing'],
                'correct_answer': 'Lazy-loading dicts, foreign key caching, and relationship graphs'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this thread-safe dictionary implementation:',
                'code': 'import threading\n\nclass ThreadSafeDict:\n    def __init__(self):\n        self._dict = dict()\n        self._lock = threading.RLock()\n    \n    def get(self, key, default=None):\n        with self._____:\n            return self._dict.get(key, default)\n    \n    def set(self, key, value):\n        with self._____:\n            self._dict[key] = value',
                'correct_answer': ['_lock']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What memory optimization does this implement?',
                'code': 'class CompactDict:\n    def __init__(self):\n        self._keys = []\n        self._values = []\n        self._key_index = dict()\n    \n    def __setitem__(self, key, value):\n        if key in self._key_index:\n            index = self._key_index[key]\n            self._values[index] = value\n        else:\n            self._keys.append(key)\n            self._values.append(value)\n            self._key_index[key] = len(self._keys) - 1\n    \n    def __getitem__(self, key):\n        index = self._key_index[key]\n        return self._values[index]\n    \n    def items(self):\n        return zip(self._keys, self._values)',
                'options': ['Memory-efficient dict with separate key/value storage', 'Compressed dictionary', 'Memory-mapped dict', 'Disk-based storage'],
                'correct_answer': 'Memory-efficient dict with separate key/value storage'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A machine learning feature store would use _____ for fast feature lookups.',
                'correct_answer': ['hash tables', 'indexed dicts']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For creating a high-performance web framework routing system, dict() would be used with:',
                'options': ['Simple string matching', 'Trie structures, regex compilation, and method dispatch tables', 'File system operations', 'Database queries'],
                'correct_answer': 'Trie structures, regex compilation, and method dispatch tables'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What distributed system pattern does this implement?',
                'code': 'class ShardedDict:\n    def __init__(self, num_shards=4):\n        self.num_shards = num_shards\n        self.shards = [dict() for _ in range(num_shards)]\n        self.locks = [threading.Lock() for _ in range(num_shards)]\n    \n    def _get_shard(self, key):\n        return hash(key) % self.num_shards\n    \n    def get(self, key):\n        shard_idx = self._get_shard(key)\n        with self.locks[shard_idx]:\n            return self.shards[shard_idx].get(key)\n    \n    def set(self, key, value):\n        shard_idx = self._get_shard(key)\n        with self.locks[shard_idx]:\n            self.shards[shard_idx][key] = value',
                'options': ['Horizontally sharded dictionary for concurrent access', 'Simple load balancer', 'Cache invalidation system', 'Message routing'],
                'correct_answer': 'Horizontally sharded dictionary for concurrent access'
            }
        ]