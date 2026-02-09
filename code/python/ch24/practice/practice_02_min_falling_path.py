"""
Practice 2: Minimum Falling Path Sum
====================================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the minimum falling path sum.

EXAMPLES
--------
  solve([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) -> 13
  solve([[-19, 57], [-40, -5]]) -> -59
  solve([[-48]]) -> -48

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized bottom-up DP. For each row, compute new dp values using the previous row. dp[j] = matrix[i][j] + min of up to 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the minimum falling path sum."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
