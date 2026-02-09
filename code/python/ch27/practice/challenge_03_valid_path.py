"""
Challenge 3: Minimum Cost to Make Valid Path
============================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return minimum cost to create a valid path from (0,0) to (m-1,n-1).

EXAMPLES
--------
  solve([[1,1,2],[1,1,2],[1,1,1]]) -> 2
  solve([[1,1,3],[3,2,2],[1,1,4]]) -> 0
  solve([[2,2,2],[2,2,2]]) -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
0-1 BFS. From each cell, try all 4 directions. If direction matches the arrow, cost = 0. Otherwise, cost = 1.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return minimum cost to create a valid path from (0,0) to (m-1,n-1)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
