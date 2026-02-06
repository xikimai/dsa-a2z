"""
Practice 02: Digit Count
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given an integer n, count the number of digits it has.
For n = 0, the answer is 1.
Handle negative numbers by counting the digits of the absolute value.

INPUT FORMAT
------------
A single line containing an integer n.

OUTPUT FORMAT
-------------
Print the number of digits in n.

CONSTRAINTS
-----------
-10^9 <= n <= 10^9

EXAMPLES
--------
Input:  12345
Output: 5

Input:  0
Output: 1

Input:  9
Output: 1

Input:  -42
Output: 2

Input:  1000000
Output: 7

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
    n = int(input())
    print(solve(n))
