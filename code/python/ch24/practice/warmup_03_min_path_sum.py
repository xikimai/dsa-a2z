"""
Warmup 3: Minimum Path Sum
==========================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the minimum path sum from top-left to bottom-right.

EXAMPLES
--------
  solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) -> 7
  solve([[1, 2, 3]]) -> 6
  solve([[1], [2], [3]]) -> 6

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized 1D DP. dp[j] = min(dp[j], dp[j-1]) + grid[i][j]. First row: accumulate. Then row by row.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the minimum path sum from top-left to bottom-right."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
