"""
Warmup 2: Number of Islands
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n grid of 0s (water) and 1s (land), count the number of
islands. An island is a group of 1s connected 4-directionally.

EXAMPLES
--------
>>> solve([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]])
3

CONSTRAINTS
-----------
- 1 <= m, n <= 300
- grid[i][j] is 0 or 1
"""


def solve(grid: list[list[int]]) -> int:
    """Return the number of islands in the grid."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
