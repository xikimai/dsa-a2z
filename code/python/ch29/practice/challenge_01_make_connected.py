"""
Challenge 1: Operations to Make Network Connected
=================================================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return min cables to move to connect all computers, or -1 if impossible.

EXAMPLES
--------
  solve(4, [[0, 1], [0, 2], [1, 2]]) -> 1
  solve(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) -> 2
  solve(4, [[0, 1], [0, 2]]) -> -1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Count connected components and redundant edges (edges within same component). Need (components - 1) cables to connect all. If redundant >= components - 1,

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, connections: list[list[int]]) -> int:
    """Return min cables to move to connect all computers, or -1 if impossible."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    connections = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        connections.append([u, v])
    print(solve(n, connections))
