"""
Warmup 3: Best Time to Buy and Sell Stock
==========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given prices[i] = price on day i, find the maximum profit
from a single buy-sell transaction (buy before sell).

EXAMPLES
--------
>>> solve([7, 1, 5, 3, 6, 4])
5
>>> solve([7, 6, 4, 3, 1])
0

CONSTRAINTS
-----------
- 1 <= len(prices) <= 10^5
- 0 <= prices[i] <= 10^4
"""


def solve(prices: list[int]) -> int:
    """Return the maximum profit from a single buy-sell transaction."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().strip().split()))
    print(solve(prices))
