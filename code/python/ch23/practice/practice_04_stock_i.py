"""
Practice 4: Best Time to Buy and Sell Stock I
==============================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an array of prices where prices[i] is the stock price on day i,
find the maximum profit from one buy-sell transaction (buy before sell).
If no profit is possible, return 0.

EXAMPLES
--------
  prices=[7,1,5,3,6,4] -> 5  (buy day 1 at 1, sell day 4 at 6)
  prices=[7,6,4,3,1] -> 0  (no profitable transaction)

CONSTRAINTS
-----------
- 1 <= len(prices) <= 10^5
- 0 <= prices[i] <= 10^4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(prices: list[int]) -> int:
    """Return max profit from one buy-sell transaction."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
