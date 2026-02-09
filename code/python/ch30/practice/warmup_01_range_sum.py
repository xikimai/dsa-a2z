"""
Warmup 1: Range Sum Query (Segment Tree)
========================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return results of range sum queries with point updates.

EXAMPLES
--------
  solve([1, 3, 5, 7, 9, 11], [[1, 1, 3], [2, 1, 10], [1, 1, 3]]) -> [15, 22]
  solve([1, 2, 3, 4, 5], [[1, 0, 4], [2, 2, 10], [1, 0, 4]]) -> [15, 22]
  solve([5], [[1, 0, 0], [2, 0, 3], [1, 0, 0]]) -> [5, 3]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build a segment tree for sum queries. Process queries: - type 1 (sum): query the tree for range [l, r]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return results of range sum queries with point updates."""
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
        t = int(tokens[idx]); idx += 1
        a = int(tokens[idx]); idx += 1
        b = int(tokens[idx]); idx += 1
        queries.append([t, a, b])
    for r in solve(arr, queries):
        print(r)
