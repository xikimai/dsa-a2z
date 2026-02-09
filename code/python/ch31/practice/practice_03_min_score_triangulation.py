"""
Practice 3: Minimum Score Triangulation of Polygon
==================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return minimum score triangulation of the polygon.

EXAMPLES
--------
  solve([1, 2, 3]) -> 6
  solve([3, 7, 4, 5]) -> 144
  solve([1, 3, 1, 4, 1, 5]) -> 13

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Interval DP. dp[i][j] = min score to triangulate polygon vertices i..j. For each pair (i, j), try every intermediate vertex k as the triangle

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(values: list[int]) -> int:
    """Return minimum score triangulation of the polygon."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    values = [int(x) for x in tokens]
    print(solve(values))
