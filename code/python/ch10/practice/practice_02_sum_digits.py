"""
Practice 2: Sum of Digits
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Given an integer n, return the sum of the digits of |n| (absolute value
of n) using recursion.

For example, sum_digits(-123) = 1 + 2 + 3 = 6.

INPUT FORMAT
------------
A single integer n (may be negative).

OUTPUT FORMAT
-------------
A single integer — the sum of the digits of |n|.

CONSTRAINTS
-----------
- -10^9 <= n <= 10^9

EXAMPLES
--------
Input:
  123
Output: 6

Input:
  -456
Output: 15

Input:
  0
Output: 0

HINT
----
First take the absolute value of n. Base case: if n < 10, return n
(it's a single digit). Recursive case: last digit is n % 10, and
the remaining digits come from n // 10.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Sum the digits of |n| recursively."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
