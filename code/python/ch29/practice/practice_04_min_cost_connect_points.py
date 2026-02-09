"""
Practice 4: Min Cost to Connect All Points
==========================================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the minimum cost to connect all points (MST of Manhattan distances).

EXAMPLES
--------
  solve([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) -> 20
  solve([[3, 12], [-2, 5], [-4, 1]]) -> 18
  solve([[0, 0]]) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Generate all pairwise edges with Manhattan distance, then run Kruskal's MST.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(points: list[list[int]]) -> int:
    """Return the minimum cost to connect all points (MST of Manhattan distances)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    points = []
    for _ in range(n):
        x = int(tokens[idx]); idx += 1
        y = int(tokens[idx]); idx += 1
        points.append([x, y])
    print(solve(points))
