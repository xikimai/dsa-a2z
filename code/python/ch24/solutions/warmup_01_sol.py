"""
Solution for Warmup 1: Unique Paths
=====================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Space-optimized bottom-up DP. Use 1D array of size n, fill left to right.
dp[j] += dp[j-1] for each row. Initially all 1s.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""


def solve(m: int, n: int) -> int:
    """Return the number of unique paths from top-left to bottom-right."""
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    m, n = map(int, input().strip().split())
    print(solve(m, n))
