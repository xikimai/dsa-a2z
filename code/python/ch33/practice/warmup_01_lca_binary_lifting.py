"""
Warmup 1: LCA with Binary Lifting
=================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the LCA for each query [u, v] using binary lifting.

EXAMPLES
--------
  solve(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [[3,4],[3,6],[5,6]]) -> [1, 0, 2]
  solve(3, [[0,1],[1,2]], [[1,2],[0,2]]) -> [1, 0]
  solve(3, [[0,1],[0,2]], [[1,1]]) -> [1]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Binary lifting: BFS to compute depths and parents, then fill up[v][k] table. LCA query: equalize depths, then jump both up until they meet.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import math
from collections import deque


def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """Return the LCA for each query [u, v] using binary lifting."""
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
        edges.append([u, v])
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        queries.append([u, v])
    result = solve(n, edges, queries)
    print(" ".join(map(str, result)))
