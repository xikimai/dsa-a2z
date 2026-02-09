"""
Warmup 3: Kruskal's MST
=======================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the total MST weight using Kruskal's algorithm.

EXAMPLES
--------
  solve(4, [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]) -> 19
  solve(3, [[0, 1, 1], [1, 2, 2], [0, 2, 3]]) -> 3
  solve(1, []) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Sort edges by weight, greedily add edges that connect different components.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the total MST weight using Kruskal's algorithm."""
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
        w = int(tokens[idx]); idx += 1
        edges.append([u, v, w])
    print(solve(n, edges))
