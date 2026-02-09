"""
Warmup 2: Range Min Query (Segment Tree)
========================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return results of range min queries with point updates.

EXAMPLES
--------
  solve([2, 5, 1, 4, 9, 3], [[1, 0, 5], [2, 2, 8], [1, 0, 5]]) -> [1, 2]
  solve([7, 3, 8, 1, 6], [[1, 1, 3], [2, 3, 2], [1, 1, 3]]) -> [1, 2]
  solve([5], [[1, 0, 0], [2, 0, 2], [1, 0, 0]]) -> [5, 2]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Segment tree with min operation. Identity element is float('inf').

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return results of range min queries with point updates."""
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
