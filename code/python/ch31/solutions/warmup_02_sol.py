"""
Solution for Warmup 2: Matrix Chain Multiplication
===================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Interval DP. dp[i][j] = min cost to multiply matrices i..j.
Iterate by interval length, try all split points k.

TIME COMPLEXITY:  O(n^3)
SPACE COMPLEXITY: O(n^2)
"""


def solve(dims: list[int]) -> int:
    """Return minimum scalar multiplications for the matrix chain."""
    n = len(dims) - 1  # number of matrices
    if n <= 1:
        return 0

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    dims = [int(x) for x in tokens]
    print(solve(dims))
