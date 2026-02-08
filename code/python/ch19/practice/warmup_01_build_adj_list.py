"""
Warmup 1: Build Adjacency List
================================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1) and a list of undirected edges,
build and return an adjacency list representation. Each node's
neighbor list should be sorted in ascending order.

INPUT FORMAT
------------
First line: n (number of nodes) and m (number of edges).
Next m lines: two integers u, v representing an undirected edge.

OUTPUT FORMAT
-------------
A list of n lists, where list[i] contains the sorted neighbors of node i.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- 0 <= m <= 10^5
- 0 <= u, v < n

EXAMPLES
--------
Input:
  4 3
  0 1
  0 2
  1 3
Output: [[1, 2], [0, 3], [0], [1]]

HINT
----
Create n empty lists. For each edge (u, v), add v to adj[u] and u to adj[v].
Don't forget to sort each list at the end.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return adjacency list as list of lists (sorted neighbors)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    adj = solve(n, edges)
    for i in range(n):
        print(f"{i}: {adj[i]}")
