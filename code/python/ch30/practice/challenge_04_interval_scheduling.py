"""
Challenge 4: Interval Scheduling
================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return max number of non-overlapping intervals.

EXAMPLES
--------
  solve([[1, 3], [2, 5], [4, 7], [6, 9]]) -> 2
  solve([[1, 2], [2, 3], [3, 4], [4, 5]]) -> 4
  solve([[1, 10], [2, 3], [4, 5], [6, 7]]) -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Classic greedy: sort intervals by end time. Greedily pick the interval that ends earliest and does not overlap with the previously picked one.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(intervals: list[list[int]]) -> int:
    """Return max number of non-overlapping intervals."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    intervals = []
    for _ in range(n):
        s = int(tokens[idx]); idx += 1
        e = int(tokens[idx]); idx += 1
        intervals.append([s, e])
    print(solve(intervals))
