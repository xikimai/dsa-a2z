"""
Challenge 2: Shortest Bridge
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an n x n binary grid with exactly two islands, return the minimum
number of 0s you must flip to connect the two islands.

EXAMPLES
--------
>>> solve([[0,1,0],[0,0,0],[0,0,1]])
2

CONSTRAINTS
-----------
- 2 <= n <= 100
- grid[i][j] is 0 or 1
- There are exactly two islands
"""


def solve(grid: list[list[int]]) -> int:
    """Return minimum flips to connect two islands."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
