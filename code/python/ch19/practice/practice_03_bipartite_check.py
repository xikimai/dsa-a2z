"""
Practice 3: Bipartite Check
=============================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1) and a list of undirected edges,
determine whether the graph is bipartite. A graph is bipartite if
its nodes can be colored with two colors such that no two adjacent
nodes share the same color. The graph may be disconnected.

INPUT FORMAT
------------
First line: n (number of nodes) and m (number of edges).
Next m lines: two integers u, v representing an undirected edge.

OUTPUT FORMAT
-------------
True if the graph is bipartite, False otherwise.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- 0 <= m <= 10^5

EXAMPLES
--------
Input:
  4 4
  0 1
  1 2
  2 3
  3 0
Output: True  (even cycle — bipartite)

Input:
  3 3
  0 1
  1 2
  2 0
Output: False  (odd cycle — not bipartite)

HINT
----
Use BFS 2-coloring. Start with color 0 for an uncolored node, then
color its neighbors with color 1. If a neighbor already has the SAME
color as the current node, return False. Check all components.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]]) -> bool:
    """Return True if the graph is bipartite."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges))
