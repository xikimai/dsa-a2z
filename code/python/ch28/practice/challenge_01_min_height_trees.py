"""
Challenge 1: Minimum Height Trees
=================================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return list of root nodes that minimize tree height.

EXAMPLES
--------
  solve(1, []) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Iterative leaf removal (like Kahn's on undirected tree). Remove all leaves (degree 1) simultaneously. Repeat until

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """Return list of root nodes that minimize tree height."""
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
