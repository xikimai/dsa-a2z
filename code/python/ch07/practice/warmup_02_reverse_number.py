"""
Warmup 2: Reverse a Number
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given an integer n, return the number formed by reversing its digits.
Preserve the sign (negative numbers stay negative).
Leading zeros in the reversed result are dropped (e.g., 1200 -> 21).

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single integer: the reversed number.

CONSTRAINTS
-----------
- -10^9 <= n <= 10^9

EXAMPLES
--------
Input:
  12345
Output: 54321

Input:
  -123
Output: -321

Input:
  1200
Output: 21

Input:
  0
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the reversed number."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
