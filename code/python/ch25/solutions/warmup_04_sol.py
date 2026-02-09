"""
Solution for Warmup 4: Coin Change II (Count Ways)
=====================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
1D DP. dp[a] = number of combinations summing to a.
Outer loop over coins (to count combinations, not permutations).
Inner loop forward (unbounded — coins can be reused).

TIME COMPLEXITY:  O(amount * len(coins))
SPACE COMPLEXITY: O(amount)
"""


def solve(coins: list[int], amount: int) -> int:
    """Return the number of combinations that sum to amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]
    return dp[amount]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    coins = list(map(int, input().strip().split()))
    amount = int(input().strip())
    print(solve(coins, amount))
