"""
Practice 5: XOR on Range (Segment Tree)
=======================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return results of range XOR queries with point updates.

EXAMPLES
--------
  solve([1, 2, 3, 4, 5], [[1, 0, 4], [2, 2, 7], [1, 0, 4]]) -> [1, 5]
  solve([3, 5], [[1, 0, 1], [2, 0, 6], [1, 0, 1]]) -> [6, 3]
  solve([42], [[1, 0, 0]]) -> [42]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Segment tree with XOR operation. Identity element is 0.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return results of range XOR queries with point updates."""
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
