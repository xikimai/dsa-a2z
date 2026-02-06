"""
Challenge 01: Diamond Pattern
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given a positive integer n, return a diamond pattern of stars. The top
half (including the middle row) has n rows. The total height is 2n - 1.
Each row has leading spaces followed by an odd number of stars.
No trailing spaces on any row. Rows separated by newlines.
No trailing newline.

INPUT FORMAT
------------
A single line containing a positive integer n.

OUTPUT FORMAT
-------------
Print the diamond pattern.

CONSTRAINTS
-----------
1 <= n <= 50

EXAMPLES
--------
Input:  3
Output:
  *
 ***
*****
 ***
  *

Input:  1
Output:
*

Input:  2
Output:
 *
***
 *

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> str:
    """Return a diamond pattern of stars with n rows in the top half."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
