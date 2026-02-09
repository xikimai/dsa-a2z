"""
Challenge 3: Rectangle Union Area (Sweep Line)
==============================================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return total area of union of rectangles.

EXAMPLES
--------
  solve([[0, 0, 2, 2], [1, 1, 3, 3]]) -> 7
  solve([[0, 0, 1, 1], [2, 2, 3, 3]]) -> 2
  solve([[0, 0, 10, 10], [1, 1, 9, 9]]) -> 100

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Sweep line with coordinate compression: 1. Collect all y-coordinates and compress them

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(rectangles: list[list[int]]) -> int:
    """Return total area of union of rectangles."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
