"""
Practice 5: Count SCCs of Size > 1
==================================
Chapter 33: Advanced Trees & Graph Algorithms

PROBLEM
-------
Return the count of SCCs with more than 1 node.

EXAMPLES
--------
  solve(7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[6,0]]) -> 2
  solve(4, [[0,1],[1,2],[2,3]]) -> 0
  solve(3, [[0,1],[1,0],[2,0]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Kosaraju's to find all SCCs, then count those with size > 1.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import sys
sys.setrecursionlimit(200000)
from collections import Counter


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the count of SCCs with more than 1 node."""
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
