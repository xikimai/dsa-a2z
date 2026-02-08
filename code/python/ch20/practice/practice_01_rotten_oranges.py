"""
Practice 1: Rotten Oranges
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n grid where 0 = empty, 1 = fresh orange, 2 = rotten orange,
every minute each rotten orange rots all 4-directionally adjacent fresh
oranges. Return the minimum minutes until no fresh orange remains, or -1
if impossible.

EXAMPLES
--------
>>> solve([[2,1,1],[1,1,0],[0,1,1]])
4

CONSTRAINTS
-----------
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2
"""


def solve(grid: list[list[int]]) -> int:
    """Return minutes until all oranges are rotten, or -1 if impossible."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
