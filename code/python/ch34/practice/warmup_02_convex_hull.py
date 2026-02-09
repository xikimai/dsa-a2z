"""
Warmup 2: Convex Hull
=====================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return convex hull vertices in CCW order.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Andrew's Monotone Chain algorithm: 1. Sort points by (x, y)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(points: list[list[int]]) -> list[list[int]]:
    """Return convex hull vertices in CCW order."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data)))
