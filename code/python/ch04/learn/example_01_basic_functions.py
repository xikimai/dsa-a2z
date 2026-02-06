"""
Example 01: Basic Functions
===========================
Chapter 4: Functions

Run with:
    python code/python/ch04/learn/example_01_basic_functions.py
"""

# ============================================================
# PART 1: Defining a simple function
# ============================================================
# A function is a reusable block of code with a name.
# You define it with `def`, give it a name, and optionally list parameters.

def square(x):
    """Return the square of x."""
    return x * x


def greet(name):
    """Print a greeting for the given name."""
    print(f"Hey there, {name}! Welcome aboard.")


print("=== PART 1: Simple Functions ===")
print(f"square(5) = {square(5)}")      # 25
print(f"square(-3) = {square(-3)}")    # 9
greet("Alex")                           # Hey there, Alex! Welcome aboard.
print()

# ============================================================
# PART 2: Functions with multiple parameters
# ============================================================
# Functions can take more than one parameter, separated by commas.

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def format_name(first, last):
    """Return a nicely formatted full name."""
    return f"{first} {last}"


print("=== PART 2: Multiple Parameters ===")
print(f"add(3, 7) = {add(3, 7)}")                         # 10
print(f"add(-1, 1) = {add(-1, 1)}")                        # 0
print(f"format_name('Ada', 'Lovelace') = {format_name('Ada', 'Lovelace')}")  # Ada Lovelace
print()

# ============================================================
# PART 3: Functions with return values vs. print
# ============================================================
# A function that uses `return` gives back a value you can store or use.
# A function that only uses `print` shows something on screen but returns None.

def multiply_return(a, b):
    """Return a * b — the caller decides what to do with the result."""
    return a * b


def multiply_print(a, b):
    """Print a * b — no return value (returns None implicitly)."""
    print(f"{a} * {b} = {a * b}")


print("=== PART 3: Return vs. Print ===")
result = multiply_return(4, 5)
print(f"multiply_return(4, 5) returned: {result}")  # 20
print(f"Can we use it in math? result + 10 = {result + 10}")  # 30
print()

print("multiply_print(4, 5) output:")
none_result = multiply_print(4, 5)   # prints "4 * 5 = 20"
print(f"But its return value is: {none_result}")  # None
# print(none_result + 10)  # This would crash! Can't add None + 10
print()

# ============================================================
# PART 4: Default parameters
# ============================================================
# You can give parameters default values. If the caller doesn't
# provide that argument, the default kicks in.

def repeat_string(s, n=3):
    """Return the string s repeated n times, separated by spaces."""
    return " ".join([s] * n)


print("=== PART 4: Default Parameters ===")
print(f"repeat_string('ha') = '{repeat_string('ha')}'")          # ha ha ha  (n defaults to 3)
print(f"repeat_string('yo', 5) = '{repeat_string('yo', 5)}'")    # yo yo yo yo yo
print(f"repeat_string('!', 1) = '{repeat_string('!', 1)}'")      # !
print(f"repeat_string('x', 0) = '{repeat_string('x', 0)}'")      # (empty string)
print()

# ============================================================
# PART 5: Calling one function from another
# ============================================================
# Functions can call other functions. This is how you build
# complex behavior from simple building blocks.

def min_of_two(a, b):
    """Return the smaller of a and b."""
    if a <= b:
        return a
    return b


def min_of_three(a, b, c):
    """Return the smallest of a, b, and c using min_of_two."""
    return min_of_two(min_of_two(a, b), c)


print("=== PART 5: Functions Calling Functions ===")
print(f"min_of_two(7, 3) = {min_of_two(7, 3)}")          # 3
print(f"min_of_two(-1, -5) = {min_of_two(-1, -5)}")      # -5
print(f"min_of_three(9, 2, 7) = {min_of_three(9, 2, 7)}")  # 2
print(f"min_of_three(4, 4, 4) = {min_of_three(4, 4, 4)}")  # 4
print(f"min_of_three(-1, 0, 1) = {min_of_three(-1, 0, 1)}")  # -1
