"""
Warmup 4: Triangle Minimum Total
================================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the minimum path sum from top to bottom of the triangle.

EXAMPLES
--------
  solve([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) -> 11
  solve([[-10]]) -> -10
  solve([[-1], [2, 3], [1, -1, -3]]) -> -1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Bottom-up DP. Start from the last row, work upward. dp[j] = triangle[i][j] + min(dp[j], dp[j+1]).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(triangle: List[List[int]]) -> int:
    """Return the minimum path sum from top to bottom of the triangle."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    triangle = json.loads(sys.stdin.readline())
    print(solve(triangle))
