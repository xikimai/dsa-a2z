"""
Challenge 3: Stock with Transaction Fee
========================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an array of prices and a transaction fee, find the maximum profit
with unlimited transactions where each transaction costs the given fee.

EXAMPLES
--------
  prices=[1,3,2,8,4,9], fee=2 -> 8
  prices=[1,3,7,5,10,3], fee=3 -> 6

CONSTRAINTS
-----------
- 1 <= len(prices) <= 5 * 10^4
- 1 <= prices[i] <= 5 * 10^4
- 0 <= fee <= 5 * 10^4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(prices: list[int], fee: int) -> int:
    """Return max profit with transaction fee."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    parts = input().split()
    fee = int(parts[-1])
    prices = list(map(int, parts[:-1]))
    print(solve(prices, fee))
