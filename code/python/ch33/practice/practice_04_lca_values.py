"""
Practice 4: LCA Queries with Node Values
========================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the value at the LCA for each query [u, v].

EXAMPLES
--------
  solve(5, [10,20,30,40,50], [[0,1],[0,2],[1,3],[1,4]], [[3,4],[3,2]]) -> [20, 10]
  solve(3, [5,10,15], [[0,1],[0,2]], [[1,2]]) -> [5]
  solve(3, [5,10,15], [[0,1],[0,2]], [[1,1]]) -> [10]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Binary lifting for LCA, then return values[lca_node] for each query.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import math
from collections import deque


def solve(n: int, values: list[int], edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """Return the value at the LCA for each query [u, v]."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    vals = []
    for _ in range(n):
        vals.append(int(tokens[idx])); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        queries.append([u, v])
    result = solve(n, vals, edges, queries)
    print(" ".join(map(str, result)))
