"""
Practice 5: Number of Enclaves
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an m x n grid of 0s and 1s, return the number of land cells (1s)
that cannot reach the boundary of the grid by walking through land cells
4-directionally.

EXAMPLES
--------
>>> solve([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
3

CONSTRAINTS
-----------
- 1 <= m, n <= 500
- grid[i][j] is 0 or 1
"""


def solve(grid: list[list[int]]) -> int:
    """Return count of land cells that cannot reach the boundary."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    grid = []
    for _ in range(rows):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
