"""
Practice 3: Count of Elements in Range
======================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return count of elements in arr[l..r] within [lo, hi] for each query.

EXAMPLES
--------
  solve([10, 20, 30], [[0, 2, 15, 25]]) -> [1]
  solve([1, 2, 3], [[0, 2, 10, 20]]) -> [0]
  solve([5, 5, 5], [[0, 2, 5, 5]]) -> [3]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Merge sort tree: build a segment tree where each node stores a sorted list of elements in its range. To count elements in [lo, hi] within

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from bisect import bisect_left, bisect_right


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return count of elements in arr[l..r] within [lo, hi] for each query."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    arr = [int(tokens[idx + i]) for i in range(n)]; idx += n
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        l = int(tokens[idx]); idx += 1
        r = int(tokens[idx]); idx += 1
        lo = int(tokens[idx]); idx += 1
        hi = int(tokens[idx]); idx += 1
        queries.append([l, r, lo, hi])
    for r in solve(arr, queries):
        print(r)
