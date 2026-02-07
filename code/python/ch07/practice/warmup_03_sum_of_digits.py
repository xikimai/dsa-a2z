"""
Warmup 3: Sum of Digits
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given an integer n, return the sum of its digits.
Use the absolute value of n (ignore the sign).

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single integer: the sum of the digits of |n|.

CONSTRAINTS
-----------
- -10^9 <= n <= 10^9

EXAMPLES
--------
Input:
  12345
Output: 15

Input:
  0
Output: 0

Input:
  -456
Output: 15

Input:
  999
Output: 27

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the sum of digits of n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
