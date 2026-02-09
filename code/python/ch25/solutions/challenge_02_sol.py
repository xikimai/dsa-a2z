"""
Solution for Challenge 2: Rod Cutting
========================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Unbounded knapsack. dp[l] = max revenue for rod of length l.
For each piece length k (1..n), dp[l] = max(dp[l], dp[l-k] + prices[k-1]).

TIME COMPLEXITY:  O(n^2) where n = rod length
SPACE COMPLEXITY: O(n)
"""


def solve(prices: list[int]) -> int:
    """Return the maximum revenue from cutting the rod."""
    n = len(prices)
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for k in range(1, length + 1):
            dp[length] = max(dp[length], dp[length - k] + prices[k - 1])
    return dp[n]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().strip().split()))
    print(solve(prices))
