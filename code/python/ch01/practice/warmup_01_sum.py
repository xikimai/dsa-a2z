"""
Warmup 01: Sum of Two Numbers
==============================
Chapter 1: The Coder's Toolkit

PROBLEM
-------
Given two integers, print their sum.

INPUT FORMAT
------------
A single line containing two space-separated integers a and b.

OUTPUT FORMAT
-------------
Print a single integer — the sum of a and b.

CONSTRAINTS
-----------
-10^6 <= a, b <= 10^6

EXAMPLES
--------
Input:  1 2
Output: 3

Input:  0 0
Output: 0

Input:  -5 5
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(a: int, b: int) -> int:
    """Return the sum of a and b."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(solve(a, b))
