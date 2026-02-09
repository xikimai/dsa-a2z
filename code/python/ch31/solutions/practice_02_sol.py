"""
Solution for Practice 2: Burst Balloons
========================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Interval DP. Add boundary 1s. dp[i][j] = max coins from bursting
balloons in [i..j]. Think about which balloon is burst LAST.

TIME COMPLEXITY:  O(n^3)
SPACE COMPLEXITY: O(n^2)
"""


def solve(nums: list[int]) -> int:
    """Return maximum coins from bursting all balloons."""
    vals = [1] + nums + [1]
    n = len(vals)
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n - 1):
        for left in range(1, n - length):
            right = left + length - 1
            for k in range(left, right + 1):
                coins = vals[left - 1] * vals[k] * vals[right + 1]
                coins += dp[left][k - 1] + dp[k + 1][right]
                dp[left][right] = max(dp[left][right], coins)

    return dp[1][n - 2]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    nums = [int(x) for x in tokens]
    print(solve(nums))
