# Python Interview Questions and Answers

## Table of Contents
1. [Language Fundamentals](#language-fundamentals)
2. [Data Types and Operations](#data-types-and-operations)
3. [Control Flow](#control-flow)
4. [Functions](#functions)
5. [Object-Oriented Programming](#object-oriented-programming)
6. [Advanced Concepts](#advanced-concepts)

---

## Language Fundamentals

### 1. Is Python a compiled language or an interpreted language?

**Answer:** Python is both compiled and interpreted, but in different stages:

- **Compilation Stage**: Python source code (.py files) is first compiled into bytecode (.pyc files)
- **Interpretation Stage**: The Python Virtual Machine (PVM) interprets and executes this bytecode line-by-line

**Example:**
```python
# When you run this file, Python first compiles it to bytecode
print("Hello, World!")  # Then PVM interprets and executes it
```

### 2. What is a dynamically typed language?

**Answer:** In dynamically typed languages, variable data types are determined at runtime, not compile time. You don't need to declare data types manually.

**Example:**
```python
x = 10        # x is an integer
x = "Hello"   # Now x is a string
x = [1, 2, 3] # Now x is a list
```

### 3. Is indentation required in Python?

**Answer:** Yes, indentation is mandatory in Python. It defines code blocks and structure, unlike other languages that use curly braces `{}`.

**Example:**
```python
if True:
    print("This is indented")  # 4 spaces or 1 tab
    if True:
        print("This is double indented")  # 8 spaces or 2 tabs
```

---

## Data Types and Operations

### 4. How can you concatenate two lists in Python?

**Answer:** There are two main ways:

**Method 1: Using + operator (creates new list)**
```python
a = [1, 2, 3]
b = [4, 5, 6]
result = a + b
print(result)  # [1, 2, 3, 4, 5, 6]
```

**Method 2: Using extend() method (modifies original list)**
```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]
```

### 5. What is the difference between / and // in Python?

**Answer:**
- `/` performs precise division (returns float)
- `//` performs floor division (returns integer)

**Example:**
```python
print(5 / 2)   # 2.5 (float division)
print(5 // 2)  # 2 (floor division)
print(7 / 3)   # 2.333...
print(7 // 3)  # 2
```

### 6. How do you floor a number in Python?

**Answer:** Use `math.floor()` function to get the largest integer less than or equal to the given number.

**Example:**
```python
import math

print(math.floor(3.7))   # 3
print(math.floor(-2.3))  # -3
print(math.ceil(3.2))    # 4 (ceiling function)
```

---

## Control Flow

### 7. Difference between for loop and while loop in Python

**Answer:**
- **For loop**: Used when you know the number of iterations or iterating over sequences
- **While loop**: Used when you have a condition to check and don't know exact iterations

**Example:**
```python
# For loop - known iterations
for i in range(5):
    print(f"For loop: {i}")

# While loop - condition-based
count = 0
while count < 5:
    print(f"While loop: {count}")
    count += 1
```

### 8. What is `pass` in Python?

**Answer:** `pass` is a placeholder statement that does nothing. It's used when syntax requires a statement but no action is needed.

**Example:**
```python
def future_function():
    pass  # Will implement later

class EmptyClass:
    pass  # Placeholder class

for i in range(5):
    if i == 3:
        pass  # Do nothing for i=3
    else:
        print(i)
```

---

## Functions

### 9. Can we pass a function as an argument in Python?

**Answer:** Yes, functions are objects in Python and can be passed as arguments to other functions. This creates higher-order functions.

**Example:**
```python
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def apply_operation(func, a, b):
    return func(a, b)

result1 = apply_operation(add, 5, 3)       # 8
result2 = apply_operation(multiply, 5, 3)  # 15
```

### 10. How are arguments passed by value or by reference in Python?

**Answer:** Python uses "Pass by Object Reference":
- **Immutable objects** (int, string, tuple): Behave like pass-by-value
- **Mutable objects** (list, dict, set): Behave like pass-by-reference

**Example:**
```python
def modify_immutable(x):
    x = x * 2
    return x

def modify_mutable(lst):
    lst.append("new item")
    return lst

# Immutable example
num = 5
result = modify_immutable(num)
print(f"Original: {num}, Result: {result}")  # Original: 5, Result: 10

# Mutable example
my_list = [1, 2, 3]
modify_mutable(my_list)
print(my_list)  # [1, 2, 3, 'new item'] - original list modified
```

### 11. What is a lambda function?

**Answer:** Lambda functions are anonymous functions that can have multiple parameters but only one expression. They're useful for short, simple functions.

**Example:**
```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))         # 25
print(square_lambda(5))  # 25

# Lambda with multiple parameters
add = lambda x, y: x + y
print(add(3, 5))  # 8

# Lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

---

## Advanced Concepts

### 12. What is List Comprehension? Give an Example.

**Answer:** List comprehension provides a concise way to create lists using a single line of code. It's more readable and often faster than traditional loops.

**Syntax:** `[expression for item in iterable if condition]`

**Example:**
```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# String manipulation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']
```

### 13. What is the difference between `remove()`, `del`, and `pop()` in Python?

**Answer:**

- **`remove()`**: Removes first occurrence of a value
- **`del`**: Removes item at specific index or deletes entire object
- **`pop()`**: Removes and returns item at specific index (last by default)

**Example:**
```python
my_list = [1, 2, 3, 2, 4]

# remove() - removes first occurrence of value
my_list.remove(2)
print(my_list)  # [1, 3, 2, 4]

# pop() - removes and returns item at index
my_list = [1, 2, 3, 4, 5]
popped = my_list.pop(2)  # removes index 2
print(f"Popped: {popped}, List: {my_list}")  # Popped: 3, List: [1, 2, 4, 5]

# del - deletes item at index
my_list = [1, 2, 3, 4, 5]
del my_list[1]  # removes index 1
print(my_list)  # [1, 3, 4, 5]
```

### 14. What are `*args` and `**kwargs` in Python?

**Answer:**
- **`*args`**: Allows function to accept variable number of positional arguments
- **`**kwargs`**: Allows function to accept variable number of keyword arguments

**Example:**
```python
def example_function(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

example_function(1, 2, 3, name="John", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'John', 'age': 25}

# Practical example
def calculate_sum(*numbers):
    return sum(numbers)

print(calculate_sum(1, 2, 3, 4, 5))  # 15

def create_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=30, city="New York")
```

### 15. What is the difference between `is` and `==` in Python?

**Answer:**
- **`==`**: Compares values (equality)
- **`is`**: Compares object identity (same object in memory)

**Example:**
```python
# Value comparison with ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different objects)

# Identity comparison with is
c = a
print(a is c)  # True (same object)

# Special case with small integers and strings
x = 5
y = 5
print(x is y)  # True (Python caches small integers)

# None comparison (always use 'is')
value = None
print(value is None)  # Correct way
print(value == None)  # Works but not recommended
```

### 16. What are generators in Python?

**Answer:** Generators are functions that return an iterator object. They use `yield` instead of `return` and generate values on-demand, making them memory efficient.

**Example:**
```python
# Generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5

# Generator expression
squares = (x**2 for x in range(5))
print(list(squares))  # [0, 1, 4, 9, 16]
```

### 17. What is the difference between `append()` and `extend()` in Python?

**Answer:**
- **`append()`**: Adds a single element to the end of a list
- **`extend()`**: Adds all elements from an iterable to the end of a list

**Example:**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# append() - adds the entire list as one element
list1.append(list2)
print(list1)  # [1, 2, 3, [4, 5, 6]]

# extend() - adds each element individually
list1 = [1, 2, 3]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
```

### 18. What is the difference between shallow copy and deep copy?

**Answer:**
- **Shallow copy**: Creates a new object but inserts references to objects found in the original
- **Deep copy**: Creates a new object and recursively copies all nested objects

**Example:**
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = copy.copy(original)
shallow[0][0] = 'X'
print(original)  # [['X', 2, 3], [4, 5, 6]] - original affected

# Deep copy
original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)
deep[0][0] = 'Y'
print(original)  # [[1, 2, 3], [4, 5, 6]] - original not affected
```

### 19. What is the Global Interpreter Lock (GIL)? (Detailed)

**Answer:** The Global Interpreter Lock (GIL) is a mutex (mutual exclusion lock) that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously in a single process.

**Why does the GIL exist?**
1. **Memory Management**: Python's memory management isn't thread-safe. The GIL prevents race conditions when accessing Python objects
2. **Reference Counting**: Python uses reference counting for garbage collection, which needs protection from concurrent access
3. **Simplicity**: Makes the CPython implementation simpler and more stable

**Key Characteristics:**
- Only **one thread** can execute Python bytecode at a time
- **CPU-bound tasks** don't benefit from multithreading
- **I/O-bound tasks** can still benefit because GIL is released during I/O operations
- The GIL is **per-process**, not per-interpreter

**When is the GIL Released?**
1. During I/O operations (file reading, network requests)
2. When calling C extensions that release the GIL
3. During certain built-in functions (like `time.sleep()`)
4. Periodically (every 100 bytecode instructions in Python 2, time-based in Python 3)

**Comprehensive Examples:**

```python
import threading
import time
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 1. CPU-bound task - GIL limits performance
def cpu_intensive_task(n):
    """Simulates CPU-intensive work"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def test_cpu_bound():
    """Demonstrates GIL impact on CPU-bound tasks"""
    n = 1000000
    
    # Single-threaded
    start_time = time.time()
    result1 = cpu_intensive_task(n)
    single_time = time.time() - start_time
    
    # Multi-threaded (won't be faster due to GIL)
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_intensive_task, n//4) for _ in range(4)]
        results = [f.result() for f in futures]
    multi_thread_time = time.time() - start_time
    
    # Multi-processing (bypasses GIL)
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_intensive_task, n//4) for _ in range(4)]
        results = [f.result() for f in futures]
    multi_process_time = time.time() - start_time
    
    print(f"Single-threaded: {single_time:.2f}s")
    print(f"Multi-threaded: {multi_thread_time:.2f}s")
    print(f"Multi-processing: {multi_process_time:.2f}s")

# 2. I/O-bound task - GIL is released during I/O
def io_task(url):
    """Simulates I/O-bound work"""
    try:
        response = requests.get(url, timeout=5)
        return len(response.content)
    except:
        return 0

def test_io_bound():
    """Demonstrates that I/O-bound tasks benefit from threading"""
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1'
    ]
    
    # Single-threaded
    start_time = time.time()
    results = [io_task(url) for url in urls]
    single_time = time.time() - start_time
    
    # Multi-threaded (faster for I/O)
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(io_task, urls))
    multi_thread_time = time.time() - start_time
    
    print(f"I/O Single-threaded: {single_time:.2f}s")
    print(f"I/O Multi-threaded: {multi_thread_time:.2f}s")

# 3. Demonstrating GIL switching
def gil_demonstration():
    """Shows how threads compete for GIL"""
    shared_counter = 0
    lock = threading.Lock()
    
    def increment_counter(name, iterations):
        nonlocal shared_counter
        for i in range(iterations):
            with lock:  # Needed to prevent race conditions
                temp = shared_counter
                temp += 1
                shared_counter = temp
            
            # Show thread switching
            if i % 100000 == 0:
                print(f"Thread {name}: iteration {i}, counter = {shared_counter}")
    
    threads = []
    for i in range(3):
        t = threading.Thread(target=increment_counter, args=(f"T{i}", 500000))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Final counter value: {shared_counter}")

# Run demonstrations
if __name__ == "__main__":
    print("=== CPU-bound task comparison ===")
    test_cpu_bound()
    
    print("\n=== I/O-bound task comparison ===")
    test_io_bound()
    
    print("\n=== GIL thread switching ===")
    gil_demonstration()
```

**GIL Workarounds and Alternatives:**

```python
# 1. Use multiprocessing for CPU-bound tasks
from multiprocessing import Pool, cpu_count

def parallel_cpu_work():
    def worker_task(x):
        return sum(i*i for i in range(x))
    
    tasks = [100000] * cpu_count()
    
    # Using multiprocessing
    with Pool() as pool:
        results = pool.map(worker_task, tasks)
    return results

# 2. Use async/await for I/O-bound tasks
import asyncio
import aiohttp

async def async_fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def async_io_work():
    urls = ['http://httpbin.org/delay/1'] * 4
    
    async with aiohttp.ClientSession() as session:
        tasks = [async_fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

# 3. Use thread pools for I/O with proper design
from concurrent.futures import as_completed

def optimized_threading():
    def io_worker(item):
        time.sleep(0.1)  # Simulate I/O
        return item ** 2
    
    items = range(20)
    results = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_item = {executor.submit(io_worker, item): item for item in items}
        
        for future in as_completed(future_to_item):
            item = future_to_item[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                print(f'Item {item} generated an exception: {exc}')
    
    return results
```

**Performance Analysis Tools:**

```python
import sys
import threading
import time

def gil_monitoring():
    """Monitor GIL switching behavior"""
    
    def monitor_thread():
        while True:
            time.sleep(0.01)
            print(f"Monitor thread running at {time.time()}")
    
    def worker_thread(name, work_time):
        start = time.time()
        count = 0
        while time.time() - start < work_time:
            count += 1
            # Force some Python operations
            _ = [i for i in range(100)]
        print(f"Thread {name} completed {count} iterations")
    
    # Start monitor
    monitor = threading.Thread(target=monitor_thread, daemon=True)
    monitor.start()
    
    # Start worker threads
    workers = []
    for i in range(3):
        w = threading.Thread(target=worker_thread, args=(f"Worker-{i}", 2))
        workers.append(w)
        w.start()
    
    for w in workers:
        w.join()
```

**Key Interview Points:**

1. **GIL exists only in CPython** (not in Jython, IronPython, PyPy)
2. **Multithreading vs Multiprocessing**: Use multiprocessing for CPU-bound, threading for I/O-bound
3. **asyncio** is often better than threading for I/O-bound tasks
4. **C extensions** can release the GIL for CPU-intensive operations
5. **GIL contention** can make multithreaded code slower than single-threaded

**Common Misconceptions:**
- ❌ "Python doesn't support multithreading" - It does, but with limitations
- ❌ "GIL makes all concurrent code useless" - I/O-bound tasks still benefit
- ❌ "Removing GIL would make Python faster" - It would complicate memory management significantly

**Real-world Implications:**
- Web servers use multiprocessing (gunicorn, uwsgi)
- Data processing uses multiprocessing or distributed computing
- I/O-heavy applications benefit from threading or asyncio
- Scientific computing often uses NumPy/C extensions that release GIL

### 20. What are decorators in Python?

**Answer:** Decorators are functions that modify or enhance other functions without changing their code. They use the `@` symbol syntax.

**Example:**
```python
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()  # Prints timing information
```

### 21. What is the difference between `range()` and `xrange()` in Python?

**Answer:** In Python 3, `xrange()` was renamed to `range()`. In Python 2:
- **`range()`**: Returns a list (memory intensive)
- **`xrange()`**: Returns an iterator (memory efficient)

**Example:**
```python
# Python 3 (current)
for i in range(5):  # Memory efficient iterator
    print(i)

# If you need a list
numbers = list(range(5))  # [0, 1, 2, 3, 4]
```

### 22. What are Python modules and packages?

**Answer:**
- **Module**: A single Python file containing functions, classes, and variables
- **Package**: A directory containing multiple modules with an `__init__.py` file

**Example:**
```python
# Module example (math_utils.py)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Using the module
import math_utils
result = math_utils.add(5, 3)

# Or import specific functions
from math_utils import add, multiply
result = add(5, 3)
```

### 23. What is the difference between `break`, `continue`, and `pass`?

**Answer:**
- **`break`**: Exits the current loop completely
- **`continue`**: Skips the rest of the current iteration and moves to the next
- **`pass`**: Does nothing, used as a placeholder

**Example:**
```python
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Exit loop at 7
    if i == 5:
        pass      # Do nothing, continue normally
    print(i)  # Prints: 0, 1, 2, 4, 5, 6
```

### 24. What is exception handling in Python?

**Answer:** Exception handling allows you to handle errors gracefully using try-except blocks instead of letting the program crash.

**Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exception occurred")
finally:
    print("This always executes")

# Custom exception
class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong")
except CustomError as e:
    print(f"Custom error: {e}")
```

### 25. What are Python's built-in data types?

**Answer:** Python has several built-in data types categorized as:

**Numeric Types:**
- `int`: Integer numbers
- `float`: Floating point numbers
- `complex`: Complex numbers

**Sequence Types:**
- `str`: Strings
- `list`: Mutable sequences
- `tuple`: Immutable sequences

**Mapping Type:**
- `dict`: Key-value pairs

**Set Types:**
- `set`: Mutable sets
- `frozenset`: Immutable sets

**Boolean Type:**
- `bool`: True/False

**Example:**
```python
# Examples of each type
integer = 42
floating = 3.14
complex_num = 3 + 4j
string = "Hello"
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"key": "value"}
my_set = {1, 2, 3}
boolean = True
```

### 26. What is the difference between `list` and `tuple`?

**Answer:**
- **List**: Mutable, ordered, allows duplicates, uses square brackets `[]`
- **Tuple**: Immutable, ordered, allows duplicates, uses parentheses `()`

**Example:**
```python
# List - mutable
my_list = [1, 2, 3]
my_list[0] = 10
my_list.append(4)
print(my_list)  # [10, 2, 3, 4]

# Tuple - immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would cause an error
print(my_tuple)  # (1, 2, 3)

# Performance difference
import sys
print(sys.getsizeof([1, 2, 3]))  # List uses more memory
print(sys.getsizeof((1, 2, 3)))  # Tuple uses less memory
```

### 27. What is a dictionary in Python?

**Answer:** A dictionary is a mutable, unordered collection of key-value pairs. Keys must be immutable and unique.

**Example:**
```python
# Creating dictionaries
student = {
    "name": "John",
    "age": 20,
    "grades": [85, 90, 92]
}

# Accessing values
print(student["name"])  # John
print(student.get("city", "Not found"))  # Not found

# Adding/updating
student["city"] = "New York"
student.update({"phone": "123-456-7890"})

# Dictionary methods
print(student.keys())    # dict_keys(['name', 'age', 'grades', 'city', 'phone'])
print(student.values())  # dict_values(['John', 20, [85, 90, 92], 'New York', '123-456-7890'])
print(student.items())   # Key-value pairs
```

### 28. What is a set in Python?

**Answer:** A set is an unordered collection of unique elements. Sets are mutable and don't allow duplicates.

**Example:**
```python
# Creating sets
my_set = {1, 2, 3, 3, 4}  # Duplicates removed
print(my_set)  # {1, 2, 3, 4}

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2))   # {1, 2}

# Adding/removing elements
my_set.add(5)
my_set.remove(1)  # Raises error if not found
my_set.discard(10)  # No error if not found
```

### 29. What is string formatting in Python?

**Answer:** Python provides multiple ways to format strings: % formatting, .format() method, and f-strings (preferred in Python 3.6+).

**Example:**
```python
name = "Alice"
age = 25
score = 95.5

# % formatting (old style)
message1 = "Hello %s, you are %d years old" % (name, age)

# .format() method
message2 = "Hello {}, you are {} years old".format(name, age)
message3 = "Hello {name}, you scored {score:.1f}%".format(name=name, score=score)

# f-strings (recommended)
message4 = f"Hello {name}, you are {age} years old"
message5 = f"Hello {name}, you scored {score:.1f}%"

print(message5)  # Hello Alice, you scored 95.5%
```

### 30. What are file operations in Python?

**Answer:** Python provides built-in functions to read, write, and manipulate files using the `open()` function.

**Example:**
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python file operations")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppended line")
```

### 31. What is the `map()` function?

**Answer:** `map()` applies a function to every item in an iterable and returns a map object (iterator).

**Example:**
```python
# Basic usage
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# With regular function
def double(x):
    return x * 2

doubled = map(double, numbers)
print(list(doubled))  # [2, 4, 6, 8, 10]

# Multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # [5, 7, 9]
```

### 32. What is the `filter()` function?

**Answer:** `filter()` creates an iterator from elements of an iterable for which a function returns True.

**Example:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6, 8, 10]

# Filter with regular function
def is_positive(x):
    return x > 0

numbers_with_negatives = [-2, -1, 0, 1, 2, 3]
positive_numbers = filter(is_positive, numbers_with_negatives)
print(list(positive_numbers))  # [1, 2, 3]
```

### 33. What is the `reduce()` function?

**Answer:** `reduce()` applies a function cumulatively to items in an iterable to reduce it to a single value. It's in the `functools` module.

**Example:**
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5

# With initial value
total_with_initial = reduce(lambda x, y: x + y, numbers, 100)
print(total_with_initial)  # 115
```

### 34. What are closures in Python?

**Answer:** A closure is a function that has access to variables from its outer enclosing scope even after the outer function has finished executing.

**Example:**
```python
def outer_function(x):
    def inner_function(y):
        return x + y  # x is from outer scope
    return inner_function

# Create a closure
add_10 = outer_function(10)
print(add_10(5))  # 15

# Another example
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)
print(times_2(5))  # 10
print(times_3(5))  # 15
```

### 35. What is the difference between `sort()` and `sorted()`?

**Answer:**
- **`sort()`**: Sorts the list in-place and returns None
- **`sorted()`**: Returns a new sorted list, original remains unchanged

**Example:**
```python
numbers = [3, 1, 4, 1, 5, 9]

# sort() - modifies original list
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]

# sorted() - returns new list
original = [3, 1, 4, 1, 5, 9]
new_sorted = sorted(original)
print(original)    # [3, 1, 4, 1, 5, 9] - unchanged
print(new_sorted)  # [1, 1, 3, 4, 5, 9]

# Custom sorting
words = ["banana", "apple", "cherry"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # ['apple', 'banana', 'cherry']
```

### 36. What is duck typing in Python?

**Answer:** Duck typing is a concept where the type of an object is determined by its behavior (methods and properties) rather than its explicit type.

**Example:**
```python
class Duck:
    def swim(self):
        return "Duck swimming"
    
    def fly(self):
        return "Duck flying"

class Swan:
    def swim(self):
        return "Swan swimming"
    
    def fly(self):
        return "Swan flying"

def make_it_swim_and_fly(bird):
    # We don't check the type, just call the methods
    print(bird.swim())
    print(bird.fly())

# Both work because they have the same interface
duck = Duck()
swan = Swan()

make_it_swim_and_fly(duck)  # Works
make_it_swim_and_fly(swan)  # Also works
```

### 37. What are Python namespaces and scope?

**Answer:** Namespaces are containers that hold names (variables) and their corresponding objects. Scope determines where variables can be accessed.

**LEGB Rule: Local → Enclosing → Global → Built-in**

**Example:**
```python
x = "global"  # Global scope

def outer_function():
    x = "enclosing"  # Enclosing scope
    
    def inner_function():
        x = "local"  # Local scope
        print(f"Local x: {x}")
    
    inner_function()
    print(f"Enclosing x: {x}")

outer_function()
print(f"Global x: {x}")

# Global and nonlocal keywords
count = 0  # Global

def increment():
    global count
    count += 1

def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

my_counter = make_counter()
print(my_counter())  # 1
print(my_counter())  # 2
```

### 38. What is method overriding in Python?

**Answer:** Method overriding allows a subclass to provide a specific implementation of a method that's already defined in its parent class.

**Example:**
```python
class Animal:
    def make_sound(self):
        return "Some generic animal sound"
    
    def move(self):
        return "Moving"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return "Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return "Meow!"

# Using the overridden methods
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.make_sound())
# Output:
# Woof!
# Meow!
# Some generic animal sound
```

### 39. What is multiple inheritance in Python?

**Answer:** Multiple inheritance allows a class to inherit from multiple parent classes. Python uses MRO (Method Resolution Order) to resolve conflicts.

**Example:**
```python
class Mammal:
    def breathe(self):
        return "Breathing air"

class Swimmer:
    def swim(self):
        return "Swimming"

class Whale(Mammal, Swimmer):
    def dive(self):
        return "Diving deep"

# Whale inherits from both Mammal and Swimmer
whale = Whale()
print(whale.breathe())  # From Mammal
print(whale.swim())     # From Swimmer
print(whale.dive())     # Own method

# Check Method Resolution Order
print(Whale.__mro__)
```

### 40. What are abstract classes in Python?

**Answer:** Abstract classes cannot be instantiated and contain abstract methods that must be implemented by subclasses. Use the `abc` module.

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):  # Concrete method
        return "This is a shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # This would raise TypeError
rectangle = Rectangle(5, 3)
print(rectangle.area())      # 15
print(rectangle.perimeter()) # 16
```

### 41. What is the `__init__` method?

**Answer:** `__init__` is the constructor method called when an object is created. It initializes the object's attributes.

**Example:**
```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        print(f"Person {name} created")
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob")  # age defaults to 0

print(person1.introduce())
print(person2.introduce())
```

### 42. What are magic methods (dunder methods) in Python?

**Answer:** Magic methods are special methods with double underscores that define how objects behave with built-in operations.

**Example:**
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):  # String representation
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):  # Developer representation
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):  # Addition operator
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):  # Equality operator
        return self.x == other.x and self.y == other.y
    
    def __len__(self):  # Length
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)          # Vector(3, 4)
print(v1 + v2)     # Vector(4, 6)
print(v1 == v2)    # False
print(len(v1))     # 5
```

### 43. What is the difference between `staticmethod` and `classmethod`?

**Answer:**
- **`@staticmethod`**: Belongs to class but doesn't access class or instance data
- **`@classmethod`**: Receives class as first argument (`cls`) and can access class variables

**Example:**
```python
class MathUtils:
    pi = 3.14159  # Class variable
    
    @staticmethod
    def add(x, y):
        return x + y  # No access to class/instance
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2  # Access class variable
    
    @classmethod
    def from_string(cls, math_string):
        # Alternative constructor
        return cls()

# Usage
print(MathUtils.add(5, 3))          # 8
print(MathUtils.circle_area(5))     # 78.53975

# Can call on instance too
utils = MathUtils()
print(utils.add(2, 3))              # 5
```

### 44. What is the `property` decorator?

**Answer:** The `@property` decorator allows you to define methods that can be accessed like attributes, providing getter, setter, and deleter functionality.

**Example:**
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.fahrenheit = 86
print(temp.celsius)     # 30.0
```

### 45. What is context management in Python?

**Answer:** Context managers ensure proper resource management using `with` statements. They implement `__enter__` and `__exit__` methods.

**Example:**
```python
# Using built-in context manager
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
# File automatically closed

# Custom context manager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing connection to {self.db_name}")
        self.connection = None

# Using custom context manager
with DatabaseConnection("mydb") as conn:
    print(f"Using {conn}")

# Using contextlib
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Time taken: {end - start}")

with timer():
    import time
    time.sleep(1)
```

### 46. What is monkey patching in Python?

**Answer:** Monkey patching is dynamically modifying a class or module at runtime by adding, modifying, or deleting attributes or methods.

**Example:**
```python
class Calculator:
    def add(self, a, b):
        return a + b

# Original functionality
calc = Calculator()
print(calc.add(2, 3))  # 5

# Monkey patch - add new method
def multiply(self, a, b):
    return a * b

Calculator.multiply = multiply
print(calc.multiply(2, 3))  # 6

# Monkey patch - modify existing method
original_add = Calculator.add

def enhanced_add(self, a, b):
    result = original_add(self, a, b)
    print(f"Adding {a} + {b} = {result}")
    return result

Calculator.add = enhanced_add
calc.add(2, 3)  # Prints: Adding 2 + 3 = 5
```

### 47. What is pickling and unpickling in Python?

**Answer:** Pickling is serializing Python objects to binary format, unpickling is deserializing them back to Python objects.

**Example:**
```python
import pickle

# Data to pickle
data = {
    'name': 'John',
    'age': 30,
    'items': [1, 2, 3, 4]
}

# Pickling (serialization)
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Unpickling (deserialization)
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)  # {'name': 'John', 'age': 30, 'items': [1, 2, 3, 4]}

# Pickle to bytes
pickled_bytes = pickle.dumps(data)
unpickled_data = pickle.loads(pickled_bytes)
print(unpickled_data)
```

### 48. What are regular expressions in Python?

**Answer:** Regular expressions are patterns used to match character combinations in strings. Python's `re` module provides regex functionality.

**Example:**
```python
import re

text = "Contact us at john@example.com or mary@test.org"

# Find all email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(emails)  # ['john@example.com', 'mary@test.org']

# Search for pattern
match = re.search(r'(\w+)@(\w+)\.(\w+)', text)
if match:
    print(f"Username: {match.group(1)}")  # john
    print(f"Domain: {match.group(2)}")    # example
    print(f"TLD: {match.group(3)}")       # com

# Replace pattern
new_text = re.sub(r'\b\d+\b', 'NUMBER', "I have 5 apples and 10 oranges")
print(new_text)  # I have NUMBER apples and NUMBER oranges
```

### 49. What is the difference between `json.loads()` and `json.load()`?

**Answer:**
- **`json.loads()`**: Deserializes JSON string to Python object
- **`json.load()`**: Deserializes JSON from file-like object to Python object

**Example:**
```python
import json

# json.loads() - from string
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)  # {'name': 'John', 'age': 30, 'city': 'New York'}

# json.dumps() - to string
python_dict = {"name": "Alice", "age": 25}
json_string = json.dumps(python_dict)
print(json_string)  # '{"name": "Alice", "age": 25}'

# json.load() - from file
with open('data.json', 'w') as f:
    json.dump(python_dict, f)

with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)  # {'name': 'Alice', 'age': 25}
```

### 50. What are iterators and iterables in Python?

**Answer:**
- **Iterable**: Object that can be iterated over (has `__iter__` method)
- **Iterator**: Object that produces values one at a time (has `__next__` and `__iter__` methods)

**Example:**
```python
# Built-in iterables
my_list = [1, 2, 3, 4]  # Iterable
my_iterator = iter(my_list)  # Iterator

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2

# Custom iterator
class Counter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.max_count:
            self.count += 1
            return self.count
        else:
            raise StopIteration

# Using custom iterator
counter = Counter(3)
for num in counter:
    print(num)  # 1, 2, 3

# Check if object is iterable
from collections.abc import Iterable
print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance(42, Iterable))         # False
```

### 51. What is the difference between `__str__` and `__repr__` methods?

**Answer:**
- **`__str__`**: Returns human-readable string representation for end users
- **`__repr__`**: Returns unambiguous string representation for developers/debugging

**Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age} years old)"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(str(person))   # Alice (30 years old)
print(repr(person))  # Person('Alice', 30)
print(person)        # Alice (30 years old) - calls __str__

# In interactive shell or debugging
[person]  # [Person('Alice', 30)] - calls __repr__
```

### 52. What are Python's memory management and garbage collection?

**Answer:** Python uses automatic memory management with reference counting and cyclic garbage collection to free unused memory.

**Example:**
```python
import gc
import sys

# Reference counting
a = [1, 2, 3]
print(sys.getrefcount(a))  # Shows reference count

b = a  # Increases reference count
print(sys.getrefcount(a))

del b  # Decreases reference count
print(sys.getrefcount(a))

# Garbage collection for cycles
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

# Create circular reference
parent = Node("parent")
child = Node("child")
parent.children.append(child)
child.parent = parent

# Manual garbage collection
print(f"Garbage collected: {gc.collect()} objects")

# Check garbage collection stats
print(gc.get_stats())
```

### 53. What is the difference between `deepcopy` and `copy`?

**Answer:** Already covered in question 18, but here's additional detail:

**Example:**
```python
import copy

# Nested mutable objects
original = {
    'numbers': [1, 2, 3],
    'nested': {'a': [4, 5, 6]}
}

# Shallow copy
shallow = copy.copy(original)
shallow['numbers'].append(4)
shallow['nested']['a'].append(7)

print("Original after shallow copy modification:")
print(original)  # Original is affected

# Deep copy
original = {
    'numbers': [1, 2, 3],
    'nested': {'a': [4, 5, 6]}
}

deep = copy.deepcopy(original)
deep['numbers'].append(4)
deep['nested']['a'].append(7)

print("Original after deep copy modification:")
print(original)  # Original is NOT affected
```

### 54. What are Python's data model and special methods?

**Answer:** Python's data model defines how objects behave with language constructs through special methods (magic/dunder methods).

**Example:**
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def __str__(self):
        return f"Account balance: ${self._balance}"
    
    def __repr__(self):
        return f"BankAccount({self._balance})"
    
    def __add__(self, amount):
        return BankAccount(self._balance + amount)
    
    def __sub__(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        return BankAccount(self._balance - amount)
    
    def __eq__(self, other):
        return self._balance == other._balance
    
    def __lt__(self, other):
        return self._balance < other._balance
    
    def __bool__(self):
        return self._balance > 0
    
    def __len__(self):
        return len(str(self._balance))

# Using the special methods
account1 = BankAccount(100)
account2 = BankAccount(50)

print(account1)           # Account balance: $100
print(account1 + 50)      # Account balance: $150
print(account1 - 25)      # Account balance: $75
print(account1 == account2)  # False
print(account1 > account2)   # True
print(bool(account1))     # True
print(len(account1))      # 3 (length of "100")
```

---

## Data Science and Libraries

### Additional Questions for Data Science Roles:

**55. What is NumPy and why is it important?**

**Answer:** NumPy is a fundamental library for scientific computing with Python, providing support for large multi-dimensional arrays and mathematical functions.

**Example:**
```python
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Array operations
print(arr * 2)          # [2, 4, 6, 8, 10]
print(np.mean(arr))     # 3.0
print(np.max(arr))      # 5

# Matrix operations
print(matrix.shape)     # (2, 2)
print(matrix.T)         # Transpose
```

**56. What is Pandas and its main data structures?**

**Answer:** Pandas provides high-performance data structures (Series and DataFrame) for data manipulation and analysis.

**Example:**
```python
import pandas as pd

# Series
s = pd.Series([1, 3, 5, 7, 9])
print(s)

# DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'Chicago']
})

print(df.head())
print(df.describe())
print(df['Age'].mean())
```

---

## Key Tips for Python Interviews

1. **Practice coding problems** on platforms like LeetCode, HackerRank
2. **Understand time and space complexity** of your solutions
3. **Know Python's built-in functions** and when to use them
4. **Be familiar with common libraries**: NumPy, Pandas, Requests
5. **Understand Python's memory management** and garbage collection
6. **Practice explaining code** clearly and concisely

---

## Common Mistakes to Avoid

1. **Mutable default arguments** in functions
2. **Late binding closures** in loops
3. **Not understanding the difference** between shallow and deep copy
4. **Forgetting about Python's** operator precedence
5. **Not handling exceptions** properly

**Example of mutable default argument mistake:**
```python
# Wrong way
def add_item(item, target_list=[]):
    target_list.append(item)
    return target_list

# Right way
def add_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

Remember: Practice regularly, understand the concepts deeply, and always write clean, readable code! 