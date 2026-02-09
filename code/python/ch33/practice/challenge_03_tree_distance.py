"""
Challenge 3: Tree Distance Queries (Binary Lifting)
===================================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the distance between u and v for each query.

EXAMPLES
--------
  solve(5, [[0,1,2],[0,2,3],[1,3,4],[1,4,1]], [[3,4],[3,2]]) -> [5, 9]
  solve(3, [[0,1,5],[0,2,10]], [[1,2]]) -> [15]
  solve(3, [[0,1,5],[0,2,10]], [[1,1]]) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. BFS from root to compute dist[v] = distance from root to v. 2. Binary lifting for LCA.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import math
from collections import deque


def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """Return the distance between u and v for each query."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        w = int(tokens[idx]); idx += 1
        edges.append([u, v, w])
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        queries.append([u, v])
    result = solve(n, edges, queries)
    print(" ".join(map(str, result)))
