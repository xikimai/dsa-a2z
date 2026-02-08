"""
Warmup 4: Count Connected Components
======================================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1) and a list of undirected edges,
return the number of connected components in the graph.

INPUT FORMAT
------------
First line: n (number of nodes) and m (number of edges).
Next m lines: two integers u, v representing an undirected edge.

OUTPUT FORMAT
-------------
A single integer: the number of connected components.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- 0 <= m <= 10^5

EXAMPLES
--------
Input:
  5 3
  0 1
  1 2
  3 4
Output: 2

Input:
  3 0
Output: 3

HINT
----
Loop through all nodes. For each unvisited node, run BFS/DFS to mark
all reachable nodes as visited. Count how many times you launch BFS/DFS.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of connected components."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges))
