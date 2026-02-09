"""
Challenge 3: Binary Tree Cameras
================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return minimum cameras to monitor all nodes.

EXAMPLES
--------
  solve(5, [[0, 1], [0, 2], [1, 3], [1, 4]]) -> 2
  solve(3, [[0, 1], [1, 2]]) -> 1
  solve(1, []) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Tree DP with 3 states per node: - state 0: node is NOT monitored (needs parent to place camera or be covered)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return minimum cameras to monitor all nodes."""
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
