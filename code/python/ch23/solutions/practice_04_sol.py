"""
Solution for Practice 4: Best Time to Buy and Sell Stock I
=============================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Track min price so far. At each day, profit = price - min_price.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(prices: list[int]) -> int:
    """Return max profit from one buy-sell transaction."""
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
