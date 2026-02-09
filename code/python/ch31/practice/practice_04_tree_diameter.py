"""
Practice 4: Tree Diameter via DP
================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return the diameter of the tree.

EXAMPLES
--------
  solve(5, [[0, 1], [1, 2], [1, 3], [3, 4]]) -> 3
  solve(2, [[0, 1]]) -> 1
  solve(1, []) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Tree DP. For each node, compute the longest downward path. The diameter through a node is the sum of the two longest downward paths from it.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the diameter of the tree."""
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
