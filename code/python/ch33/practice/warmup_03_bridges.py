"""
Warmup 3: Find Bridges in Graph
===============================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return all bridges in the graph, sorted.

EXAMPLES
--------
  solve(5, [[0,1],[1,2],[2,0],[1,3],[3,4]]) -> [[1,3],[3,4]]
  solve(4, [[0,1],[1,2],[2,3],[3,0]]) -> []
  solve(2, [[0,1]]) -> [[0,1]]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Tarjan's bridge-finding algorithm: DFS with disc[] and low[] arrays. Edge (u,v) is a bridge if low[v] > disc[u] (v's subtree has no back edge

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return all bridges in the graph, sorted."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    result = solve(n, edges)
    for bridge in result:
        print(bridge[0], bridge[1])
