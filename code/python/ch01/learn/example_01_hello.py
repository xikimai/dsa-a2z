"""
Example 01: Hello World — Your First Input/Output Program
==========================================================
Chapter 1: The Coder's Toolkit

This example shows you the two most fundamental operations in competitive
programming: reading input and writing output.

Every competitive programming problem follows the same pattern:
  1. Read input from the user (or a judge system)
  2. Do some computation
  3. Print the output

Let's start with the simplest possible version of this pattern.
"""

# ──────────────────────────────────────────────
# PART 1: Simple output
# ──────────────────────────────────────────────

# print() writes text to the screen, followed by a newline.
print("Hello, World!")

# You can print numbers too.
print(42)

# You can print multiple things separated by spaces.
print("The answer is", 42)


# ──────────────────────────────────────────────
# PART 2: Reading input
# ──────────────────────────────────────────────

# input() reads one line of text from the user.
# In competitive programming, this reads from "standard input" (stdin).
name = input()  # If the user types "Maya", name will be "Maya"
print("Hello,", name)


# ──────────────────────────────────────────────
# PART 3: Reading numbers
# ──────────────────────────────────────────────

# input() always gives you a string. To get a number, convert it with int().
# If the input line is "7", this reads the string "7" and converts it to
# the integer 7.
number = int(input())
print("Your number doubled is", number * 2)


# ──────────────────────────────────────────────
# PART 4: Reading multiple numbers on one line
# ──────────────────────────────────────────────

# Many problems give you multiple numbers on one line, like "3 5".
# Here's how to read them:
#
#   input()          → "3 5"       (a string)
#   .split()         → ["3", "5"]  (a list of strings)
#   map(int, ...)    → 3, 5        (integers)
#   a, b = ...       → a=3, b=5   (assigned to variables)

a, b = map(int, input().split())
print("Sum:", a + b)


# ──────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────
#
# These four patterns cover almost every input/output scenario you'll see:
#
#   print(value)                        → output a value
#   s = input()                         → read a string
#   n = int(input())                    → read one integer
#   a, b = map(int, input().split())    → read multiple integers on one line
#
# You'll use these in every single problem from here on out!
