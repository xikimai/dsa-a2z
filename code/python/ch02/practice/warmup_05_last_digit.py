"""
Warmup 05: Last Digit
==============================
Chapter 2: Your First Programs

PROBLEM
-------
Given an integer n, return its last digit. If n is negative, return the
last digit of its absolute value.

INPUT FORMAT
------------
A single line containing an integer n.

OUTPUT FORMAT
-------------
Print a single integer — the last digit of n.

CONSTRAINTS
-----------
-10^9 <= n <= 10^9

EXAMPLES
--------
Input:  12345
Output: 5

Input:  100
Output: 0

Input:  -789
Output: 9

Input:  7
Output: 7

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the last digit of n (always non-negative)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
