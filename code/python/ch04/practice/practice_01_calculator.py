"""
Practice 1: Calculator
==============================
Chapter 4: Functions

PROBLEM
-------
Build a mini calculator. Define separate helper functions for add,
subtract, multiply, and divide. The solve function dispatches to the
correct helper based on the operator string.

INPUT FORMAT
------------
Three values on separate lines: int a, string op, int b.
op is one of: "+", "-", "*", "/"

OUTPUT FORMAT
-------------
The integer result, or "None" for division by zero or invalid operator.

CONSTRAINTS
-----------
- a, b are integers
- op is a single-character string
- For division, use integer division (//)
- Division by zero returns None
- Invalid operator returns None

EXAMPLES
--------
Input:  10, +, 3
Output: 13

Input:  10, /, 0
Output: None

Input:  10, ^, 3
Output: None

INSTRUCTIONS
------------
Replace the `pass` in each helper function and solve() with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def add(a: int, b: int) -> int:
    """Return a + b."""
    pass  # TODO: Replace this with your solution


def subtract(a: int, b: int) -> int:
    """Return a - b."""
    pass  # TODO: Replace this with your solution


def multiply(a: int, b: int) -> int:
    """Return a * b."""
    pass  # TODO: Replace this with your solution


def divide(a: int, b: int) -> int | None:
    """Return a // b, or None if b is zero."""
    pass  # TODO: Replace this with your solution


def solve(a: int, op: str, b: int) -> int | None:
    """Dispatch to the correct operation based on op."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a = int(input())
    op = input().strip()
    b = int(input())
    print(solve(a, op, b))
