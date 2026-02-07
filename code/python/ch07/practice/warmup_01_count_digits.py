"""
Warmup 1: Count Digits
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given an integer n, return the number of digits in n.
Use the absolute value of n (ignore the sign).
The number 0 has 1 digit.

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single integer: the number of digits in n.

CONSTRAINTS
-----------
- -10^9 <= n <= 10^9

EXAMPLES
--------
Input:
  12345
Output: 5

Input:
  0
Output: 1

Input:
  -42
Output: 2

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the number of digits in n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
