"""
Warmup 4: Detect Cycle in Directed Graph
========================================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return True if graph is a DAG (no cycle), False if cycle exists.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Three-color DFS. WHITE=0, GRAY=1, BLACK=2. If we visit a GRAY node, cycle exists. Return False.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]]) -> bool:
    """Return True if graph is a DAG (no cycle), False if cycle exists."""
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
