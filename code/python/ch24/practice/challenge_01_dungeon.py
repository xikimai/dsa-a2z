"""
Challenge 1: Dungeon Game
=========================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the minimum initial health to reach the bottom-right.

EXAMPLES
--------
  solve([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) -> 7
  solve([[0]]) -> 1
  solve([[100]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Reverse DP from bottom-right to top-left. dp[j] = minimum health needed at cell (i,j) to survive to the end.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(dungeon: List[List[int]]) -> int:
    """Return the minimum initial health to reach the bottom-right."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    dungeon = json.loads(sys.stdin.readline())
    print(solve(dungeon))
