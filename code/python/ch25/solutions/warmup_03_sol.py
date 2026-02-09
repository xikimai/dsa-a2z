"""
Solution for Warmup 3: Coin Change (Minimum Coins)
=====================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Bottom-up DP. dp[a] = min coins to make amount a.
For each amount, try each coin and take the minimum.

TIME COMPLEXITY:  O(amount * len(coins))
SPACE COMPLEXITY: O(amount)
"""


def solve(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins to make amount, or -1 if impossible."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
    return dp[amount] if dp[amount] != float("inf") else -1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    coins = list(map(int, input().strip().split()))
    amount = int(input().strip())
    print(solve(coins, amount))
