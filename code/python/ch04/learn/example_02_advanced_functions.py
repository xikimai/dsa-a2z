"""
Example 02: Advanced Functions
==============================
Chapter 4: Functions

Run with:
    python code/python/ch04/learn/example_02_advanced_functions.py
"""

# ============================================================
# PART 1: Pass by value vs. reference
# ============================================================
# In Python, EVERYTHING is passed by reference to the object.
# But here's the twist:
#   - Immutable types (int, str, tuple) can't be changed in place,
#     so it *feels* like pass-by-value.
#   - Mutable types (list, dict, set) CAN be changed in place,
#     so changes inside the function affect the original.

def try_to_change_number(x):
    """Try to modify an integer — spoiler: it won't affect the original."""
    x = x + 100
    print(f"  Inside function: x = {x}")


def modify_list(lst):
    """Modify a list — this WILL affect the original."""
    lst.append(999)
    print(f"  Inside function: lst = {lst}")


print("=== PART 1: Pass by Value vs. Reference ===")

my_num = 42
print(f"Before: my_num = {my_num}")
try_to_change_number(my_num)
print(f"After:  my_num = {my_num}")    # Still 42! Integers are immutable.
print()

my_list = [1, 2, 3]
print(f"Before: my_list = {my_list}")
modify_list(my_list)
print(f"After:  my_list = {my_list}")  # [1, 2, 3, 999] — the list was mutated!
print()

# Key takeaway: If you don't WANT to modify the original list,
# pass a copy: modify_list(my_list.copy()) or modify_list(my_list[:])

# ============================================================
# PART 2: Scope and shadowing
# ============================================================
# Variables defined inside a function are LOCAL — they only exist
# inside that function. Variables defined outside are GLOBAL.
# If a local variable has the same name as a global one, the local
# one "shadows" the global — it hides it within the function.

message = "I am global"


def show_scope():
    """Demonstrate local vs. global scope."""
    message = "I am local"  # This creates a NEW local variable
    print(f"  Inside show_scope: message = '{message}'")


print("=== PART 2: Scope and Shadowing ===")
print(f"Before calling show_scope: message = '{message}'")
show_scope()
print(f"After calling show_scope:  message = '{message}'")  # Still global!
print()

# Using the `global` keyword (use sparingly — it's usually a code smell)
counter = 0


def increment_counter():
    """Increment the global counter. Using `global` keyword."""
    global counter
    counter += 1


print(f"counter = {counter}")
increment_counter()
print(f"After increment_counter(): counter = {counter}")  # 1
increment_counter()
print(f"After increment_counter(): counter = {counter}")  # 2
print()

# Pro tip: Instead of global variables, prefer passing values as
# parameters and returning results. It makes code easier to understand.

# ============================================================
# PART 3: Lambda functions
# ============================================================
# A lambda is a tiny anonymous function written on one line.
# Syntax: lambda parameters: expression
# Useful for short throwaway functions, especially with sorted(), map(), etc.

double = lambda x: x * 2
add = lambda a, b: a + b

print("=== PART 3: Lambda Functions ===")
print(f"double(7) = {double(7)}")     # 14
print(f"add(3, 4) = {add(3, 4)}")    # 7
print()

# Lambdas really shine when used as arguments to other functions:
words = ["banana", "apple", "cherry", "date"]
sorted_by_length = sorted(words, key=lambda w: len(w))
print(f"Words sorted by length: {sorted_by_length}")
# ['date', 'apple', 'banana', 'cherry']

pairs = [(1, 'z'), (3, 'a'), (2, 'm')]
sorted_by_second = sorted(pairs, key=lambda p: p[1])
print(f"Pairs sorted by second element: {sorted_by_second}")
# [(3, 'a'), (2, 'm'), (1, 'z')]
print()

# Note: For anything more than a simple expression, use a regular
# function with `def`. Lambdas should be one-liners.

# ============================================================
# PART 4: Functions as values
# ============================================================
# In Python, functions are "first-class citizens" — you can store
# them in variables, put them in lists, pass them to other functions.

def shout(text):
    """Return text in uppercase with exclamation marks."""
    return text.upper() + "!!!"


def whisper(text):
    """Return text in lowercase with ellipsis."""
    return text.lower() + "..."


print("=== PART 4: Functions as Values ===")

# Store a function in a variable
my_func = shout
print(f"my_func('hello') = {my_func('hello')}")  # HELLO!!!

my_func = whisper
print(f"my_func('hello') = {my_func('hello')}")  # hello...
print()

# Store functions in a list and loop through them
transformers = [shout, whisper, str.title, str.upper]
for func in transformers:
    print(f"  {func.__name__}('python is fun') = {func('python is fun')}")
print()

# Pass a function as an argument to another function
def apply_twice(func, value):
    """Apply func to value, then apply func to that result."""
    return func(func(value))


print(f"apply_twice(double, 3) = {apply_twice(double, 3)}")  # double(double(3)) = 12
print(f"apply_twice(shout, 'hi') = {apply_twice(shout, 'hi')}")  # HI!!!!!!
