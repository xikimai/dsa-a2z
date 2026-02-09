"""
Challenge 2: Making a Large Island
==================================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the largest island size after flipping at most one 0 to 1.

EXAMPLES
--------
  solve([[1, 0], [0, 1]]) -> 3
  solve([[1, 1], [1, 0]]) -> 4
  solve([[1, 1], [1, 1]]) -> 4

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Label each connected component of 1s with Union-Find, track component sizes. 2. For each 0 cell, check the 4 adjacent cells and sum up the sizes of

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(grid: list[list[int]]) -> int:
    """Return the largest island size after flipping at most one 0 to 1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(tokens[idx])); idx += 1
        grid.append(row)
    print(solve(grid))
