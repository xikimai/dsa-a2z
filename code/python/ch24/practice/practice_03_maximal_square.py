"""
Practice 3: Maximal Square
==========================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the area of the largest square of all 1s.

EXAMPLES
--------
  solve([[0, 1], [1, 0]]) -> 1
  solve([[0]]) -> 0
  solve([[1, 1], [1, 1]]) -> 4

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized 1D DP. dp[j] = side length of largest square with bottom-right at (i,j). Track prev_diag for dp[i-1][j-1].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the area of the largest square of all 1s."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
