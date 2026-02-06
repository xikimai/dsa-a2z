"""
Example 01: Variables and Data Types
=====================================
Chapter 2: Your First Programs — Speaking Three Languages

This example shows you how Python handles variables, data types, and
type checking. Understanding types is crucial because every piece of
data in your program has a type, and the type determines what you can
do with it.
"""

# ──────────────────────────────────────────────
# PART 1: Variables — giving names to values
# ──────────────────────────────────────────────

# A variable is just a name that points to a value.
# Python figures out the type automatically — you don't declare it.

age = 14               # int (integer — a whole number)
height = 5.7           # float (floating-point — a decimal number)
name = "Maya"          # str (string — text)
is_student = True      # bool (boolean — True or False)
favorite = None        # NoneType (the "nothing" value)

print("age:", age)
print("height:", height)
print("name:", name)
print("is_student:", is_student)
print("favorite:", favorite)


# ──────────────────────────────────────────────
# PART 2: The 5 basic types you'll see everywhere
# ──────────────────────────────────────────────

# int    — whole numbers:       42, -7, 0, 1000000
# float  — decimal numbers:     3.14, -0.5, 2.0
# str    — text in quotes:      "hello", 'world', "42"
# bool   — True or False:       True, False
# None   — means "no value":    None

# Use type() to check what type something is:
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type(None))        # <class 'NoneType'>


# ──────────────────────────────────────────────
# PART 3: Type conversions (casting)
# ──────────────────────────────────────────────

# Sometimes you need to convert between types.

# String to int (you'll do this a LOT when reading input)
x = int("42")           # x is now the integer 42
print(x + 8)            # 50

# String to float
pi = float("3.14")      # pi is now the float 3.14
print(pi)               # 3.14

# Int to float
y = float(7)             # y is now 7.0
print(y)                 # 7.0

# Float to int (truncates — chops off the decimal, does NOT round!)
z = int(3.99)            # z is 3, NOT 4!
print(z)                 # 3

# Anything to string
s = str(42)              # s is now the string "42"
print("The answer is " + s)  # string concatenation


# ──────────────────────────────────────────────
# PART 4: Operators
# ──────────────────────────────────────────────

# Arithmetic operators work on numbers:
print(10 + 3)    # 13   (addition)
print(10 - 3)    # 7    (subtraction)
print(10 * 3)    # 30   (multiplication)
print(10 / 3)    # 3.33... (true division — always gives a float!)
print(10 // 3)   # 3    (floor division — rounds down to integer)
print(10 % 3)    # 1    (modulo — the remainder)
print(10 ** 3)   # 1000 (exponent — 10 to the power of 3)

# IMPORTANT: / always gives a float, even if the result is a whole number!
print(10 / 2)    # 5.0  (not 5)
print(10 // 2)   # 5    (use // when you want an integer result)


# ──────────────────────────────────────────────
# PART 5: The modulo trick (super useful in CP!)
# ──────────────────────────────────────────────

# The % (modulo) operator gives you the remainder after division.
# This is incredibly useful in competitive programming!

n = 12345

# Get the last digit of any number:
last_digit = n % 10      # 5
print("Last digit:", last_digit)

# Check if a number is even or odd:
print(7 % 2)   # 1 → odd
print(8 % 2)   # 0 → even

# Get the last two digits:
last_two = n % 100       # 45
print("Last two digits:", last_two)


# ──────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────
#
# 1. Python has 5 basic types: int, float, str, bool, None
# 2. Use type(x) to check a variable's type
# 3. Convert types with int(), float(), str(), bool()
# 4. int(3.99) gives 3, NOT 4 — it truncates!
# 5. / always returns float; use // for integer division
# 6. % (modulo) is your best friend — last digit, even/odd, etc.
