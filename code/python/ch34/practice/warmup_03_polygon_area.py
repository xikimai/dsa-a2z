"""
Warmup 3: Polygon Area (Shoelace Formula)
=========================================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return the area of a simple polygon.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Shoelace formula: Area = |sum(x_i * y_{i+1} - x_{i+1} * y_i)| / 2

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(polygon: list[list[int]]) -> float:
    """Return the area of a simple polygon."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
