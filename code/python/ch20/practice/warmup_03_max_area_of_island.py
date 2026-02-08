"""
Warmup 3: Max Area of Island
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n grid of 0s and 1s, return the maximum area of an island.
An island's area is the number of 1s in a 4-directionally connected group.

EXAMPLES
--------
>>> solve([[0,0,1,0,0],[0,0,1,0,0],[0,1,1,0,1],[0,0,1,0,0]])
5

CONSTRAINTS
-----------
- 1 <= m, n <= 50
- grid[i][j] is 0 or 1
"""


def solve(grid: list[list[int]]) -> int:
    """Return the maximum area of an island."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
