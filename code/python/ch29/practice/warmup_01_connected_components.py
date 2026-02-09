"""
Warmup 1: Connected Components (Union-Find)
===========================================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the number of connected components in an undirected graph.

EXAMPLES
--------
  solve(5, [[0, 1], [1, 2], [3, 4]]) -> 2
  solve(5, []) -> 5
  solve(4, [[0, 1], [1, 2], [2, 3]]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Union-Find: start with n components, merge for each edge, count remaining.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of connected components in an undirected graph."""
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
