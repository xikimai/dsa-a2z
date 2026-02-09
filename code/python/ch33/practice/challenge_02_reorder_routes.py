"""
Challenge 2: Reorder Routes to City Zero
========================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the number of roads to reverse so all cities can reach city 0.

EXAMPLES
--------
  solve(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) -> 3
  solve(3, [[1,0],[2,0]]) -> 0
  solve(3, [[0,1],[0,2]]) -> 2

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build undirected adjacency list but track which edges are original (away from 0) vs reversed (toward 0). BFS/DFS from node 0. For each edge traversed from 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque


def solve(n: int, connections: list[list[int]]) -> int:
    """Return the number of roads to reverse so all cities can reach city 0."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    connections = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        connections.append([u, v])
    print(solve(n, connections))
