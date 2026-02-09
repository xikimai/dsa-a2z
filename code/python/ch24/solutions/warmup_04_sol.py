"""
Solution for Warmup 4: Triangle Minimum Total
===============================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Bottom-up DP. Start from the last row, work upward.
dp[j] = triangle[i][j] + min(dp[j], dp[j+1]).
After processing all rows, dp[0] is the answer.

TIME COMPLEXITY:  O(n^2) where n = number of rows
SPACE COMPLEXITY: O(n) — one row of the triangle
"""

from typing import List


def solve(triangle: List[List[int]]) -> int:
    """Return the minimum path sum from top to bottom of the triangle."""
    dp = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    triangle = json.loads(sys.stdin.readline())
    print(solve(triangle))
