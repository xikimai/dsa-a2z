"""
Practice 4: Clone Graph
=========================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given an adjacency list (list of lists), return a deep clone. The clone
must be a completely independent copy — modifying the clone should not
affect the original.

INPUT FORMAT
------------
First line: n (number of nodes).
Next n lines: space-separated neighbor indices for each node (or empty).

OUTPUT FORMAT
-------------
The cloned adjacency list (same format as input).

CONSTRAINTS
-----------
- 0 <= n <= 10^4
- 0 <= adj[i][j] < n

EXAMPLES
--------
Input:
  4
  1 2
  0 3
  0 3
  1 2
Output: [[1, 2], [0, 3], [0, 3], [1, 2]]

HINT
----
Create a new list of n empty lists. Copy each node's neighbor list
using list() or slicing to ensure independent copies.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(adj: list[list[int]]) -> list[list[int]]:
    """Return a deep clone of the adjacency list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    adj = []
    for _ in range(n):
        line = input().strip()
        if line:
            adj.append(list(map(int, line.split())))
        else:
            adj.append([])
    clone = solve(adj)
    for i in range(len(clone)):
        print(f"{i}: {clone[i]}")
