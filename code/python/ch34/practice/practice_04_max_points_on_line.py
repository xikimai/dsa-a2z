"""
Practice 4: Maximum Points on a Line
====================================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return maximum number of collinear points.

EXAMPLES
--------
  solve([[1, 1], [2, 2], [3, 3], [4, 1]]) -> 3
  solve([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) -> 4
  solve([[0, 0]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
For each point i, compute the slope to every other point j. Use GCD-normalized (dx, dy) as slope key to avoid floating point.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from math import gcd


def solve(points: list[list[int]]) -> int:
    """Return maximum number of collinear points."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
