"""
Warmup 02: Rectangle Area
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given the length and width of a rectangle, compute its area.

INPUT FORMAT
------------
A single line containing two space-separated integers: length and width.

OUTPUT FORMAT
-------------
Print a single integer — the area of the rectangle.

CONSTRAINTS
-----------
1 <= length, width <= 10^4

EXAMPLES
--------
Input:  5 3
Output: 15

Input:  1 1
Output: 1

Input:  100 200
Output: 20000

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(length: int, width: int) -> int:
    """Return the area of a rectangle with the given length and width."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    length, width = map(int, input().split())
    print(solve(length, width))
