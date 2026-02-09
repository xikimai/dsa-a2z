"""
Challenge 1: Range Update Range Query (Set, Lazy Segment Tree)
==============================================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return results of range sum queries with range set updates.

EXAMPLES
--------
  solve(5, [[1, 0, 4, 3], [2, 0, 4], [1, 1, 3, 5], [2, 0, 4]]) -> [15, 21]
  solve(3, [[1, 0, 2, 10], [2, 0, 2], [1, 1, 1, 0], [2, 0, 2]]) -> [30, 20]
  solve(1, [[1, 0, 0, 7], [2, 0, 0], [1, 0, 0, 3], [2, 0, 0]]) -> [7, 3]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Lazy segment tree with "set" operation. Lazy value stores the value to set (use None / sentinel to mean "no pending set"). When pushing

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, queries: list[list[int]]) -> list[int]:
    """Return results of range sum queries with range set updates."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        t = int(tokens[idx]); idx += 1
        if t == 1:
            l = int(tokens[idx]); idx += 1
            r = int(tokens[idx]); idx += 1
            v = int(tokens[idx]); idx += 1
            queries.append([t, l, r, v])
        else:
            l = int(tokens[idx]); idx += 1
            r = int(tokens[idx]); idx += 1
            queries.append([t, l, r])
    for r in solve(n, queries):
        print(r)
