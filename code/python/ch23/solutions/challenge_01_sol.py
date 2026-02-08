"""
Solution for Challenge 1: Best Time to Buy and Sell Stock III
================================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Track 4 states: buy1, sell1, buy2, sell2. Process each price, updating
states in order.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(prices: list[int]) -> int:
    """Return max profit with at most 2 transactions."""
    if not prices:
        return 0
    buy1 = -prices[0]
    sell1 = 0
    buy2 = -prices[0]
    sell2 = 0
    for price in prices[1:]:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    return sell2


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
