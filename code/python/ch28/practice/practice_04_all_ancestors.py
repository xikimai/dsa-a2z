"""
Practice 4: All Ancestors of a Node
===================================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return sorted ancestors for each node.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
For each node, run DFS/BFS in the original graph and mark all reachable nodes as descendants. Equivalently, iterate over each

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return sorted ancestors for each node."""
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
    result = solve(n, edges)
    for row in result:
        print(row)
