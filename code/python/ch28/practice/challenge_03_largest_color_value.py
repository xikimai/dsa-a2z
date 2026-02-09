"""
Challenge 3: Largest Color Value in Directed Graph
==================================================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return max color frequency on any path, or -1 if cycle.

EXAMPLES
--------
  solve("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) -> 3
  solve("a", [[0, 0]]) -> -1
  solve("a", []) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Kahn's BFS + DP. For each node, maintain dp[node][c] = max count of color c on any path ending at node. Process in topological order,

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque, defaultdict


def solve(colors: str, edges: list[list[int]]) -> int:
    """Return max color frequency on any path, or -1 if cycle."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    colors = tokens[0]
    m = int(tokens[1])
    idx = 2
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    print(solve(colors, edges))
