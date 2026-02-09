"""
Warmup 2: Euler Tour of Tree
============================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the Euler tour order (DFS entry order) of the tree.

EXAMPLES
--------
  solve(5, [[0,1],[0,2],[1,3],[1,4]]) -> [0, 1, 3, 4, 2]
  solve(3, [[0,1],[0,2]]) -> [0, 1, 2]
  solve(1, []) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
DFS from root (node 0). Record each node when first entered. Use iterative DFS to avoid recursion limit issues.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """Return the Euler tour order (DFS entry order) of the tree."""
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
