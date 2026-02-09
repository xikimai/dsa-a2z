"""
Warmup 1: Cross Product and Orientation
=======================================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return orientation for each triplet of points.

EXAMPLES
--------
  solve(queries) -> [1, -1, 0]
  solve(queries) -> [1]
  solve(queries) -> [0, 0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
For each triplet (A, B, C), compute the cross product of vectors AB and AC. The sign tells the orientation.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(queries: list[list[list[int]]]) -> list[int]:
    """Return orientation for each triplet of points."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(json.dumps(solve(data)))
