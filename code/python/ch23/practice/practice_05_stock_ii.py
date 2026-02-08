"""
Practice 5: Best Time to Buy and Sell Stock II
===============================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an array of prices where prices[i] is the stock price on day i,
find the maximum profit with unlimited transactions (you can buy and sell
multiple times, but must sell before buying again).

EXAMPLES
--------
  prices=[7,1,5,3,6,4] -> 7  (buy@1 sell@5, buy@3 sell@6)
  prices=[1,2,3,4,5] -> 4  (buy@1 sell@5)
  prices=[7,6,4,3,1] -> 0

CONSTRAINTS
-----------
- 1 <= len(prices) <= 3 * 10^4
- 0 <= prices[i] <= 10^4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(prices: list[int]) -> int:
    """Return max profit with unlimited transactions."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
