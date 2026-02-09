"""
Practice 3: Point in Polygon
============================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return True/False for each query point.

EXAMPLES
--------
  solve(polygon, queries) -> [True, False, True, True]
  solve(polygon, queries) -> [True, False]
  solve(polygon, queries) -> [True, True, True]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
For each query point: 1. Check if the point lies on any edge (boundary check)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(polygon: list[list[int]], queries: list[list[int]]) -> list[bool]:
    """Return True/False for each query point."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data["polygon"], data["queries"])))
