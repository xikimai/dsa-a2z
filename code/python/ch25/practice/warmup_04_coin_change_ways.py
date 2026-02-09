"""
Warmup 4: Coin Change II (Count Ways)
=====================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the number of combinations that sum to amount.

EXAMPLES
--------
  solve([1, 2, 5], 5) -> 4
  solve([2], 3) -> 0
  solve([10], 10) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1D DP. dp[a] = number of combinations summing to a. Outer loop over coins (to count combinations, not permutations).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(coins: list[int], amount: int) -> int:
    """Return the number of combinations that sum to amount."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    coins = list(map(int, input().strip().split()))
    amount = int(input().strip())
    print(solve(coins, amount))
