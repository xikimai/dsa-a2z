"""
Warmup 3: Prefix Sum with BIT (Fenwick Tree)
============================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return results of prefix sum queries with point add updates.

EXAMPLES
--------
  solve([1, 2, 3, 4, 5], [[1, 3, 0], [2, 2, 5], [1, 3, 0]]) -> [10, 15]
  solve([3, 1, 4, 1, 5], [[1, 4, 0], [2, 0, 2], [1, 4, 0]]) -> [14, 16]
  solve([7], [[1, 0, 0], [2, 0, 3], [1, 0, 0]]) -> [7, 10]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Fenwick tree (BIT) with 1-indexed internal storage. - type 1: prefix sum query (0..l)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return results of prefix sum queries with point add updates."""
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
