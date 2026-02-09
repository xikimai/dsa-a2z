"""
Challenge 1: Minimum Obstacle Removal to Reach Corner
=====================================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return minimum obstacles to remove.

EXAMPLES
--------
  solve([[0,1,1],[1,1,0],[1,1,0]]) -> 2
  solve([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]) -> 0
  solve([[0]]) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
0-1 BFS. Empty cell (0) costs 0, obstacle (1) costs 1 to remove. Push 0-cost moves to front of deque, 1-cost to back.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return minimum obstacles to remove."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
