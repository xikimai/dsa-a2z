"""
Challenge 2: Maximal Rectangle
==============================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the area of the largest rectangle of all 1s.

EXAMPLES
--------
  solve([[0]]) -> 0
  solve([[1]]) -> 1
  solve([[1, 1], [1, 1]]) -> 4

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build a histogram of heights row by row. For each row, compute the largest rectangle in the histogram using a stack. Take the

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the area of the largest rectangle of all 1s."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
