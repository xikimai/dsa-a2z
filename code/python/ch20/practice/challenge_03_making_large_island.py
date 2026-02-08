"""
Challenge 3: Making a Large Island
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an n x n binary grid, you may change at most one 0 to 1. Return
the size of the largest island after this operation. An island is a
4-directionally connected group of 1s.

EXAMPLES
--------
>>> solve([[1,0],[0,1]])
3

CONSTRAINTS
-----------
- 1 <= n <= 500
- grid[i][j] is 0 or 1
"""


def solve(grid: list[list[int]]) -> int:
    """Return largest island size after flipping at most one 0."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
