"""
Challenge 01: Extract Digits
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given a 3-digit integer n, extract its hundreds digit, tens digit, and
ones digit. Use integer division and modulo — no string tricks allowed!

INPUT FORMAT
------------
A single line containing a 3-digit integer n.

OUTPUT FORMAT
-------------
Print three space-separated integers: hundreds, tens, ones.

CONSTRAINTS
-----------
100 <= n <= 999

EXAMPLES
--------
Input:  123
Output: 1 2 3

Input:  907
Output: 9 0 7

Input:  100
Output: 1 0 0

Input:  999
Output: 9 9 9

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> tuple[int, int, int]:
    """Return a tuple (hundreds, tens, ones) for a 3-digit number n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    h, t, o = solve(n)
    print(h, t, o)
