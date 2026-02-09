"""
Challenge 2: Maximum Rectangle in Histogram
===========================================
Chapter 34: Computational Geometry & Sweep Line

PROBLEM
-------
Return area of largest rectangle in histogram.

EXAMPLES
--------
  solve([2, 1, 5, 6, 2, 3]) -> 10
  solve([2, 4]) -> 4
  solve([1]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Stack-based sweep: maintain a stack of indices in increasing height order. When a shorter bar is encountered, pop and compute the area of the

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(heights: list[int]) -> int:
    """Return area of largest rectangle in histogram."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
