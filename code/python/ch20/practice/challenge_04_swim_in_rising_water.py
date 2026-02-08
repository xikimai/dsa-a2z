"""
Challenge 4: Swim in Rising Water
============================================
Chapter 20: Graphs II -- Real Problems

PROBLEM
-------
Given an n x n grid where grid[i][j] is the elevation, at time t the
water level is t. You can swim from (r,c) to an adjacent cell if both
cells have elevation <= t. Starting at (0,0), return the minimum time
to reach (n-1, n-1).

EXAMPLES
--------
>>> solve([[0,2],[1,3]])
3

CONSTRAINTS
-----------
- 1 <= n <= 50
- 0 <= grid[i][j] < n^2
- Each value in [0, n^2 - 1] appears exactly once
"""


def solve(grid: list[list[int]]) -> int:
    """Return minimum time to swim from (0,0) to (n-1,n-1)."""
    pass


# -- Do not change anything below this line ----------------------------------
if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(grid))
