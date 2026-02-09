"""
Practice 2: Line Segment Intersection
=====================================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return True/False for each pair of segments.

EXAMPLES
--------
  solve(segments) -> [True, False, False]
  solve(segments) -> [True]
  solve(segments) -> [False]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
For each pair of segments AB and CD: 1. Compute orientations d1=orientation(C,D,A), d2=orientation(C,D,B),

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(segments: list[list[list[int]]]) -> list[bool]:
    """Return True/False for each pair of segments."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data)))
