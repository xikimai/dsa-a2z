"""
Example 02: Loops and Patterns
=====================================
Chapter 3: Decisions and Loops

This example covers for loops, while loops, nested loops, break/continue,
and how to print simple patterns. Loops are how you make the computer
repeat work — one of the most powerful ideas in programming.
"""

# ──────────────────────────────────────────────
# PART 1: for loops — repeat a known number of times
# ──────────────────────────────────────────────

# range(n) gives you 0, 1, 2, ..., n-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()  # newline

# range(start, stop) — from start up to (but NOT including) stop
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

# range(start, stop, step) — with a step size
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# Counting backwards
for i in range(5, 0, -1):
    print(i, end=" ")  # 5 4 3 2 1
print()


# ──────────────────────────────────────────────
# PART 2: while loops — repeat until a condition is False
# ──────────────────────────────────────────────

# Use while when you don't know how many iterations you need.

n = 5
total = 0
while n > 0:
    total += n
    n -= 1
print(f"Sum: {total}")  # Sum: 15

# DANGER: If you forget to change the condition variable, you get
# an infinite loop! Always make sure the condition will eventually
# become False.

# while True:   ← This would run FOREVER! Don't do this unless you
#     ...         have a break statement inside.


# ──────────────────────────────────────────────
# PART 3: break and continue — loop control
# ──────────────────────────────────────────────

# break — immediately exits the loop
print("Finding first multiple of 7 above 50:")
for i in range(51, 100):
    if i % 7 == 0:
        print(f"Found it: {i}")  # Found it: 56
        break  # stop searching

# continue — skips the rest of THIS iteration, goes to the next one
print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i, end=" ")  # 1 3 5 7 9
print()


# ──────────────────────────────────────────────
# PART 4: Nested loops — loops inside loops
# ──────────────────────────────────────────────

# The inner loop runs COMPLETELY for each iteration of the outer loop.

# A 3x4 grid of coordinates:
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()  # newline after each row
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)


# ──────────────────────────────────────────────
# PART 5: Simple pattern — left-aligned triangle
# ──────────────────────────────────────────────

# Print a triangle of stars:
# *
# **
# ***
# ****

n = 4
for i in range(1, n + 1):
    print("*" * i)

# The * operator repeats a string: "*" * 3 gives "***"
# This is a super useful trick for pattern problems!


# ──────────────────────────────────────────────
# PART 6: Accumulator pattern — building up a result
# ──────────────────────────────────────────────

# The accumulator pattern: start with an empty result,
# add to it in each iteration.

# Example: build a list of squares
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)  # [1, 4, 9, 16, 25]

# Same thing with a list comprehension (more Pythonic):
squares = [i * i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


# ──────────────────────────────────────────────
# PART 7: Common loop idioms for CP
# ──────────────────────────────────────────────

# Sum of a range:
total = sum(range(1, 101))  # 1 + 2 + ... + 100 = 5050
print(f"Sum 1 to 100: {total}")

# Enumerate — get both index AND value:
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Zip — loop over two lists at the same time:
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")


# ──────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────
#
# 1. for i in range(n) — repeat n times (0 to n-1)
# 2. range(start, stop, step) — flexible counting
# 3. while condition — repeat until condition is False
# 4. break — exit loop early; continue — skip to next iteration
# 5. Nested loops — inner loop runs fully for each outer iteration
# 6. "*" * n — repeat a string n times (great for patterns)
# 7. Accumulator pattern — build results in a loop
