"""
Challenge 4: Path with Maximum Minimum Value
============================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return the maximum minimum value on any path from (0,0) to (m-1,n-1).

EXAMPLES
--------
  solve([[5,4,5],[1,2,6],[7,4,6]]) -> 4
  solve([[2,2,1,2,2,2],[1,2,2,2,1,2]]) -> 2
  solve(grid) -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Modified Dijkstra using a MAX-heap. We want to maximize the minimum value on the path. dist[r][c] = best (largest) minimum value to reach (r,c).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import heapq


def solve(grid: list[list[int]]) -> int:
    """Return the maximum minimum value on any path from (0,0) to (m-1,n-1)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
