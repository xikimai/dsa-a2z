"""
Example 02: Greedy vs DP — When Greedy Fails, DP Saves the Day
===============================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

This example demonstrates:
  - Part 1: Coin change — greedy works for US coins, fails for {1, 3, 4}
  - Part 2: Fractional knapsack (greedy) vs 0/1 knapsack (needs DP)
  - Part 3: The exchange argument — proving activity selection is correct
"""


# ── Part 1: Coin Change ────────────────────────────────────────────

def part1_coin_change():
    """Show when greedy coin change works vs fails."""
    print("=" * 60)
    print("PART 1: Coin Change — Greedy vs Optimal")
    print("=" * 60)

    def greedy_coins(denominations, target):
        """Greedy coin change: always pick the largest coin that fits."""
        coins_used = []
        remaining = target
        for coin in sorted(denominations, reverse=True):
            while remaining >= coin:
                coins_used.append(coin)
                remaining -= coin
        return coins_used

    def dp_coins(denominations, target):
        """DP coin change: find minimum coins (always optimal)."""
        dp = [float("inf")] * (target + 1)
        dp[0] = 0
        parent = [-1] * (target + 1)
        for amount in range(1, target + 1):
            for coin in denominations:
                if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                    dp[amount] = dp[amount - coin] + 1
                    parent[amount] = coin
        # Reconstruct
        coins_used = []
        a = target
        while a > 0:
            coins_used.append(parent[a])
            a -= parent[a]
        return coins_used

    # Test 1: US coins
    us_coins = [1, 5, 10, 25]
    target = 41
    greedy_result = greedy_coins(us_coins, target)
    dp_result = dp_coins(us_coins, target)
    print(f"\n  US coins {us_coins}, target = {target}")
    print(f"    Greedy: {greedy_result} ({len(greedy_result)} coins)")
    print(f"    DP:     {dp_result} ({len(dp_result)} coins)")
    print(f"    Same? {len(greedy_result) == len(dp_result)}")

    # Test 2: Tricky coins where greedy fails
    bad_coins = [1, 3, 4]
    target = 6
    greedy_result = greedy_coins(bad_coins, target)
    dp_result = dp_coins(bad_coins, target)
    print(f"\n  Coins {bad_coins}, target = {target}")
    print(f"    Greedy: {greedy_result} ({len(greedy_result)} coins)")
    print(f"    DP:     {dp_result} ({len(dp_result)} coins)")
    print(f"    Same? {len(greedy_result) == len(dp_result)}")
    print(f"    Greedy is {'WRONG' if len(greedy_result) != len(dp_result) else 'correct'}!")

    # Test 3: Another failure case
    bad_coins2 = [1, 5, 6, 9]
    target = 11
    greedy_result = greedy_coins(bad_coins2, target)
    dp_result = dp_coins(bad_coins2, target)
    print(f"\n  Coins {bad_coins2}, target = {target}")
    print(f"    Greedy: {greedy_result} ({len(greedy_result)} coins)")
    print(f"    DP:     {dp_result} ({len(dp_result)} coins)")
    print(f"    Same? {len(greedy_result) == len(dp_result)}")


# ── Part 2: Knapsack ───────────────────────────────────────────────

def part2_knapsack():
    """Compare fractional knapsack (greedy) vs 0/1 knapsack (DP)."""
    print("\n" + "=" * 60)
    print("PART 2: Fractional vs 0/1 Knapsack")
    print("=" * 60)

    items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
    capacity = 50

    # Fractional knapsack (greedy)
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    remaining = capacity
    print(f"\n  Items: {items} (weight, value)")
    print(f"  Capacity: {capacity}")
    print(f"\n  Sorted by ratio (desc): {sorted_items}")
    print(f"  Ratios: {[v / w for w, v in sorted_items]}")

    print("\n  Fractional Knapsack (greedy):")
    for w, v in sorted_items:
        take = min(w, remaining)
        value_taken = take * (v / w)
        total_value += value_taken
        remaining -= take
        print(f"    Item (w={w}, v={v}): take {take}/{w}, value = {value_taken:.1f}")
    print(f"    Total: {total_value:.1f}")

    # 0/1 knapsack (DP) — show that greedy ratio fails
    print("\n  0/1 Knapsack counterexample:")
    items2 = [(6, 8), (5, 5), (5, 5)]
    cap2 = 10
    print(f"    Items: {items2}, Capacity: {cap2}")
    print(f"    Ratios: {[round(v / w, 2) for w, v in items2]}")
    print(f"    Greedy (by ratio): takes (6,8) -> value 8, remaining capacity 4")
    print(f"    No other item fits. Total: 8")
    print(f"    Optimal: takes (5,5) + (5,5) -> value 10")
    print(f"    Greedy is WRONG for 0/1 knapsack!")


# ── Part 3: Exchange Argument Demo ──────────────────────────────────

def part3_exchange_argument():
    """Demonstrate the exchange argument for activity selection."""
    print("\n" + "=" * 60)
    print("PART 3: Exchange Argument — Proving Activity Selection")
    print("=" * 60)

    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]

    # Greedy solution
    sorted_acts = sorted(activities, key=lambda x: x[1])
    greedy_sol = []
    last_end = 0
    for s, e in sorted_acts:
        if s >= last_end:
            greedy_sol.append((s, e))
            last_end = e

    print(f"\n  Activities (sorted by end): {sorted_acts}")
    print(f"  Greedy solution G: {greedy_sol}")

    # Suppose someone has a different "optimal" solution
    alt_sol = [(0, 6), (6, 10)]  # A valid non-overlapping subset
    print(f"  Alternative solution O: {alt_sol}")
    print(f"  |G| = {len(greedy_sol)}, |O| = {len(alt_sol)}")

    print("\n  Exchange argument:")
    print(f"    G picks (1,4) first. O picks (0,6) first.")
    print(f"    end(G[0]) = 4 <= end(O[0]) = 6")
    print(f"    Swap O[0] with G[0]: O becomes [(1,4), (6,10)]")
    print(f"    Still valid! And O now agrees with G on the first pick.")
    print(f"    Continue swapping... O converges to G.")
    print(f"    Since O never got worse, |G| >= |O|.")
    print(f"    Greedy is optimal!")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_coin_change()
    part2_knapsack()
    part3_exchange_argument()
