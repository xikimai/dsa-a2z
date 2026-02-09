"""
Practice 3: Subtree Sum (Euler Tour + Array)
============================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the subtree sum for each query node.

EXAMPLES
--------
  solve(5, [1,2,3,4,5], [[0,1],[0,2],[1,3],[1,4]], [0,1,2]) -> [15, 11, 3]
  solve(3, [10,20,30], [[0,1],[0,2]], [0,1]) -> [60, 20]
  solve(1, [42], [], [0]) -> [42]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Euler Tour to get tin/tout for each node. 2. Build flat array in Euler tour order with node values.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, values: list[int], edges: list[list[int]], queries: list[int]) -> list[int]:
    """Return the subtree sum for each query node."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    vals = []
    for _ in range(n):
        vals.append(int(tokens[idx])); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        queries.append(int(tokens[idx])); idx += 1
    result = solve(n, vals, edges, queries)
    print(" ".join(map(str, result)))
