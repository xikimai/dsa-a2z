"""
Practice 2: Detect Cycle in Undirected Graph
=============================================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1) and a list of undirected edges,
determine whether the graph contains a cycle. The graph may be
disconnected.

INPUT FORMAT
------------
First line: n (number of nodes) and m (number of edges).
Next m lines: two integers u, v representing an undirected edge.

OUTPUT FORMAT
-------------
True if a cycle exists, False otherwise.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- 0 <= m <= 10^5
- No self-loops or duplicate edges

EXAMPLES
--------
Input:
  4 4
  0 1
  1 2
  2 3
  3 0
Output: True

Input:
  4 3
  0 1
  1 2
  2 3
Output: False

HINT
----
Use DFS with parent tracking. If you visit a neighbor that is already
visited AND it's not the parent of the current node, you've found a cycle.
Remember to check all components (the graph may be disconnected).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]]) -> bool:
    """Return True if the undirected graph contains a cycle."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges))
