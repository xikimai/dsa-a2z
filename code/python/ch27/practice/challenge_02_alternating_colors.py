"""
Challenge 2: Shortest Path with Alternating Colors
==================================================
Chapter 27: Shortest Paths — Finding the Best Route

PROBLEM
-------
Return shortest alternating-color path distances from node 0.

EXAMPLES
--------
  solve(3, [[0,1],[1,2]], []) -> [0, 1, -1]
  solve(3, [[0,1]], [[2,1]]) -> [0, 1, -1]
  solve(3, [[0,1],[0,2]], [[1,0]]) -> [0, 1, 1]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
BFS with state = (node, last_color). 0 = red, 1 = blue. Start BFS from (0, -1) to allow first edge to be either color.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque


def solve(n: int, red_edges: list[list[int]], blue_edges: list[list[int]]) -> list[int]:
    """Return shortest alternating-color path distances from node 0."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    data = sys.stdin.read().strip().split('\n')
    n = int(data[0])
    red_edges = json.loads(data[1])
    blue_edges = json.loads(data[2])
    print(solve(n, red_edges, blue_edges))
