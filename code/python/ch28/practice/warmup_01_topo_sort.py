"""
Warmup 1: Topological Sort (Kahn's)
===================================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return a valid topological ordering, or [] if cycle exists.

EXAMPLES
--------
  solve(3, [[0, 1], [1, 2]]) -> [0, 1, 2]
  solve(1, []) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Kahn's Algorithm: BFS with in-degree tracking. Process zero-indegree nodes, decrement neighbors' in-degrees.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque, defaultdict


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """Return a valid topological ordering, or [] if cycle exists."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
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
