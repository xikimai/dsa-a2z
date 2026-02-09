"""
Warmup 1: Dijkstra SSSP
=======================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return shortest distances from src to all nodes.

EXAMPLES
--------
  solve(5, edges, 0) -> [0, 3, 1, 8, 9]
  solve(3, [[0,1,1],[1,2,2]], 0) -> [0, 1, 3]
  solve(1, [], 0) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Standard Dijkstra with min-heap. Build adjacency list, relax neighbors.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import heapq


def solve(n: int, edges: list[list[int]], src: int) -> list[int]:
    """Return shortest distances from src to all nodes."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        edges.append([u, v, w])
    src = int(input_data[idx]); idx += 1
    print(solve(n, edges, src))
