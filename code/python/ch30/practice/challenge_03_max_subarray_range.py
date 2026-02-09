"""
Challenge 3: Maximum Subarray Sum in Range (Segment Tree)
=========================================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return max subarray sum in arr[l..r] for each query.

EXAMPLES
--------
  solve([-1, -2, -3], [[0, 2]]) -> [-1]
  solve([5], [[0, 0]]) -> [5]
  solve([-5], [[0, 0]]) -> [-5]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Each segment tree node stores 4 values: - total: sum of all elements in the range

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return max subarray sum in arr[l..r] for each query."""
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
        queries.append([l, r])
    for r in solve(arr, queries):
        print(r)
