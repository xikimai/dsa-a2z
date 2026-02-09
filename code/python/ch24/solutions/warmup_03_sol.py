"""
Solution for Warmup 3: Minimum Path Sum
=========================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Space-optimized 1D DP. dp[j] = min(dp[j], dp[j-1]) + grid[i][j].
First row: accumulate. Then row by row.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the minimum path sum from top-left to bottom-right."""
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]
    for j in range(1, n):
        dp[j] = dp[j - 1] + grid[0][j]
    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[n - 1]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
