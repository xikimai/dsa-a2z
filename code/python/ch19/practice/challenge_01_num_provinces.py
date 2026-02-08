"""
Challenge 1: Number of Provinces
==================================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given an n x n adjacency matrix `isConnected` where isConnected[i][j] = 1
means cities i and j are directly connected, return the number of provinces.
A province is a group of directly or indirectly connected cities.

INPUT FORMAT
------------
First line: n (number of cities).
Next n lines: n integers (0 or 1) representing the adjacency matrix.

OUTPUT FORMAT
-------------
A single integer: the number of provinces.

CONSTRAINTS
-----------
- 1 <= n <= 200
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]

EXAMPLES
--------
Input:
  3
  1 1 0
  1 1 0
  0 0 1
Output: 2

Input:
  3
  1 0 0
  0 1 0
  0 0 1
Output: 3

HINT
----
This is "count connected components" but on an adjacency matrix instead
of an edge list. For each unvisited city, BFS/DFS to mark all connected
cities as visited.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(isConnected: list[list[int]]) -> int:
    """Return the number of provinces."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    isConnected = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        isConnected.append(row)
    print(solve(isConnected))
