"""
Example 01: Collections Basics
==============================
Chapter 5: Collections

Run with:
    python code/python/ch05/learn/example_01_collections_basics.py
"""

# ============================================================
# PART 1: Creating and accessing lists
# ============================================================
# A list is an ordered, mutable collection of items.
# Think of it like a numbered shelf where you can store anything.


def create_demo_list():
    """Show different ways to create and access lists."""
    # Creating lists
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    numbers = [10, 20, 30, 40, 50]
    empty = []
    mixed = [1, "hello", 3.14, True]

    # Indexing (0-based: first element is index 0)
    first = fruits[0]      # "apple"
    third = fruits[2]      # "cherry"

    # Negative indexing (count from the end)
    last = fruits[-1]      # "elderberry"
    second_last = fruits[-2]  # "date"

    # Slicing [start:stop] — stop is exclusive
    first_three = fruits[0:3]   # ["apple", "banana", "cherry"]
    middle = fruits[1:4]        # ["banana", "cherry", "date"]
    from_second = fruits[2:]    # ["cherry", "date", "elderberry"]
    up_to_third = fruits[:3]    # ["apple", "banana", "cherry"]

    # Length
    size = len(fruits)     # 5

    return fruits, numbers, empty, mixed, first, last, first_three, size


print("=== PART 1: Creating and Accessing Lists ===")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"fruits = {fruits}")
print(f"fruits[0]  = {fruits[0]}")
print(f"fruits[2]  = {fruits[2]}")
print(f"fruits[-1] = {fruits[-1]}")
print(f"fruits[-2] = {fruits[-2]}")
print(f"fruits[0:3] = {fruits[0:3]}")
print(f"fruits[2:]  = {fruits[2:]}")
print(f"fruits[:3]  = {fruits[:3]}")
print(f"len(fruits) = {len(fruits)}")
print()

# ============================================================
# PART 2: Modifying lists
# ============================================================
# Lists are mutable — you can add, remove, and change elements.


def modify_demo():
    """Demonstrate list modifications."""
    heroes = ["Alice", "Bob", "Charlie"]

    # append — add to the end
    heroes.append("Diana")        # ["Alice", "Bob", "Charlie", "Diana"]

    # insert — add at a specific position
    heroes.insert(1, "Eve")       # ["Alice", "Eve", "Bob", "Charlie", "Diana"]

    # remove — remove first occurrence of a value
    heroes.remove("Bob")          # ["Alice", "Eve", "Charlie", "Diana"]

    # pop — remove and return by index (default: last element)
    last = heroes.pop()           # returns "Diana", list = ["Alice", "Eve", "Charlie"]
    first = heroes.pop(0)         # returns "Alice", list = ["Eve", "Charlie"]

    return heroes, last, first


print("=== PART 2: Modifying Lists ===")
heroes = ["Alice", "Bob", "Charlie"]
print(f"Start:  {heroes}")
heroes.append("Diana")
print(f"append('Diana'):  {heroes}")
heroes.insert(1, "Eve")
print(f"insert(1, 'Eve'): {heroes}")
heroes.remove("Bob")
print(f"remove('Bob'):     {heroes}")
last = heroes.pop()
print(f"pop():  returned '{last}', list = {heroes}")
first = heroes.pop(0)
print(f"pop(0): returned '{first}', list = {heroes}")
print()

# ============================================================
# PART 3: String basics
# ============================================================
# Strings are sequences of characters. They are IMMUTABLE —
# you cannot change a string in place; you create new ones.


def string_demo():
    """Demonstrate string operations."""
    msg = "Hello, World!"

    # Strings are immutable — indexing works, but assignment doesn't
    first_char = msg[0]       # 'H'
    # msg[0] = 'h'           # This would crash! TypeError

    # Slicing
    greeting = msg[:5]        # "Hello"
    name = msg[7:12]          # "World"

    # Common methods (all return NEW strings)
    lower = msg.lower()       # "hello, world!"
    upper = msg.upper()       # "HELLO, WORLD!"
    pos = msg.find("World")   # 7 (index where "World" starts)
    replaced = msg.replace("World", "Python")  # "Hello, Python!"

    # Split and join
    words = "one two three".split()          # ["one", "two", "three"]
    joined = "-".join(words)                 # "one-two-three"

    return first_char, greeting, lower, upper, pos, replaced, words, joined


print("=== PART 3: String Basics ===")
msg = "Hello, World!"
print(f"msg = '{msg}'")
print(f"msg[0]  = '{msg[0]}'")
print(f"msg[:5] = '{msg[:5]}'")
print(f"msg[7:12] = '{msg[7:12]}'")
print(f"msg.lower()  = '{msg.lower()}'")
print(f"msg.upper()  = '{msg.upper()}'")
print(f"msg.find('World') = {msg.find('World')}")
print(f"msg.replace('World', 'Python') = '{msg.replace('World', 'Python')}'")
words = "one two three".split()
print(f"'one two three'.split() = {words}")
print(f"'-'.join({words}) = '{'-'.join(words)}'")
print()

# ============================================================
# PART 4: Iterating over lists and strings
# ============================================================
# Three common patterns: for-each, enumerate, and index-based.


def iterate_demo():
    """Demonstrate iteration patterns."""
    colors = ["red", "green", "blue"]

    # Pattern 1: for-each (simplest, when you just need the value)
    for color in colors:
        print(f"  {color}")

    # Pattern 2: enumerate (when you need both index and value)
    for i, color in enumerate(colors):
        print(f"  [{i}] {color}")

    # Pattern 3: index-based (when you need to control the index)
    for i in range(len(colors)):
        print(f"  colors[{i}] = {colors[i]}")


print("=== PART 4: Iterating ===")
colors = ["red", "green", "blue"]
print("for-each:")
for color in colors:
    print(f"  {color}")
print("enumerate:")
for i, color in enumerate(colors):
    print(f"  [{i}] {color}")
print("index-based:")
for i in range(len(colors)):
    print(f"  colors[{i}] = {colors[i]}")
print()

# Iterating over strings works the same way
print("Iterating over a string:")
for ch in "Python":
    print(f"  '{ch}'")
