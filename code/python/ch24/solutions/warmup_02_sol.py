"""
Solution for Warmup 2: Unique Paths with Obstacles
====================================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Space-optimized 1D DP. Set dp[j] = 0 for obstacles.
For first row, propagate left; then row by row, dp[j] += dp[j-1]
if the cell is not blocked.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return number of unique paths avoiding obstacles."""
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1:
        return 0
    dp = [0] * n
    dp[0] = 1
    for j in range(1, n):
        dp[j] = dp[j - 1] if grid[0][j] == 0 else 0
    for i in range(1, m):
        dp[0] = dp[0] if grid[i][0] == 0 else 0
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[j] = 0
            else:
                dp[j] += dp[j - 1]
    return dp[n - 1]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
