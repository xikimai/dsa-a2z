"""
Solution for Challenge 2: Stock with Cooldown
================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
3-state DP: held (holding stock), sold (just sold), rest (idle/cooldown).

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(prices: list[int]) -> int:
    """Return max profit with cooldown after selling."""
    if not prices:
        return 0
    held = -prices[0]
    sold = 0
    rest = 0
    for price in prices[1:]:
        prev_held = held
        held = max(held, rest - price)
        rest = max(rest, sold)
        sold = prev_held + price
    return max(sold, rest)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    prices = list(map(int, input().split()))
    print(solve(prices))
