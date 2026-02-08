"""
Warmup 5: Is Path Exists
==========================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given n nodes (labeled 0 to n-1), a list of undirected edges, a source
node, and a destination node, return True if a path exists from source
to destination, False otherwise.

INPUT FORMAT
------------
First line: n, m, source, dest.
Next m lines: two integers u, v representing an undirected edge.

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- 0 <= m <= 10^5
- 0 <= source, dest < n

EXAMPLES
--------
Input:
  4 3 0 3
  0 1
  1 2
  2 3
Output: True

Input:
  4 2 0 3
  0 1
  2 3
Output: False

HINT
----
BFS from source. If you visit dest during the traversal, return True.
If the BFS finishes without reaching dest, return False.
Don't forget the edge case: source == dest.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, edges: list[list[int]], source: int, dest: int) -> bool:
    """Return True if a path exists from source to dest."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, m, source, dest = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges, source, dest))
