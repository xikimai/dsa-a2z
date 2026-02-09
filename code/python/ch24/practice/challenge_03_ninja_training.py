"""
Challenge 3: Ninja Training
===========================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the maximum total points the ninja can earn.

EXAMPLES
--------
  solve([[10, 40, 70], [20, 50, 80], [30, 60, 90]]) -> 210
  solve([[1, 2, 5], [3, 1, 1], [3, 3, 3]]) -> 11
  solve([[10, 10, 10]]) -> 10

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized DP. Track prev[0], prev[1], prev[2] = best total points ending with activity 0, 1, 2 on the previous day. For each new day,

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from typing import List


def solve(points: List[List[int]]) -> int:
    """Return the maximum total points the ninja can earn."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    points = json.loads(sys.stdin.readline())
    print(solve(points))
