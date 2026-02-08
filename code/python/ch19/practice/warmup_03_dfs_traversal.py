"""
Warmup 3: DFS Traversal
=========================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1), a list of undirected edges, and a
source node, return the DFS traversal order starting from the source.
When multiple neighbors are available, visit the smallest-numbered first.

INPUT FORMAT
------------
First line: n (number of nodes), m (number of edges), source.
Next m lines: two integers u, v representing an undirected edge.

OUTPUT FORMAT
-------------
A list of node labels in DFS visit order.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- 0 <= m <= 10^5
- 0 <= source < n

EXAMPLES
--------
Input:
  4 3 0
  0 1
  0 2
  1 3
Output: [0, 1, 3, 2]

HINT
----
Use recursion. Mark a node as visited, add it to the result, then
recurse on each unvisited neighbor (in sorted order).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]], source: int) -> list[int]:
    """Return DFS traversal order from source."""
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
