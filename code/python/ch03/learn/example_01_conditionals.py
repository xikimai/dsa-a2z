"""
Example 01: Conditionals
=====================================
Chapter 3: Decisions and Loops

This example shows you how Python makes decisions using if/else,
elif chains, ternary expressions, logical operators, and match/case.
Every program needs to make choices — this is how you do it.
"""

# ──────────────────────────────────────────────
# PART 1: Basic if/else — the simplest decision
# ──────────────────────────────────────────────

age = 14

if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote.")

# The condition (age >= 18) is either True or False.
# Python runs the indented block under whichever branch is True.


# ──────────────────────────────────────────────
# PART 2: elif — multiple branches
# ──────────────────────────────────────────────

# When you have more than two cases, use elif (short for "else if").
# Python checks each condition top-to-bottom and runs the FIRST True one.

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")  # Score 85 → Grade B

# ORDER MATTERS! If you put (score >= 70) first, a score of 95
# would match it and get "C" instead of "A". Always check the
# most restrictive condition first.


# ──────────────────────────────────────────────
# PART 3: Comparison operators
# ──────────────────────────────────────────────

# ==   equal to          (don't confuse with = which is assignment!)
# !=   not equal to
# <    less than
# >    greater than
# <=   less than or equal
# >=   greater than or equal

x = 10
print(x == 10)   # True
print(x != 5)    # True
print(x < 20)    # True
print(x > 20)    # False
print(x <= 10)   # True  (equal counts!)
print(x >= 11)   # False


# ──────────────────────────────────────────────
# PART 4: Logical operators — combining conditions
# ──────────────────────────────────────────────

# and → both must be True
# or  → at least one must be True
# not → flips True/False

age = 14
has_permission = True

if age >= 13 and has_permission:
    print("Welcome!")  # Both conditions are True

temperature = 35

if temperature < 0 or temperature > 40:
    print("Extreme weather!")
else:
    print("Normal temperature.")  # 35 is between 0 and 40

is_raining = False
if not is_raining:
    print("No umbrella needed.")  # not False → True


# ──────────────────────────────────────────────
# PART 5: Ternary operator — one-line if/else
# ──────────────────────────────────────────────

# Python's ternary: value_if_true if condition else value_if_false
n = 7
result = "Even" if n % 2 == 0 else "Odd"
print(f"{n} is {result}")  # 7 is Odd

# This is exactly the same as:
# if n % 2 == 0:
#     result = "Even"
# else:
#     result = "Odd"

# Use ternary for simple one-line decisions.
# Use regular if/else when the logic is more complex.


# ──────────────────────────────────────────────
# PART 6: match/case — Python 3.10+ pattern matching
# ──────────────────────────────────────────────

# match/case is Python's version of switch/case from other languages.
# It's great when you have many specific values to check.

command = "start"

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "pause":
        print("Pausing...")
    case _:
        print(f"Unknown command: {command}")

# The _ (underscore) case is the default — it matches anything.
# match/case is cleaner than a long chain of if/elif when you're
# comparing one variable against many exact values.


# ──────────────────────────────────────────────
# PART 7: Truthy and Falsy values
# ──────────────────────────────────────────────

# In Python, some values are "falsy" — they act like False in if statements:
#   False, 0, 0.0, "", [], {}, None
# Everything else is "truthy" — it acts like True.

name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Name is empty!")  # "" is falsy

count = 0
if count:
    print(f"Count is {count}")
else:
    print("Count is zero!")  # 0 is falsy


# ──────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────
#
# 1. if/elif/else for branching — check conditions top to bottom
# 2. Comparison: ==, !=, <, >, <=, >=
# 3. Logical: and, or, not — combine conditions
# 4. Ternary: x if condition else y — one-line decisions
# 5. match/case — clean alternative to long elif chains (Python 3.10+)
# 6. Falsy values: False, 0, 0.0, "", [], {}, None
