"""
Example 02: Input/Output Patterns for Competitive Programming
==============================================================
Chapter 2: Your First Programs — Speaking Three Languages

This example covers every I/O pattern you'll need for competitive
programming problems. Master these and you'll never struggle with
reading input again.
"""

# ──────────────────────────────────────────────
# PART 1: Reading a single string
# ──────────────────────────────────────────────

# input() reads one line and returns it as a string.
name = input()          # If user types "Maya", name = "Maya"
print(f"Hello, {name}!")

# f-strings (formatted strings) let you embed variables directly:
age = 14
print(f"I am {age} years old.")
print(f"Next year I'll be {age + 1}.")


# ──────────────────────────────────────────────
# PART 2: Reading a single integer
# ──────────────────────────────────────────────

# Wrap input() with int() to read an integer.
n = int(input())        # If user types "42", n = 42
print(f"Double: {n * 2}")


# ──────────────────────────────────────────────
# PART 3: Reading a single float
# ──────────────────────────────────────────────

# Wrap input() with float() to read a decimal number.
temp = float(input())   # If user types "98.6", temp = 98.6
print(f"Temperature: {temp}")


# ──────────────────────────────────────────────
# PART 4: Reading multiple integers on one line
# ──────────────────────────────────────────────

# Pattern: split the line, then convert each part to int.
# If the line is "3 5 7":
#   input()          → "3 5 7"
#   .split()         → ["3", "5", "7"]
#   map(int, ...)    → 3, 5, 7

a, b = map(int, input().split())       # Two integers
print(f"{a} + {b} = {a + b}")

x, y, z = map(int, input().split())    # Three integers
print(f"Sum: {x + y + z}")


# ──────────────────────────────────────────────
# PART 5: Reading multiple floats on one line
# ──────────────────────────────────────────────

# Same pattern, just use float instead of int.
x1, y1 = map(float, input().split())   # Two floats
print(f"Point: ({x1}, {y1})")


# ──────────────────────────────────────────────
# PART 6: Reading a list of numbers
# ──────────────────────────────────────────────

# Sometimes you don't know how many numbers there are,
# or you want to store them all in a list.
numbers = list(map(int, input().split()))
print(f"You entered {len(numbers)} numbers: {numbers}")


# ──────────────────────────────────────────────
# PART 7: Output formatting
# ──────────────────────────────────────────────

# Print with specific decimal places:
pi = 3.14159265
print(f"{pi:.2f}")      # 3.14  (2 decimal places)
print(f"{pi:.4f}")      # 3.1416 (4 decimal places, rounds!)

# Print multiple values separated by space (default):
print(1, 2, 3)          # 1 2 3

# Print with a custom separator:
print(1, 2, 3, sep=", ")  # 1, 2, 3

# Print without a newline at the end:
print("Hello ", end="")
print("World!")          # Hello World!  (on one line)


# ──────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────
#
# Input patterns:
#   s = input()                          → read a string
#   n = int(input())                     → read one integer
#   x = float(input())                   → read one float
#   a, b = map(int, input().split())     → read multiple ints
#   a, b = map(float, input().split())   → read multiple floats
#   nums = list(map(int, input().split()))  → read a list of ints
#
# Output patterns:
#   print(value)                         → basic output
#   print(f"{var:.2f}")                  → formatted decimal
#   print(a, b, sep=", ")               → custom separator
#   print(x, end="")                    → no newline
