"""
Practice 03: Reverse Number
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given an integer n, reverse its digits. For negative numbers, reverse the
digits and keep the negative sign. Leading zeros in the reversed result
should be dropped (e.g., 1200 reversed is 21, not 0021).

INPUT FORMAT
------------
A single line containing an integer n.

OUTPUT FORMAT
-------------
Print the reversed integer.

CONSTRAINTS
-----------
-10^9 <= n <= 10^9

EXAMPLES
--------
Input:  1234
Output: 4321

Input:  1200
Output: 21

Input:  5
Output: 5

Input:  -123
Output: -321

Input:  0
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the integer with its digits reversed."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
