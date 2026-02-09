"""
Warmup 2: Redundant Connection
==============================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the redundant edge [u, v] that creates a cycle.

EXAMPLES
--------
  solve([[1, 2], [1, 3], [2, 3]]) -> [2, 3]
  solve([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) -> [1, 4]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Process edges in order. The first edge where both endpoints are already connected (find(u) == find(v)) is the redundant edge.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(edges: list[list[int]]) -> list[int]:
    """Return the redundant edge [u, v] that creates a cycle."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    result = solve(edges)
    print(result[0], result[1])
