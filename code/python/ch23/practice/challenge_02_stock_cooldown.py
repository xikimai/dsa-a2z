"""
Challenge 2: Stock with Cooldown
=================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an array of prices, find the maximum profit with unlimited transactions,
but after selling you must wait one day before buying again (cooldown).

EXAMPLES
--------
  prices=[1,2,3,0,2] -> 3  (buy@1 sell@3, cooldown, buy@0 sell@2)
  prices=[1] -> 0
  prices=[1,2] -> 1

CONSTRAINTS
-----------
- 1 <= len(prices) <= 5000
- 0 <= prices[i] <= 1000

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(prices: list[int]) -> int:
    """Return max profit with cooldown after selling."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
