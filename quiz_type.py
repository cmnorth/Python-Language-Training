# =================================Type Function Quiz Module==================================
# quiz_type.py - Comprehensive type() function quiz with 75 questions across 5 Bloom's levels
from quiz_base import QuizBase

class QuizType(QuizBase):
    def __init__(self, parent_root, user_data):
        super().__init__(parent_root, "type", user_data)

    def get_questions(self):
        return [
            # LEVEL 1 - KNOWLEDGE/REMEMBER (15 questions)
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does the type() function return?',
                'options': ['The value of the object', 'The type object of the argument', 'The size of the object', 'The memory address'],
                'correct_answer': 'The type object of the argument'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is type(5)?',
                'options': ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"],
                'correct_answer': "<class 'int'>"
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What is the type of "Hello"?',
                'correct_answer': 'str'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What does type("Python") return?',
                'options': ["<class 'str'>", "<class 'string'>", "<class 'text'>", "<class 'char'>"],
                'correct_answer': "<class 'str'>"
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'type() is a _____ function in Python.',
                'correct_answer': ['built-in', 'builtin']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is type([1, 2, 3])?',
                'options': ["<class 'list'>", "<class 'array'>", "<class 'sequence'>", "<class 'collection'>"],
                'correct_answer': "<class 'list'>"
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What is the type of 3.14?',
                'correct_answer': 'float'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is type(True)?',
                'options': ["<class 'bool'>", "<class 'boolean'>", "<class 'logical'>", "<class 'binary'>"],
                'correct_answer': "<class 'bool'>"
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'type() helps identify the _____ of a variable.',
                'correct_answer': ['data type', 'type', 'class']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is type({})?',
                'options': ["<class 'dict'>", "<class 'map'>", "<class 'hash'>", "<class 'object'>"],
                'correct_answer': "<class 'dict'>"
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What is the type of None?',
                'correct_answer': 'NoneType'
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'Which is the correct syntax for type()?',
                'options': ['type(object)', 'Type(object)', 'typeof(object)', 'datatype(object)'],
                'correct_answer': 'type(object)'
            },
            {
                'level': 1,
                'type': 'missing_word',
                'question': 'type() returns a _____ object.',
                'correct_answer': ['type', 'class']
            },
            {
                'level': 1,
                'type': 'multiple_choice',
                'question': 'What is type((1, 2, 3))?',
                'options': ["<class 'tuple'>", "<class 'list'>", "<class 'array'>", "<class 'sequence'>"],
                'correct_answer': "<class 'tuple'>"
            },
            {
                'level': 1,
                'type': 'one_word',
                'question': 'What function checks if an object is an instance of a specific type?',
                'correct_answer': 'isinstance'
            },

            # LEVEL 2 - COMPREHENSION/UNDERSTAND (15 questions)
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this code output?',
                'code': 'x = 42\nprint(type(x).__name__)',
                'options': ['42', 'int', "<class 'int'>", 'integer'],
                'correct_answer': 'int'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the difference between type() and isinstance()?',
                'options': ['No difference', 'type() is exact, isinstance() includes inheritance', 'isinstance() is faster', 'type() works with strings only'],
                'correct_answer': 'type() is exact, isinstance() includes inheritance'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'type(x) == int checks for _____ type match.',
                'correct_answer': ['exact', 'precise']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this accomplish?',
                'code': 'if type(user_input) == str:\n    process_text(user_input)',
                'options': ['Validates input is a string', 'Converts to string', 'Checks string length', 'Formats the string'],
                'correct_answer': 'Validates input is a string'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'Why might isinstance(x, int) be preferred over type(x) == int?',
                'options': ['Better performance', 'Handles inheritance properly', 'More readable', 'Works with more types'],
                'correct_answer': 'Handles inheritance properly'
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this return?',
                'code': 'data = [1, "hello", 3.14]\ntypes = [type(item).__name__ for item in data]\nprint(types)',
                'options': ["['int', 'str', 'float']", "['number', 'text', 'decimal']", "['1', 'hello', '3.14']", 'Error'],
                'correct_answer': "['int', 'str', 'float']"
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'type() can be used for _____ in debugging.',
                'correct_answer': ['type checking', 'inspection', 'debugging']
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does type(type) return?',
                'options': ["<class 'type'>", "<class 'function'>", "<class 'builtin'>", "<class 'object'>"],
                'correct_answer': "<class 'type'>"
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What pattern does this demonstrate?',
                'code': 'def debug_variable(var, name):\n    print(f"{name}: {var} (type: {type(var).__name__})")',
                'options': ['Debug logging with type info', 'Variable validation', 'Type conversion', 'Error handling'],
                'correct_answer': 'Debug logging with type info'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What is the relationship between classes and types in Python?',
                'options': ['They are completely different', 'Classes define types', 'Types define classes', 'No relationship'],
                'correct_answer': 'Classes define types'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'In Python, everything is an _____, and every object has a type.',
                'correct_answer': ['object']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What does this type checking accomplish?',
                'code': 'def safe_add(a, b):\n    if type(a) in [int, float] and type(b) in [int, float]:\n        return a + b\n    raise TypeError("Numbers required")',
                'options': ['Ensures numeric addition', 'Converts types', 'Handles strings', 'Optimizes performance'],
                'correct_answer': 'Ensures numeric addition'
            },
            {
                'level': 2,
                'type': 'multiple_choice',
                'question': 'What does type() tell you about an object?',
                'options': ['Its value', 'Its exact class/type', 'Its size', 'Its methods'],
                'correct_answer': 'Its exact class/type'
            },
            {
                'level': 2,
                'type': 'missing_word',
                'question': 'type(obj).__name__ returns the _____ name of the type.',
                'correct_answer': ['string', 'text']
            },
            {
                'level': 2,
                'type': 'snippet_analysis',
                'question': 'What will this comparison return?',
                'code': 'class MyInt(int):\n    pass\n\nx = MyInt(5)\nprint(type(x) == int)',
                'options': ['True', 'False', 'Error', 'None'],
                'correct_answer': 'False'
            },

            # LEVEL 3 - APPLICATION/APPLY (15 questions)
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this type validation:',
                'code': 'if type(data) is "list":\n    process_list(data)',
                'correct_answer': ['type(data) is list', 'remove quotes', 'list not "list"']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this polymorphic function do?',
                'code': 'def process_data(data):\n    if type(data) == list:\n        return sum(data)\n    elif type(data) == str:\n        return len(data)\n    elif type(data) == dict:\n        return len(data.keys())\n    return None',
                'options': ['Handles different data types appropriately', 'Converts all types to numbers', 'Validates data format', 'Sorts different data types'],
                'correct_answer': 'Handles different data types appropriately'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'To check multiple types: if type(x) in [int, float, _____]:',
                'correct_answer': ['complex', 'decimal']
            },
            {
                'level': 3,
                'type': 'mix_match',
                'question': 'Match type checking approaches with their use cases:',
                'left_items': ['type(x) == int', 'isinstance(x, int)', 'hasattr(x, "method")', 'type(x).__name__'],
                'right_items': ['Duck typing', 'Exact type check', 'String comparison', 'Inheritance-aware'],
                'correct_answer': {0: 'Exact type check', 1: 'Inheritance-aware', 2: 'Duck typing', 3: 'String comparison'}
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this input validator create?',
                'code': 'def validate_input(value, expected_type):\n    if type(value) != expected_type:\n        try:\n            return expected_type(value)\n        except:\n            raise ValueError(f"Cannot convert to {expected_type.__name__}")\n    return value',
                'options': ['Type converter with validation', 'Simple type checker', 'Error handler', 'Data formatter'],
                'correct_answer': 'Type converter with validation'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this type-based dispatch:',
                'code': 'handlers = {int: handle_int, str: handle_str}\nhandler = handlers[type(data)]\nhandler(data)',
                'correct_answer': ['handlers.get(type(data))', 'handle missing types', 'use get method']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What design pattern does this implement?',
                'code': 'def serialize(obj):\n    if type(obj) == dict:\n        return json.dumps(obj)\n    elif type(obj) == list:\n        return json.dumps(obj)\n    elif type(obj) == str:\n        return obj\n    else:\n        return str(obj)',
                'options': ['Type-based serialization', 'Data validation', 'Error handling', 'Format conversion'],
                'correct_answer': 'Type-based serialization'
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'Type-based function dispatch uses type() to choose the correct _____.',
                'correct_answer': ['function', 'handler', 'method']
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'How would you create a function that works with multiple numeric types?',
                'options': ['Check each type individually', 'Use isinstance with tuple of types', 'Convert everything to float', 'Use try/except only'],
                'correct_answer': 'Use isinstance with tuple of types'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this debugging helper do?',
                'code': 'def inspect_object(obj):\n    return {\n        "value": obj,\n        "type": type(obj).__name__,\n        "id": id(obj),\n        "methods": [m for m in dir(obj) if not m.startswith("_")]\n    }',
                'options': ['Creates comprehensive object info', 'Validates object structure', 'Converts object format', 'Handles object errors'],
                'correct_answer': 'Creates comprehensive object info'
            },
            {
                'level': 3,
                'type': 'syntax_error',
                'question': 'Fix this type checking condition:',
                'code': 'if type(value) == int or float:\n    return value * 2',
                'correct_answer': ['type(value) in [int, float]', 'isinstance(value, (int, float))', 'proper type check']
            },
            {
                'level': 3,
                'type': 'missing_word',
                'question': 'A type registry pattern uses type() as a _____ to look up handlers.',
                'correct_answer': ['key', 'index']
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this configuration system do?',
                'code': 'def load_config(value):\n    converters = {\n        str: lambda x: x,\n        int: lambda x: int(x),\n        bool: lambda x: x.lower() == "true",\n        list: lambda x: x.split(",")\n    }\n    return converters[type(value)](value)',
                'options': ['Type-aware configuration parsing', 'Data validation', 'String processing', 'Error handling'],
                'correct_answer': 'Type-aware configuration parsing'
            },
            {
                'level': 3,
                'type': 'multiple_choice',
                'question': 'What is the best practice for type checking in function parameters?',
                'options': ['Always use type()', 'Use isinstance() for flexibility', 'Avoid type checking', 'Use string comparisons'],
                'correct_answer': 'Use isinstance() for flexibility'
            },
            {
                'level': 3,
                'type': 'snippet_analysis',
                'question': 'What does this API wrapper accomplish?',
                'code': 'def api_call(endpoint, data):\n    if type(data) == dict:\n        data = json.dumps(data)\n    elif type(data) == list:\n        data = json.dumps(data)\n    elif type(data) != str:\n        data = str(data)\n    return requests.post(endpoint, data=data)',
                'options': ['Normalizes data format for API', 'Validates API endpoints', 'Handles API errors', 'Manages API authentication'],
                'correct_answer': 'Normalizes data format for API'
            },

            # LEVEL 4 - ANALYSIS/ANALYZE (15 questions)
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What design principle does this violate?',
                'code': 'def process_animal(animal):\n    if type(animal) == Dog:\n        return animal.bark()\n    elif type(animal) == Cat:\n        return animal.meow()\n    elif type(animal) == Bird:\n        return animal.chirp()',
                'options': ['Open/Closed Principle', 'Single Responsibility', 'Dependency Inversion', 'Interface Segregation'],
                'correct_answer': 'Open/Closed Principle'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Why is duck typing preferred over explicit type checking in Python?',
                'options': ['Better performance', 'More flexible and extensible code', 'Easier to debug', 'Uses less memory'],
                'correct_answer': 'More flexible and extensible code'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What anti-pattern does this represent?',
                'code': 'def calculate(a, b, operation):\n    if type(a) != int or type(b) != int:\n        raise TypeError("Only integers allowed")\n    if operation == "add":\n        return a + b\n    elif operation == "multiply":\n        return a * b',
                'options': ['Unnecessary type restriction', 'Poor error handling', 'Inefficient operation dispatch', 'Missing validation'],
                'correct_answer': 'Unnecessary type restriction'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Type checking can make code _____ brittle and less reusable.',
                'correct_answer': ['more', 'overly']
            },
            {
                'level': 4,
                'type': 'mix_match',
                'question': 'Match type checking concepts with their implications:',
                'left_items': ['Duck typing', 'Explicit type checks', 'Type annotations', 'Runtime type validation'],
                'right_items': ['Static analysis help', 'Flexible interfaces', 'Security/validation', 'Rigid constraints'],
                'correct_answer': {0: 'Flexible interfaces', 1: 'Rigid constraints', 2: 'Static analysis help', 3: 'Security/validation'}
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What performance issue might this cause?',
                'code': 'def process_large_dataset(data):\n    for item in data:\n        if type(item) == dict:\n            expensive_dict_operation(item)\n        elif type(item) == list:\n            expensive_list_operation(item)',
                'options': ['Repeated type checking overhead', 'Memory leaks', 'Stack overflow', 'Infinite loops'],
                'correct_answer': 'Repeated type checking overhead'
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'When is explicit type checking with type() actually beneficial?',
                'options': ['Always', 'Never', 'For security/validation in critical systems', 'Only for debugging'],
                'correct_answer': 'For security/validation in critical systems'
            },
            {
                'level': 4,
                'type': 'syntax_error',
                'question': 'Identify the architectural flaw in this design:',
                'code': 'class DataProcessor:\n    def process(self, data):\n        if type(data) == UserData:\n            return self.process_user(data)\n        elif type(data) == ProductData:\n            return self.process_product(data)\n        # Need to modify this method for every new type',
                'correct_answer': ['violates open/closed principle', 'not extensible', 'tight coupling']
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What maintainability issue does this create?',
                'code': 'def validate_config(config):\n    for key, value in config.items():\n        if key == "port" and type(value) != int:\n            raise ValueError("Port must be integer")\n        elif key == "host" and type(value) != str:\n            raise ValueError("Host must be string")\n        # ... 50 more specific type checks',
                'options': ['Hard to extend and maintain', 'Poor performance', 'Security vulnerability', 'Memory inefficiency'],
                'correct_answer': 'Hard to extend and maintain'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'Excessive type checking can lead to _____ code that is hard to extend.',
                'correct_answer': ['brittle', 'rigid', 'inflexible']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'What is the main philosophical difference between Python and statically typed languages regarding types?',
                'options': ['Python has no types', 'Python uses duck typing and dynamic dispatch', 'Python is slower', 'Python is less secure'],
                'correct_answer': 'Python uses duck typing and dynamic dispatch'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What design smell does this exhibit?',
                'code': 'def handle_response(response):\n    if type(response) == SuccessResponse:\n        return response.data\n    elif type(response) == ErrorResponse:\n        raise Exception(response.error)\n    elif type(response) == WarningResponse:\n        log_warning(response.message)\n        return response.data',
                'options': ['Type-based conditional logic', 'Poor error handling', 'Missing return values', 'Inefficient processing'],
                'correct_answer': 'Type-based conditional logic'
            },
            {
                'level': 4,
                'type': 'missing_word',
                'question': 'The _____ principle suggests using common interfaces instead of type checking.',
                'correct_answer': ['polymorphism', 'duck typing']
            },
            {
                'level': 4,
                'type': 'multiple_choice',
                'question': 'Which approach is more aligned with Python philosophy?',
                'options': ['if type(obj) == list: process_list(obj)', 'if hasattr(obj, "__iter__"): process_iterable(obj)', 'isinstance(obj, list)', 'obj.__class__ == list'],
                'correct_answer': 'if hasattr(obj, "__iter__"): process_iterable(obj)'
            },
            {
                'level': 4,
                'type': 'snippet_analysis',
                'question': 'What testing challenge does heavy type checking create?',
                'code': 'def process_payment(payment):\n    if type(payment) != CreditCardPayment:\n        raise TypeError("Only credit cards accepted")\n    return payment.charge()',
                'options': ['Difficult to create test doubles/mocks', 'Slow test execution', 'Complex test setup', 'Unreliable test results'],
                'correct_answer': 'Difficult to create test doubles/mocks'
            },

            # LEVEL 5 - SYNTHESIS/CREATE (15 questions)
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced pattern does this type registry implement?',
                'code': 'class TypeRegistry:\n    def __init__(self):\n        self.handlers = {}\n    \n    def register(self, type_class, handler):\n        self.handlers[type_class] = handler\n    \n    def handle(self, obj):\n        handler = self.handlers.get(type(obj))\n        if handler:\n            return handler(obj)\n        # Try parent classes\n        for cls in type(obj).__mro__[1:]:\n            if cls in self.handlers:\n                return self.handlers[cls](obj)\n        raise ValueError(f"No handler for type {type(obj)}")',
                'options': ['Inheritance-aware type dispatch system', 'Simple registry pattern', 'Factory pattern', 'Observer pattern'],
                'correct_answer': 'Inheritance-aware type dispatch system'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a flexible serialization system, you would combine type() with:',
                'options': ['Simple if/else chains', 'Registry pattern and method resolution order', 'String comparisons', 'Exception handling only'],
                'correct_answer': 'Registry pattern and method resolution order'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A metaclass can customize how type() behaves by implementing _____.',
                'correct_answer': ['__new__', '__init__']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced type system does this create?',
                'code': 'class TypeValidator:\n    def __init__(self):\n        self.rules = {}\n    \n    def add_rule(self, type_class, validator_func):\n        self.rules[type_class] = validator_func\n    \n    def validate(self, obj):\n        obj_type = type(obj)\n        if obj_type in self.rules:\n            return self.rules[obj_type](obj)\n        \n        # Check inheritance chain\n        for base_type in obj_type.__mro__:\n            if base_type in self.rules:\n                return self.rules[base_type](obj)\n        \n        return True  # No rules = valid',
                'options': ['Hierarchical validation system', 'Simple type checker', 'Error handling system', 'Data converter'],
                'correct_answer': 'Hierarchical validation system'
            },
            {
                'level': 5,
                'type': 'mix_match',
                'question': 'Match advanced type concepts with their applications:',
                'left_items': ['Metaclasses', 'Type annotations', 'Generic types', 'Protocol classes'],
                'right_items': ['Static analysis', 'Type creation', 'Structural typing', 'Parameterized types'],
                'correct_answer': {0: 'Type creation', 1: 'Static analysis', 2: 'Parameterized types', 3: 'Structural typing'}
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What design pattern does this dynamic dispatcher implement?',
                'code': 'class MethodDispatcher:\n    def __init__(self):\n        self.methods = {}\n    \n    def register(self, *types):\n        def decorator(func):\n            key = tuple(types)\n            self.methods[key] = func\n            return func\n        return decorator\n    \n    def dispatch(self, *args):\n        key = tuple(type(arg) for arg in args)\n        if key in self.methods:\n            return self.methods[key](*args)\n        raise NotImplementedError(f"No method for types {key}")',
                'options': ['Multiple dispatch pattern', 'Factory pattern', 'Command pattern', 'Strategy pattern'],
                'correct_answer': 'Multiple dispatch pattern'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a type-safe API framework, you would primarily use:',
                'options': ['Only type() checks', 'Type hints, runtime validation, and generic types', 'String comparisons', 'Exception handling'],
                'correct_answer': 'Type hints, runtime validation, and generic types'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'Dynamic type creation uses type() as a _____ with three arguments.',
                'correct_answer': ['constructor', 'factory']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What meta-programming technique does this demonstrate?',
                'code': 'def create_typed_class(name, fields, validators):\n    def __init__(self, **kwargs):\n        for field, expected_type in fields.items():\n            value = kwargs.get(field)\n            if value is not None and type(value) != expected_type:\n                raise TypeError(f"{field} must be {expected_type.__name__}")\n            setattr(self, field, value)\n    \n    attrs = {"__init__": __init__}\n    for field, validator in validators.items():\n        attrs[f"validate_{field}"] = validator\n    \n    return type(name, (object,), attrs)',
                'options': ['Dynamic class generation with type validation', 'Simple class factory', 'Data validation system', 'Object serialization'],
                'correct_answer': 'Dynamic class generation with type validation'
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'For building a plugin system with type-based loading, you would use:',
                'options': ['Simple type checks', 'Type registry, inheritance checking, and dynamic loading', 'String matching only', 'File system operations'],
                'correct_answer': 'Type registry, inheritance checking, and dynamic loading'
            },
            {
                'level': 5,
                'type': 'syntax_error',
                'question': 'Complete this type-safe generic container:',
                'code': 'class TypedContainer:\n    def __init__(self, item_type):\n        self.item_type = item_type\n        self.items = []\n    \n    def add(self, item):\n        if _____(item) != self.item_type:\n            raise TypeError(f"Expected {self.item_type}, got {type(item)}")\n        self.items.append(item)',
                'correct_answer': ['type']
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What advanced caching system does this implement?',
                'code': 'class TypeAwareCache:\n    def __init__(self):\n        self.caches = {}\n    \n    def get_cache(self, obj_type):\n        if obj_type not in self.caches:\n            self.caches[obj_type] = {}\n        return self.caches[obj_type]\n    \n    def store(self, key, value):\n        cache = self.get_cache(type(value))\n        cache[key] = value\n    \n    def retrieve(self, key, expected_type):\n        cache = self.get_cache(expected_type)\n        return cache.get(key)',
                'options': ['Type-segregated caching system', 'Simple key-value cache', 'Memory management system', 'Data persistence layer'],
                'correct_answer': 'Type-segregated caching system'
            },
            {
                'level': 5,
                'type': 'missing_word',
                'question': 'A sophisticated ORM would use type() for _____ between Python objects and database types.',
                'correct_answer': ['mapping', 'conversion', 'translation']
            },
            {
                'level': 5,
                'type': 'multiple_choice',
                'question': 'To create a domain-specific language with type checking, you would combine:',
                'options': ['Basic type() calls', 'AST manipulation, type() inspection, and metaclasses', 'String parsing only', 'Regular expressions'],
                'correct_answer': 'AST manipulation, type() inspection, and metaclasses'
            },
            {
                'level': 5,
                'type': 'snippet_analysis',
                'question': 'What architectural pattern does this implement?',
                'code': 'class TypeBasedInjector:\n    def __init__(self):\n        self.providers = {}\n    \n    def register_provider(self, type_class, provider_func):\n        self.providers[type_class] = provider_func\n    \n    def inject(self, target_class):\n        init_signature = inspect.signature(target_class.__init__)\n        dependencies = {}\n        \n        for param_name, param in init_signature.parameters.items():\n            if param.annotation != inspect.Parameter.empty:\n                param_type = param.annotation\n                if param_type in self.providers:\n                    dependencies[param_name] = self.providers[param_type]()\n        \n        return target_class(**dependencies)',
                'options': ['Type-based dependency injection', 'Factory pattern', 'Registry pattern', 'Builder pattern'],
                'correct_answer': 'Type-based dependency injection'
            }
        ]