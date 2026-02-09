"""
Solution for Practice 2: Minimum Falling Path Sum
===================================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Space-optimized bottom-up DP. For each row, compute new dp values
using the previous row. dp[j] = matrix[i][j] + min of up to 3
values from the previous row (j-1, j, j+1).

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n)
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the minimum falling path sum."""
    n = len(matrix)
    dp = matrix[0][:]
    for i in range(1, n):
        new_dp = [0] * n
        for j in range(n):
            best = dp[j]
            if j > 0:
                best = min(best, dp[j - 1])
            if j < n - 1:
                best = min(best, dp[j + 1])
            new_dp[j] = matrix[i][j] + best
        dp = new_dp
    return min(dp)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
