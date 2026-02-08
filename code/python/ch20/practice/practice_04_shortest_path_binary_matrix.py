"""
Practice 4: Shortest Path in Binary Matrix
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an n x n binary grid, find the shortest path from (0,0) to
(n-1,n-1) using 8-directional movement. You can only walk through
cells with value 0. Return the path length (number of cells), or -1
if no path exists.

EXAMPLES
--------
>>> solve([[0,0,0],[1,1,0],[1,1,0]])
4

CONSTRAINTS
-----------
- 1 <= n <= 100
- grid[i][j] is 0 or 1
"""


def solve(grid: list[list[int]]) -> int:
    """Return length of shortest path, or -1 if impossible."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
