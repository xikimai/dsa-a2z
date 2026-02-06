"""
Solution for Practice 1: Calculator
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Define four helper functions (add, subtract, multiply, divide), then use
a dictionary to dispatch to the correct one based on the operator string.
Return None for division by zero or unknown operators.

TIME COMPLEXITY:  O(1)
SPACE COMPLEXITY: O(1)
"""


def add(a: int, b: int) -> int:
    """Return a + b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return a - b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return a * b."""
    return a * b


def divide(a: int, b: int) -> int | None:
    """Return a // b, or None if b is zero."""
    if b == 0:
        return None
    return a // b


def solve(a: int, op: str, b: int) -> int | None:
    """Dispatch to the correct operation based on op."""
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return None


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a = int(input())
    op = input().strip()
    b = int(input())
    print(solve(a, op, b))
