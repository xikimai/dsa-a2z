"""
Warmup 3: Min of Three (Using a Helper)
==============================
Chapter 4: Functions

PROBLEM
-------
Find the minimum of three integers. You MUST define a helper function
called min_of_two(a, b) that returns the smaller of two values, then
use it inside solve() to find the minimum of three.

INPUT FORMAT
------------
Three integers on separate lines.

OUTPUT FORMAT
-------------
A single integer: the smallest of the three.

CONSTRAINTS
-----------
- All values are integers (can be negative)

EXAMPLES
--------
Input:  5, 2, 8
Output: 2

Input:  -1, -5, 3
Output: -5

Input:  4, 4, 4
Output: 4

INSTRUCTIONS
------------
Replace the `pass` in both min_of_two() and solve() with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def min_of_two(a: int, b: int) -> int:
    """Return the smaller of a and b."""
    pass  # TODO: Replace this with your solution


def solve(a: int, b: int, c: int) -> int:
    """Return the minimum of a, b, and c using min_of_two."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(solve(a, b, c))
