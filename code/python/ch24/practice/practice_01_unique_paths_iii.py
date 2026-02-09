"""
Practice 1: Unique Paths III
============================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the number of paths visiting every non-obstacle cell exactly once.

EXAMPLES
--------
  solve([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) -> 2
  solve([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) -> 4
  solve([[0, 1], [2, 0]]) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Backtracking/DFS. Count empty cells (including start). DFS from start, marking cells visited. When reaching end, check if all cells visited.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the number of paths visiting every non-obstacle cell exactly once."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
