"""
Warmup 3: Bellman-Ford SSSP
===========================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return shortest distances from src to all nodes (Bellman-Ford).

EXAMPLES
--------
  solve(5, edges, 0) -> [0, -1, 2, -2, 1]
  solve(3, edges, 0) -> [0, 3, 1]
  solve(1, [], 0) -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Standard Bellman-Ford: relax all edges n-1 times.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int, edges: list[list[int]], src: int) -> list[int]:
    """Return shortest distances from src to all nodes (Bellman-Ford)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        edges.append([u, v, w])
    src = int(data[idx]); idx += 1
    print(solve(n, edges, src))
