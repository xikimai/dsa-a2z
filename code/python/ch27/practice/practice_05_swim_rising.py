"""
Practice 5: Swim in Rising Water
================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return minimum time to swim from (0,0) to (n-1,n-1).

EXAMPLES
--------
  solve([[0,2],[1,3]]) -> 3
  solve(grid) -> 16
  solve([[0]]) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Dijkstra where "distance" = max elevation on the path so far. Relax: new_dist = max(dist[r][c], grid[nr][nc]).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

import heapq


def solve(grid: list[list[int]]) -> int:
    """Return minimum time to swim from (0,0) to (n-1,n-1)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
