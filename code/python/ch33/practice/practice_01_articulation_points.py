"""
Practice 1: Articulation Points
===============================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return all articulation points in the graph, sorted.

EXAMPLES
--------
  solve(5, [[0,1],[1,2],[2,0],[1,3],[3,4]]) -> [1, 3]
  solve(4, [[0,1],[1,2],[2,3],[3,0]]) -> []
  solve(5, [[0,1],[0,2],[0,3],[0,4]]) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Tarjan's algorithm variant for articulation points: - Root is AP if it has 2+ DFS children

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """Return all articulation points in the graph, sorted."""
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
    print(" ".join(map(str, result)))
