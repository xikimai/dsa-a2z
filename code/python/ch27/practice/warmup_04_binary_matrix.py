"""
Warmup 4: Shortest Path in Binary Matrix
========================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return shortest path length in binary matrix, or -1.

EXAMPLES
--------
  solve([[0,1],[1,0]]) -> 2
  solve([[0,0,0],[1,1,0],[1,1,0]]) -> 4
  solve([[1,0,0],[0,0,0],[0,0,0]]) -> -1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
BFS from (0,0) to (n-1,n-1) with 8-directional moves. Each step costs 1.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    """Return shortest path length in binary matrix, or -1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    grid = json.loads(sys.stdin.read().strip())
    print(solve(grid))
