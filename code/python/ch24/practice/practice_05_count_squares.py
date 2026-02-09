"""
Practice 5: Count Square Submatrices
====================================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the total number of square submatrices with all ones.

EXAMPLES
--------
  solve([[1, 1], [1, 1]]) -> 5
  solve([[0, 0], [0, 0]]) -> 0
  solve([[1]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Same DP as Maximal Square, but sum all dp values. dp[j] at (i,j) gives the side of the largest square ending there, which equals

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the total number of square submatrices with all ones."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
