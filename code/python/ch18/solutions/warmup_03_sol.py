"""
Solution for Warmup 3: Best Time to Buy and Sell Stock
=======================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Track minimum price seen so far. At each day, compute profit if sold today.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(prices: list[int]) -> int:
    """Return the maximum profit from a single buy-sell transaction."""
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().strip().split()))
    print(solve(prices))
