"""
Solution for Practice 5: Best Time to Buy and Sell Stock II
==============================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Collect every upward price movement. Greedy / DP equivalence.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(prices: list[int]) -> int:
    """Return max profit with unlimited transactions."""
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
