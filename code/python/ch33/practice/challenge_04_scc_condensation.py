"""
Challenge 4: SCC Condensation (DAG of SCCs)
===========================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the number of edges in the condensed DAG of SCCs.

EXAMPLES
--------
  solve(6, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[2,3]]) -> 1
  solve(4, [[0,1],[1,0],[2,3],[3,2],[1,2]]) -> 1
  solve(3, [[0,1],[1,2]]) -> 2

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Kosaraju's to find SCC labels for each node. 2. For each original edge (u,v), if comp[u] != comp[v], add edge to condensed DAG.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of edges in the condensed DAG of SCCs."""
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
