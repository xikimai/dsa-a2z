"""
Solution for Challenge 3: Stock with Transaction Fee
=======================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
2-state DP: cash (not holding), hold (holding). Fee paid on sell.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(prices: list[int], fee: int) -> int:
    """Return max profit with transaction fee."""
    if not prices:
        return 0
    cash = 0
    hold = -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().split()
    fee = int(parts[-1])
    prices = list(map(int, parts[:-1]))
    print(solve(prices, fee))
