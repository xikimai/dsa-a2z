"""
Practice 2: Path with Minimum Effort
====================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return the minimum effort path value.

EXAMPLES
--------
  solve([[1,2,2],[3,8,2],[5,3,5]]) -> 2
  solve([[1,2,3],[3,8,4],[5,3,5]]) -> 1
  solve(grid) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Dijkstra on grid. dist[r][c] = minimum effort to reach (r,c). Edge weight = abs(heights[r][c] - heights[nr][nc]).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import heapq


def solve(heights: list[list[int]]) -> int:
    """Return the minimum effort path value."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    heights = json.loads(sys.stdin.read().strip())
    print(solve(heights))
