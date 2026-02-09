"""
Challenge 2: Rod Cutting
========================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the maximum revenue from cutting the rod.

EXAMPLES
--------
  solve([1, 5, 8, 9, 10, 17, 17, 20]) -> 22
  solve([3, 5, 8, 9, 10, 17, 17, 20]) -> 24
  solve([1]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Unbounded knapsack. dp[l] = max revenue for rod of length l. For each piece length k (1..n), dp[l] = max(dp[l], dp[l-k] + prices[k-1]).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(prices: list[int]) -> int:
    """Return the maximum revenue from cutting the rod."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().strip().split()))
    print(solve(prices))
