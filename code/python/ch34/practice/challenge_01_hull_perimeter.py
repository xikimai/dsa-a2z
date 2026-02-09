"""
Challenge 1: Convex Hull Perimeter
==================================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return the perimeter of the convex hull.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Compute convex hull using Andrew's Monotone Chain 2. Sum Euclidean distances between consecutive hull vertices

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import math


def solve(points: list[list[int]]) -> float:
    """Return the perimeter of the convex hull."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
