"""
Challenge 2: Distinct Values in Range (Offline + BIT)
=====================================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return count of distinct values in arr[l..r] for each query.

EXAMPLES
--------
  solve([1, 2, 1, 3, 2, 1], [[0, 5], [0, 2], [3, 5]]) -> [3, 2, 3]
  solve([1, 1, 1], [[0, 2]]) -> [1]
  solve([1, 2, 3, 4], [[0, 3], [1, 2]]) -> [4, 2]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Process queries offline sorted by right endpoint. Maintain a BIT where bit[i] = 1 if arr[i] is the latest occurrence

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return count of distinct values in arr[l..r] for each query."""
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
