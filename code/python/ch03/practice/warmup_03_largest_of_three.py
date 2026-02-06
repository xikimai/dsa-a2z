"""
Warmup 03: Largest of Three
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given three integers a, b, and c, return the largest of the three.

INPUT FORMAT
------------
A single line containing three space-separated integers a, b, c.

OUTPUT FORMAT
-------------
Print the largest of the three integers.

CONSTRAINTS
-----------
-10^9 <= a, b, c <= 10^9

EXAMPLES
--------
Input:  1 2 3
Output: 3

Input:  3 2 1
Output: 3

Input:  5 5 5
Output: 5

Input:  -1 -2 -3
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(a: int, b: int, c: int) -> int:
    """Return the largest of three integers."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
