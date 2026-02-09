"""
Warmup 3: Coin Change (Minimum Coins)
=====================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the minimum number of coins to make amount, or -1 if impossible.

EXAMPLES
--------
  solve([1, 5, 11], 15) -> 3
  solve([2], 3) -> -1
  solve([1], 0) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Bottom-up DP. dp[a] = min coins to make amount a. For each amount, try each coin and take the minimum.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins to make amount, or -1 if impossible."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    coins = list(map(int, input().strip().split()))
    amount = int(input().strip())
    print(solve(coins, amount))
