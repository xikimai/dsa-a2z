"""
Warmup 2: Network Delay Time
============================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return the minimum time for all nodes to receive the signal.

EXAMPLES
--------
  solve([[2,1,1],[2,3,1],[3,4,1]], 4, 2) -> 2
  solve([[1,2,1]], 2, 2) -> -1
  solve([[1,2,1]], 2, 1) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Dijkstra from node k (1-indexed). Answer is max of all distances. If any node is unreachable (dist == INF), return -1.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import heapq


def solve(times: list[list[int]], n: int, k: int) -> int:
    """Return the minimum time for all nodes to receive the signal."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    m = int(data[idx]); idx += 1
    times = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        times.append([u, v, w])
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    print(solve(times, n, k))
