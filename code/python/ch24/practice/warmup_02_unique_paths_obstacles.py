"""
Warmup 2: Unique Paths with Obstacles
=====================================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return number of unique paths avoiding obstacles.

EXAMPLES
--------
  solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) -> 2
  solve([[0, 1], [0, 0]]) -> 1
  solve([[1, 0]]) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized 1D DP. Set dp[j] = 0 for obstacles. For first row, propagate left; then row by row, dp[j] += dp[j-1]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return number of unique paths avoiding obstacles."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
