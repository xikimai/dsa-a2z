"""
Warmup 5: Armstrong Number
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given an integer n, return True if n is an Armstrong (narcissistic) number,
False otherwise. An Armstrong number is a number where the sum of its digits
each raised to the power of the total number of digits equals the number itself.

For example, 153 is an Armstrong number because:
  153 has 3 digits, and 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Negative numbers are NOT Armstrong numbers.
Single-digit numbers (0-9) are all Armstrong numbers.

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single value: True or False.

CONSTRAINTS
-----------
- -10^9 <= n <= 10^9

EXAMPLES
--------
Input:
  153
Output: True

Input:
  370
Output: True

Input:
  9474
Output: True

Input:
  100
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> bool:
    """Return True if n is an Armstrong number."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
