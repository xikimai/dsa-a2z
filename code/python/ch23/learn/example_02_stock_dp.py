"""
Example 02: Stock DP — State Machine Thinking
==============================================
Chapter 23: Dynamic Programming I — The Foundation

This example demonstrates the stock buy/sell DP family:
  - Stock I:   One transaction (track min price)
  - Stock II:  Unlimited transactions (collect every gain)
  - Stock III: At most 2 transactions (4-state machine)
  - Stock with Cooldown (3-state: held/sold/rest)
  - Stock with Fee (2-state: cash/hold)
"""


# ── Stock I: One Transaction ─────────────────────────────────────

def stock_one(prices):
    """Max profit with at most one buy-sell. O(n) time, O(1) space."""
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


# ── Stock II: Unlimited Transactions ─────────────────────────────

def stock_unlimited(prices):
    """Max profit with unlimited buy-sells. O(n) time, O(1) space."""
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


# ── Stock III: At Most 2 Transactions ────────────────────────────

def stock_two_txn(prices):
    """Max profit with at most 2 buy-sells. O(n) time, O(1) space."""
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


# ── Stock with Cooldown ──────────────────────────────────────────

def stock_cooldown(prices):
    """Max profit with 1-day cooldown after selling. O(n) time, O(1) space."""
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


# ── Stock with Transaction Fee ───────────────────────────────────

def stock_fee(prices, fee):
    """Max profit with transaction fee per trade. O(n) time, O(1) space."""
    if not prices:
        return 0
    cash = 0
    hold = -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash


# ── Demo ──────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("STOCK DP: State Machine Thinking")
    print("=" * 60)

    prices = [7, 1, 5, 3, 6, 4]
    print(f"\n  Prices: {prices}")
    print(f"  Stock I   (one txn):     {stock_one(prices)}")       # 5
    print(f"  Stock II  (unlimited):   {stock_unlimited(prices)}")  # 7
    print()

    prices2 = [3, 3, 5, 0, 0, 3, 1, 4]
    print(f"  Prices: {prices2}")
    print(f"  Stock III (at most 2):   {stock_two_txn(prices2)}")  # 6
    print()

    prices3 = [1, 2, 3, 0, 2]
    print(f"  Prices: {prices3}")
    print(f"  Stock w/ Cooldown:       {stock_cooldown(prices3)}")  # 3
    print()

    prices4 = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(f"  Prices: {prices4}, Fee: {fee}")
    print(f"  Stock w/ Fee:            {stock_fee(prices4, fee)}")  # 8
    print()

    # State machine diagram
    print("  State Machine for Stock with Cooldown:")
    print("  ┌─────────┐   buy    ┌─────────┐")
    print("  │  REST    │────────>│  HELD    │")
    print("  │(no stock)│<───┐   │(holding) │")
    print("  └─────────┘    │    └─────────┘")
    print("       ^         │         │")
    print("       │    cooldown       │ sell")
    print("       │         │         v")
    print("       │    ┌─────────┐")
    print("       └────│  SOLD   │")
    print("            │(just sold)│")
    print("            └─────────┘")


if __name__ == "__main__":
    main()
