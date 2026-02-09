"""
Practice 4: Kth Order Statistics (Segment Tree on Values)
=========================================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return results of kth-smallest queries on a dynamic multiset.

EXAMPLES
--------
  solve([[1, 5], [1, 3], [1, 7], [1, 1], [3, 2], [2, 3], [3, 2]]) -> [3, 5]
  solve([[1, 10], [3, 1]]) -> [10]
  solve([[1, 5], [1, 5], [3, 1], [3, 2], [2, 5], [3, 1]]) -> [5, 5, 5]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build a segment tree over the value range [1, MAX_VAL]. Each node stores the count of elements in that value range. To find kth smallest, walk

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(queries: list[list[int]]) -> list[int]:
    """Return results of kth-smallest queries on a dynamic multiset."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        t = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        queries.append([t, v])
    for r in solve(queries):
        print(r)
