"""
Practice 4: Cherry Pickup II
============================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the maximum cherries collected by both robots.

EXAMPLES
--------
  solve([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]) -> 24
  solve([[1, 1], [1, 1]]) -> 4

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
3D DP bottom-up. dp[c1][c2] = max cherries from current row to last row, with robot 1 at column c1 and robot 2 at column c2.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the maximum cherries collected by both robots."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
