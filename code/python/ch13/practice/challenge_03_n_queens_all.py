"""
Challenge 3: N-Queens All Solutions
=====================================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given an integer n, return all distinct solutions to the N-Queens puzzle.
Each solution is a list of strings where 'Q' represents a queen and '.'
represents an empty space. Return solutions in sorted order.

INPUT FORMAT
------------
A single positive integer n.

OUTPUT FORMAT
-------------
Each solution as n lines of the board, with a blank line between solutions.

CONSTRAINTS
-----------
- 1 <= n <= 10

EXAMPLES
--------
Input:
  4
Output:
  .Q..
  ...Q
  Q...
  ..Q.

  ..Q.
  Q...
  ...Q
  .Q..

Input:
  1
Output:
  Q

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[list[str]]:
    """Return all N-Queens solutions as lists of strings."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    result = solve(n)
    for solution in result:
        for row in solution:
            print(row)
        print()

