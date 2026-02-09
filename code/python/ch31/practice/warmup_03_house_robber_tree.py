"""
Warmup 3: House Robber on Tree
==============================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return max sum of non-adjacent nodes in the tree.

EXAMPLES
--------
  solve(4, [1, 2, 3, 4], [[0, 1], [0, 2], [1, 3]]) -> 7
  solve(3, [1, 3, 5], [[0, 1], [0, 2]]) -> 8
  solve(1, [10], []) -> 10

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Tree DP. For each node: dp[u][0] = max if u NOT robbed, dp[u][1] = max if u IS robbed. Process leaves to root.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, values: list[int], edges: list[list[int]]) -> int:
    """Return max sum of non-adjacent nodes in the tree."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    values = []
    for _ in range(n):
        values.append(int(tokens[idx])); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    print(solve(n, values, edges))
