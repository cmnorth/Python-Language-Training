# =================================Range Function Quiz Module==================================
# quiz_range.py - Comprehensive range() function quiz with 75 questions across 5 Bloom's levels
from quiz_base import QuizBase

class QuizRange(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "range", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - KNOWLEDGE/REMEMBER (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does range(5) generate?',
                'options': ['Numbers 1 to 5', 'Numbers 0 to 4', 'Numbers 0 to 5', 'Numbers 1 to 4'],
                'correct_answer': 'Numbers 0 to 4'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What type of object does range() return?',
                'options': ['List', 'Tuple', 'Range object', 'Iterator'],
                'correct_answer': 'Range object'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What is the starting value of range(10)?',
                'correct_answer': '0'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'How many parameters can range() accept?',
                'options': ['1 only', '2 only', '1, 2, or 3', '3 only'],
                'correct_answer': '1, 2, or 3'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'range(start, stop, _____) allows you to specify the increment.',
                'correct_answer': ['step']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is range(2, 8)?',
                'options': ['Numbers 2 to 8', 'Numbers 2 to 7', 'Numbers 3 to 8', 'Numbers 3 to 7'],
                'correct_answer': 'Numbers 2 to 7'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What is the default step value in range()?',
                'correct_answer': '1'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which parameter is required in range()?',
                'options': ['start', 'stop', 'step', 'All parameters'],
                'correct_answer': 'stop'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'range() is commonly used with _____ loops.',
                'correct_answer': ['for']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does range(0) return?',
                'options': ['[0]', 'Empty range', '0', 'Error'],
                'correct_answer': 'Empty range'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What value is NOT included in range(1, 5)?',
                'correct_answer': '5'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is the syntax for range with all three parameters?',
                'options': ['range(start, stop, step)', 'range(stop, start, step)', 'range(step, start, stop)', 'range(start, step, stop)'],
                'correct_answer': 'range(start, stop, step)'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'range() generates _____ numbers by default.',
                'correct_answer': ['integer', 'whole']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which is a valid range() call?',
                'options': ['range(1.5, 5.5)', 'range("1", "5")', 'range(1, 5)', 'range([1, 5])'],
                'correct_answer': 'range(1, 5)'
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What function converts a range to a list?',
                'correct_answer': 'list'
            },

            # LEVEL 2 - COMPREHENSION/UNDERSTAND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this code print?',
                'code': 'for i in range(3):\n    print(i)',
                'options': ['1 2 3', '0 1 2', '1 2', '0 1 2 3'],
                'correct_answer': '0 1 2'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why is range() memory efficient compared to creating a list?',
                'options': ['It stores all values', 'It generates values on demand', 'It uses compression', 'It uses less syntax'],
                'correct_answer': 'It generates values on demand'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'range() is a _____ object that generates values when needed.',
                'correct_answer': ['lazy', 'generator-like', 'iterable']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this produce?',
                'code': 'list(range(2, 10, 3))',
                'options': ['[2, 5, 8]', '[2, 5, 8, 11]', '[3, 6, 9]', '[2, 4, 6, 8]'],
                'correct_answer': '[2, 5, 8]'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What happens with range(10, 2)?',
                'options': ['Counts down from 10 to 2', 'Returns empty range', 'Causes error', 'Returns [10, 2]'],
                'correct_answer': 'Returns empty range'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this output?',
                'code': 'print(len(range(5, 15)))',
                'options': ['10', '11', '9', '15'],
                'correct_answer': '10'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'To count backwards, use a _____ step value.',
                'correct_answer': ['negative']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the purpose of the step parameter?',
                'options': ['Set starting point', 'Set ending point', 'Set increment/decrement', 'Set total count'],
                'correct_answer': 'Set increment/decrement'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this create?',
                'code': 'list(range(10, 0, -2))',
                'options': ['[10, 8, 6, 4, 2]', '[10, 8, 6, 4, 2, 0]', '[8, 6, 4, 2]', 'Empty list'],
                'correct_answer': '[10, 8, 6, 4, 2]'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'How do you check if a number is in a range?',
                'options': ['Use in operator', 'Use == operator', 'Use range.contains()', 'Convert to list first'],
                'correct_answer': 'Use in operator'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'range() objects are _____, meaning you can iterate over them multiple times.',
                'correct_answer': ['reusable', 'persistent']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What pattern does this demonstrate?',
                'code': 'for i in range(len(my_list)):\n    print(f"Index {i}: {my_list[i]}")',
                'options': ['Index-based iteration', 'Value-based iteration', 'Range validation', 'List comprehension'],
                'correct_answer': 'Index-based iteration'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What advantage does range() have over manual list creation?',
                'options': ['Faster execution', 'Lower memory usage', 'Better readability', 'All of the above'],
                'correct_answer': 'All of the above'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'range(start, stop) generates numbers from start up to but not _____ stop.',
                'correct_answer': ['including']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this accomplish?',
                'code': 'even_numbers = list(range(0, 20, 2))',
                'options': ['Creates list of even numbers 0-18', 'Creates list of odd numbers', 'Creates list 0-20', 'Creates empty list'],
                'correct_answer': 'Creates list of even numbers 0-18'
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this countdown range:',
                'code': 'for i in range(10, 0):\n    print(i)',
                'correct_answer': ['range(10, 0, -1)', 'add step -1', 'negative step needed']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this list processing create?',
                'code': 'data = ["a", "b", "c", "d"]\nfor i in range(0, len(data), 2):\n    print(data[i])',
                'options': ['Prints every second element', 'Prints all elements', 'Prints first two elements', 'Causes index error'],
                'correct_answer': 'Prints every second element'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To iterate over indices of a list: for i in range(len(_____)):',
                'correct_answer': ['my_list', 'list_name']
            },
            {
                'level': 3,
                'type': 'mix_match',
                'question': 'Match range patterns with their applications:',
                'left_items': ['range(len(list))', 'range(0, 100, 10)', 'range(10, 0, -1)', 'range(1, n+1)'],
                'right_items': ['Natural numbers 1 to n', 'Index iteration', 'Countdown sequence', 'Multiples of 10'],
                'correct_answer': {0: 'Index iteration', 1: 'Multiples of 10', 2: 'Countdown sequence', 3: 'Natural numbers 1 to n'}
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this nested loop create?',
                'code': 'for row in range(3):\n    for col in range(3):\n        print(f"({row},{col})", end=" ")\n    print()',
                'options': ['3x3 coordinate grid', 'List of numbers', 'Single row output', 'Error'],
                'correct_answer': '3x3 coordinate grid'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this range for odd numbers 1-9:',
                'code': 'odd_numbers = list(range(1, 10, 1))',
                'correct_answer': ['range(1, 10, 2)', 'step should be 2', 'use step 2 for odds']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this batch processing do?',
                'code': 'data = list(range(100))\nfor i in range(0, len(data), 10):\n    batch = data[i:i+10]\n    process_batch(batch)',
                'options': ['Processes data in chunks of 10', 'Processes every 10th item', 'Validates data format', 'Sorts the data'],
                'correct_answer': 'Processes data in chunks of 10'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To skip every nth item: for i in range(0, len(data), _____):',
                'correct_answer': ['n']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How do you create a range of multiples of 5 from 5 to 50?',
                'options': ['range(5, 50, 5)', 'range(5, 55, 5)', 'range(1, 10) * 5', 'range(5, 51, 5)'],
                'correct_answer': 'range(5, 55, 5)'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this enumeration alternative do?',
                'code': 'items = ["apple", "banana", "cherry"]\nfor i in range(len(items)):\n    print(f"{i}: {items[i]}")',
                'options': ['Creates indexed output like enumerate', 'Sorts the items', 'Counts the items', 'Validates the items'],
                'correct_answer': 'Creates indexed output like enumerate'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this matrix initialization:',
                'code': 'matrix = [[0 for j in range(3)] for i in range(3)]\nprint(matrix[4][0])',
                'correct_answer': ['index 4 out of range', 'use index 0-2', 'matrix only has indices 0-2']
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To iterate in reverse order: for i in range(len(list)-1, -1, _____):',
                'correct_answer': ['-1']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this progress indicator create?',
                'code': 'total = 100\nfor i in range(0, total, 10):\n    percent = (i / total) * 100\n    print(f"Progress: {percent}%")',
                'options': ['Progress updates every 10%', 'Complete progress bar', 'Error checking', 'Data validation'],
                'correct_answer': 'Progress updates every 10%'
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'Which is more efficient for large sequences?',
                'options': ['[i for i in range(1000000)]', 'list(range(1000000))', 'range(1000000)', 'tuple(range(1000000))'],
                'correct_answer': 'range(1000000)'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this sliding window create?',
                'code': 'data = [1, 2, 3, 4, 5]\nwindow_size = 3\nfor i in range(len(data) - window_size + 1):\n    window = data[i:i+window_size]\n    print(window)',
                'options': ['Overlapping subsequences of size 3', 'Non-overlapping chunks', 'Reversed sequences', 'Sorted sequences'],
                'correct_answer': 'Overlapping subsequences of size 3'
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue does this have?',
                'code': 'def inefficient_search(data, target):\n    for i in list(range(len(data))):\n        if data[i] == target:\n            return i\n    return -1',
                'options': ['Unnecessary list conversion of range', 'Inefficient search algorithm', 'Missing error handling', 'Poor variable naming'],
                'correct_answer': 'Unnecessary list conversion of range'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the time complexity of creating range(n)?',
                'options': ['O(1)', 'O(n)', 'O(log n)', 'O(n²)'],
                'correct_answer': 'O(1)'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What memory advantage does this demonstrate?',
                'code': 'large_range = range(10**9)  # One billion numbers\nprint(f"Memory efficient: {large_range}")',
                'options': ['Range uses constant memory regardless of size', 'Range compresses the data', 'Range uses disk storage', 'Range samples the data'],
                'correct_answer': 'Range uses constant memory regardless of size'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'range() implements the _____ pattern by generating values on demand.',
                'correct_answer': ['lazy evaluation', 'iterator']
            },
            {
                'level': 4,
                'type': 'mix_match',
                'question': 'Match range optimizations with their benefits:',
                'left_items': ['Lazy evaluation', 'Constant memory', 'Fast membership testing', 'Arithmetic progression'],
                'right_items': ['Mathematical calculation', 'No storage overhead', 'Values generated on-demand', 'O(1) containment check'],
                'correct_answer': {0: 'Values generated on-demand', 1: 'No storage overhead', 2: 'O(1) containment check', 3: 'Mathematical calculation'}
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What algorithmic insight does this reveal?',
                'code': 'def is_in_range(value, start, stop, step=1):\n    if step > 0:\n        return start <= value < stop and (value - start) % step == 0\n    elif step < 0:\n        return stop < value <= start and (start - value) % (-step) == 0\n    return False',
                'options': ['Range membership is calculable without iteration', 'Range requires linear search', 'Range needs sorting first', 'Range membership is random'],
                'correct_answer': 'Range membership is calculable without iteration'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why is "for i in range(len(list))" sometimes considered non-Pythonic?',
                'options': ['It\'s inefficient', 'Direct iteration is more readable', 'It causes errors', 'It uses more memory'],
                'correct_answer': 'Direct iteration is more readable'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the performance anti-pattern:',
                'code': 'def process_items(items):\n    indices = list(range(len(items)))\n    for i in indices:\n        process(items[i])',
                'correct_answer': ['unnecessary list conversion', 'use range directly', 'avoid list(range())']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What design principle does this violate?',
                'code': 'def create_sequence(n):\n    if n < 1000:\n        return list(range(n))  # Small: use list\n    else:\n        return range(n)        # Large: use range\n    # Inconsistent return types',
                'options': ['Consistent interface principle', 'Single responsibility', 'Open/closed principle', 'Dependency inversion'],
                'correct_answer': 'Consistent interface principle'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Range objects are _____ but not generators, so they can be reused.',
                'correct_answer': ['immutable', 'reusable']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the main trade-off of range\'s lazy evaluation?',
                'options': ['Memory for speed', 'Speed for memory', 'Computation time for memory savings', 'Accuracy for performance'],
                'correct_answer': 'Computation time for memory savings'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What concurrency consideration does this highlight?',
                'code': 'def parallel_process(data):\n    indices = range(len(data))\n    # Multiple threads accessing same range object\n    for i in indices:\n        worker_thread(data[i])',
                'options': ['Range objects are thread-safe for reading', 'Range objects need locking', 'Range objects cause race conditions', 'Range objects are not thread-safe'],
                'correct_answer': 'Range objects are thread-safe for reading'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Range\'s _____ testing is O(1) because it uses mathematical calculation.',
                'correct_answer': ['membership', 'containment']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'When might converting range to list be justified?',
                'options': ['Never', 'When you need random access patterns', 'Always for performance', 'Only for small ranges'],
                'correct_answer': 'When you need random access patterns'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What scalability issue might this cause?',
                'code': 'def process_large_dataset(size):\n    all_indices = list(range(size))  # size could be billions\n    random.shuffle(all_indices)\n    for i in all_indices:\n        process_item(i)',
                'options': ['Memory exhaustion from list creation', 'CPU bottleneck', 'I/O limitations', 'Network congestion'],
                'correct_answer': 'Memory exhaustion from list creation'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced iteration pattern does this implement?',
                'code': 'class SteppedRange:\n    def __init__(self, start, stop, step_func):\n        self.start = start\n        self.stop = stop\n        self.step_func = step_func\n    \n    def __iter__(self):\n        current = self.start\n        while current < self.stop:\n            yield current\n            current = self.step_func(current)\n    \n    def __contains__(self, value):\n        current = self.start\n        while current < self.stop:\n            if current == value:\n                return True\n            current = self.step_func(current)\n        return False',
                'options': ['Dynamic step range with custom progression', 'Simple arithmetic sequence', 'Random number generator', 'Fixed step iterator'],
                'correct_answer': 'Dynamic step range with custom progression'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a memory-efficient data processing pipeline for massive datasets, you would use:',
                'options': ['Lists with range indices', 'Range objects with generators and lazy evaluation', 'Arrays with range', 'Tuples with range'],
                'correct_answer': 'Range objects with generators and lazy evaluation'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A sophisticated numeric library might implement _____ for non-integer sequences.',
                'correct_answer': ['numpy.arange', 'linspace', 'floating ranges']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What optimization technique does this parallel processing implement?',
                'code': 'import multiprocessing\ndef parallel_range_process(data, num_workers=4):\n    chunk_size = len(data) // num_workers\n    processes = []\n    \n    for i in range(num_workers):\n        start_idx = i * chunk_size\n        end_idx = start_idx + chunk_size if i < num_workers - 1 else len(data)\n        process = multiprocessing.Process(\n            target=worker,\n            args=(data, range(start_idx, end_idx))\n        )\n        processes.append(process)\n        process.start()',
                'options': ['Work partitioning using range slicing', 'Load balancing', 'Memory optimization', 'Error handling'],
                'correct_answer': 'Work partitioning using range slicing'
            },
            {
                'level': 5,
                'type': 'mix_match',
                'question': 'Match advanced range applications with their domains:',
                'left_items': ['Batch processing', 'Signal processing', 'Graphics programming', 'Machine learning'],
                'right_items': ['Pixel coordinates', 'Sample indices', 'Mini-batch creation', 'Chunk boundaries'],
                'correct_answer': {0: 'Chunk boundaries', 1: 'Sample indices', 2: 'Pixel coordinates', 3: 'Mini-batch creation'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What mathematical concept does this range-based algorithm implement?',
                'code': 'def sieve_of_eratosthenes(limit):\n    is_prime = [True] * limit\n    is_prime[0] = is_prime[1] = False\n    \n    for i in range(2, int(limit**0.5) + 1):\n        if is_prime[i]:\n            for j in range(i*i, limit, i):\n                is_prime[j] = False\n    \n    return [i for i in range(limit) if is_prime[i]]',
                'options': ['Prime number sieve algorithm', 'Sorting algorithm', 'Search algorithm', 'Graph traversal'],
                'correct_answer': 'Prime number sieve algorithm'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For building a high-performance numerical computing library, range() concepts would be extended to:',
                'options': ['Simple integer sequences', 'Multi-dimensional arrays with vectorized operations', 'String processing', 'File I/O operations'],
                'correct_answer': 'Multi-dimensional arrays with vectorized operations'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A distributed computing system might use range() for _____ distribution across nodes.',
                'correct_answer': ['task', 'work', 'data']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced data structure does this implement?',
                'code': 'class LazyMatrix:\n    def __init__(self, rows, cols, init_func):\n        self.rows = rows\n        self.cols = cols\n        self.init_func = init_func\n        self._cache = {}\n    \n    def __getitem__(self, pos):\n        row, col = pos\n        if pos not in self._cache:\n            if 0 <= row < self.rows and 0 <= col < self.cols:\n                self._cache[pos] = self.init_func(row, col)\n            else:\n                raise IndexError("Matrix index out of range")\n        return self._cache[pos]\n    \n    def get_row(self, row):\n        return [self[row, col] for col in range(self.cols)]',
                'options': ['Lazy-evaluated matrix with range-based indexing', 'Dense matrix storage', 'Sparse matrix implementation', 'Fixed-size array'],
                'correct_answer': 'Lazy-evaluated matrix with range-based indexing'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create an efficient time series processing system, you would combine range() with:',
                'options': ['Simple loops only', 'Sliding windows, batch processing, and memory mapping', 'String operations', 'File handling only'],
                'correct_answer': 'Sliding windows, batch processing, and memory mapping'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this efficient matrix multiplication using range:',
                'code': 'def matrix_multiply(A, B):\n    rows_A, cols_A = len(A), len(A[0])\n    rows_B, cols_B = len(B), len(B[0])\n    \n    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]\n    \n    for i in range(_____):  # rows of result\n        for j in range(_____):  # cols of result\n            for k in range(_____):  # inner dimension\n                result[i][j] += A[i][k] * B[k][j]\n    \n    return result',
                'correct_answer': ['rows_A, cols_B, cols_A']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What caching strategy does this range-based system implement?',
                'code': 'class ChunkedProcessor:\n    def __init__(self, data, chunk_size=1000):\n        self.data = data\n        self.chunk_size = chunk_size\n        self.cache = {}\n    \n    def get_chunk(self, chunk_id):\n        if chunk_id not in self.cache:\n            start = chunk_id * self.chunk_size\n            end = min(start + self.chunk_size, len(self.data))\n            self.cache[chunk_id] = self.data[start:end]\n        return self.cache[chunk_id]\n    \n    def process_range(self, start_chunk, end_chunk):\n        results = []\n        for chunk_id in range(start_chunk, end_chunk):\n            chunk = self.get_chunk(chunk_id)\n            results.extend(self.process_chunk(chunk))\n        return results',
                'options': ['Chunk-based lazy loading with range navigation', 'Simple caching system', 'Memory optimization only', 'Error handling system'],
                'correct_answer': 'Chunk-based lazy loading with range navigation'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A GPU computing framework would use range concepts for _____ parallelization.',
                'correct_answer': ['thread', 'block', 'grid']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For creating a database query optimizer, range() concepts would help with:',
                'options': ['SQL parsing only', 'Index range scans and partition pruning', 'Connection pooling', 'Transaction management'],
                'correct_answer': 'Index range scans and partition pruning'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What distributed algorithm pattern does this implement?',
                'code': 'class DistributedRange:\n    def __init__(self, total_size, num_nodes, node_id):\n        self.total_size = total_size\n        self.num_nodes = num_nodes\n        self.node_id = node_id\n        \n        # Calculate this node\'s range\n        chunk_size = total_size // num_nodes\n        remainder = total_size % num_nodes\n        \n        if node_id < remainder:\n            self.start = node_id * (chunk_size + 1)\n            self.end = self.start + chunk_size + 1\n        else:\n            self.start = remainder * (chunk_size + 1) + (node_id - remainder) * chunk_size\n            self.end = self.start + chunk_size\n    \n    def get_local_range(self):\n        return range(self.start, self.end)',
                'options': ['Load-balanced range partitioning for distributed systems', 'Simple data copying', 'Error recovery system', 'Message passing protocol'],
                'correct_answer': 'Load-balanced range partitioning for distributed systems'
            }
        ]