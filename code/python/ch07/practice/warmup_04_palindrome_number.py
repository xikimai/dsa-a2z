"""
Warmup 4: Palindrome Number
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given an integer n, return True if n is a palindrome number, False otherwise.
A palindrome number reads the same forwards and backwards.
Negative numbers are NOT palindromes (e.g., -121 is not a palindrome).

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
  121
Output: True

Input:
  -121
Output: False

Input:
  10
Output: False

Input:
  0
Output: True

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> bool:
    """Return True if n is a palindrome number."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
