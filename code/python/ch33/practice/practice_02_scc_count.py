"""
Practice 2: Strongly Connected Components (Kosaraju's)
======================================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the number of SCCs in the directed graph.

EXAMPLES
--------
  solve(5, [[0,1],[1,2],[2,0],[1,3],[3,4]]) -> 3
  solve(4, [[0,1],[1,2],[2,3],[3,0]]) -> 1
  solve(3, [[0,1],[1,2]]) -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Kosaraju's two-pass algorithm: 1. DFS on original graph to get finish order

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of SCCs in the directed graph."""
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
    print(solve(n, edges))
