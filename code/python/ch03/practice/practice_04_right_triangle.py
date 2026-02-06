"""
Practice 04: Right Triangle
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given a positive integer n, return a right-aligned triangle of stars
with n rows as a single string. Row i (1-indexed) has (n - i) spaces
followed by i stars. Rows are separated by newlines. No trailing newline.

INPUT FORMAT
------------
A single line containing a positive integer n.

OUTPUT FORMAT
-------------
Print the right-aligned triangle.

CONSTRAINTS
-----------
1 <= n <= 50

EXAMPLES
--------
Input:  4
Output:
   *
  **
 ***
****

Input:  1
Output:
*

Input:  3
Output:
  *
 **
***

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> str:
    """Return a right-aligned triangle of stars with n rows."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
