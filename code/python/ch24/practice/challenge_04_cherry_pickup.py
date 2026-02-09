"""
Challenge 4: Cherry Pickup I (3D DP)
====================================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the maximum cherries collected on a round trip.

EXAMPLES
--------
  solve([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) -> 5
  solve([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) -> 0
  solve([[1]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Model as two people walking simultaneously from (0,0) to (n-1,n-1). After t steps, person 1 is at (r1, c1=t-r1), person 2 at (r2, c2=t-r2).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the maximum cherries collected on a round trip."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
