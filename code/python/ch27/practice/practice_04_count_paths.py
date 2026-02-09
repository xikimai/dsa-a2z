"""
Practice 4: Number of Ways to Arrive at Destination
===================================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return number of shortest paths from 0 to n-1, mod 10^9+7.

EXAMPLES
--------
  solve(7, roads) -> 4
  solve(2, [[1,0,10]]) -> 1
  solve(1, []) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Dijkstra + counting. Maintain ways[v] alongside dist[v]. When dist improves, reset ways. When dist equals, add ways.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import heapq


def solve(n: int, roads: list[list[int]]) -> int:
    """Return number of shortest paths from 0 to n-1, mod 10^9+7."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    roads = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        roads.append([u, v, w])
    print(solve(n, roads))
