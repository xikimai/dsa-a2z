"""
Challenge 1: Best Time to Buy and Sell Stock III
=================================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an array of prices, find the maximum profit with at most 2 transactions.
You must sell before buying again.

EXAMPLES
--------
  prices=[3,3,5,0,0,3,1,4] -> 6  (buy@0 sell@5=3, buy@1 sell@4=3)
  prices=[1,2,3,4,5] -> 4  (buy@1 sell@5)
  prices=[7,6,4,3,1] -> 0

CONSTRAINTS
-----------
- 1 <= len(prices) <= 10^5
- 0 <= prices[i] <= 10^5

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(prices: list[int]) -> int:
    """Return max profit with at most 2 transactions."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
