"""
Practice 1: Shortest Path (Unweighted)
========================================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1), a list of undirected edges, and a
source node, return a list of shortest distances from source to every
node. If a node is unreachable, its distance should be -1.

INPUT FORMAT
------------
First line: n (number of nodes), m (number of edges), source.
Next m lines: two integers u, v representing an undirected edge.

OUTPUT FORMAT
-------------
A list of n integers: dist[i] is the shortest distance from source to i.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- 0 <= m <= 10^5
- 0 <= source < n

EXAMPLES
--------
Input:
  5 4 0
  0 1
  0 2
  1 3
  3 4
Output: [0, 1, 1, 2, 3]

Input:
  4 2 0
  0 1
  2 3
Output: [0, 1, -1, -1]

HINT
----
BFS naturally finds shortest paths in unweighted graphs. Initialize
dist array to -1, set dist[source] = 0, then for each neighbor:
dist[neighbor] = dist[node] + 1.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]], source: int) -> list[int]:
    """Return shortest distances from source to all nodes."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, m, source = int(parts[0]), int(parts[1]), int(parts[2])
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges, source))
