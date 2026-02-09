"""
Practice 2: Range Max Query with Point Update
=============================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return results of range max queries with point updates.

EXAMPLES
--------
  solve([3, 1, 4, 1, 5, 9, 2, 6], [[1, 0, 7], [2, 5, 1], [1, 0, 7]]) -> [9, 6]
  solve([1, 2, 3], [[1, 0, 2], [2, 1, 5], [1, 0, 2]]) -> [3, 5]
  solve([10], [[1, 0, 0], [2, 0, 20], [1, 0, 0]]) -> [10, 20]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Segment tree with max operation. Identity is -infinity.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return results of range max queries with point updates."""
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
