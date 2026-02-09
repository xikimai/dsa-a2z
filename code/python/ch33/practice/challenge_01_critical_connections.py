"""
Challenge 1: Critical Connections in a Network
==============================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return all critical connections (bridges), sorted.

EXAMPLES
--------
  solve(4, [[0,1],[1,2],[2,0],[1,3]]) -> [[1,3]]
  solve(5, [[0,1],[1,2],[2,3],[3,0],[2,4]]) -> [[2,4]]
  solve(3, [[0,1],[1,2],[2,0]]) -> []

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Same as Tarjan's bridge-finding: disc/low arrays, bridge if low[v] > disc[u].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, connections: list[list[int]]) -> list[list[int]]:
    """Return all critical connections (bridges), sorted."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    connections = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        connections.append([u, v])
    result = solve(n, connections)
    for bridge in result:
        print(bridge[0], bridge[1])
