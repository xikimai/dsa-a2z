"""
Practice 5: All Paths from Source to Target
=============================================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1) and a list of DIRECTED edges
(forming a DAG), find all paths from node 0 to node n-1.
Return the paths sorted lexicographically.

INPUT FORMAT
------------
First line: n (number of nodes) and m (number of edges).
Next m lines: two integers u, v representing a directed edge u -> v.

OUTPUT FORMAT
-------------
A list of paths (each path is a list of node labels), sorted.

CONSTRAINTS
-----------
- 2 <= n <= 15
- 0 <= m <= n*(n-1)/2
- The graph is a DAG (no cycles)

EXAMPLES
--------
Input:
  4 4
  0 1
  0 2
  1 3
  2 3
Output: [[0, 1, 3], [0, 2, 3]]

HINT
----
Use DFS with backtracking from node 0. Maintain a current path list.
When you reach node n-1, save a copy of the path. Since it's a DAG,
you don't need a visited array — but do remember to pop after recursing.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return all paths from node 0 to node n-1, sorted."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    paths = solve(n, edges)
    for path in paths:
        print(" -> ".join(map(str, path)))
