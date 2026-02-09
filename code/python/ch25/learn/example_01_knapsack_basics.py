"""
Example 01: Knapsack Basics — Step-by-Step 0/1 Knapsack
========================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

This example demonstrates the 0/1 Knapsack problem through
three approaches:
  - Recursion (exponential)
  - Memoization (top-down)
  - Tabulation with space optimization (bottom-up)

We also visualize the DP table to build intuition.
"""


# ── 0/1 Knapsack: Recursive ─────────────────────────────────────

def knapsack_recursive(weights, values, capacity, i=None):
    """O(2^n) — try including or excluding each item."""
    if i is None:
        i = len(weights) - 1
    if i < 0 or capacity <= 0:
        return 0
    # Skip item i
    skip = knapsack_recursive(weights, values, capacity, i - 1)
    # Take item i (only if it fits)
    take = 0
    if weights[i] <= capacity:
        take = values[i] + knapsack_recursive(
            weights, values, capacity - weights[i], i - 1
        )
    return max(skip, take)


# ── 0/1 Knapsack: Memoization ───────────────────────────────────

def knapsack_memo(weights, values, capacity):
    """O(n * capacity) — top-down with cache."""
    n = len(weights)
    memo = {}

    def dp(i, w):
        if i < 0 or w <= 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]
        skip = dp(i - 1, w)
        take = 0
        if weights[i] <= w:
            take = values[i] + dp(i - 1, w - weights[i])
        memo[(i, w)] = max(skip, take)
        return memo[(i, w)]

    return dp(n - 1, capacity)


# ── 0/1 Knapsack: Tabulation (2D) ───────────────────────────────

def knapsack_tabulation(weights, values, capacity):
    """O(n * capacity) time, O(n * capacity) space — bottom-up."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # skip item i-1
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]


# ── 0/1 Knapsack: Space-Optimized (1D) ──────────────────────────

def knapsack_optimized(weights, values, capacity):
    """O(n * capacity) time, O(capacity) space — single row."""
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        # Iterate BACKWARDS so we don't reuse an item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


# ── Table Visualization ─────────────────────────────────────────

def print_knapsack_table(weights, values, capacity):
    """Print the 2D DP table for visualization."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # Print header
    print(f"\n{'':>12}", end="")
    for w in range(capacity + 1):
        print(f"  w={w}", end="")
    print()
    print("  " + "-" * (6 * (capacity + 1) + 12))

    # Print rows
    for i in range(n + 1):
        label = f"  item {i-1} (w={weights[i-1]},v={values[i-1]})" if i > 0 else "  (no items)"
        print(f"{label:>30}", end="  ")
        for w in range(capacity + 1):
            print(f"{dp[i][w]:>4}", end="  ")
        print()

    print(f"\n  Max value = {dp[n][capacity]}")


# ── Demo ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    cap = 7

    print("=" * 60)
    print("0/1 KNAPSACK: Three Approaches")
    print("=" * 60)
    print(f"  Items: weights={weights}, values={values}, capacity={cap}")

    r = knapsack_recursive(weights, values, cap)
    m = knapsack_memo(weights, values, cap)
    t = knapsack_tabulation(weights, values, cap)
    o = knapsack_optimized(weights, values, cap)
    assert r == m == t == o == 9
    print(f"  All approaches give: {o}")

    print_knapsack_table(weights, values, cap)

    # Why iterate backwards in 1D?
    print("\n" + "=" * 60)
    print("WHY BACKWARDS? (1D space optimization)")
    print("=" * 60)
    print("  In 2D: dp[i][w] uses dp[i-1][w-weight], which is the PREVIOUS row.")
    print("  In 1D: if we go left-to-right, dp[w-weight] might already be updated")
    print("  for the CURRENT item — so we'd use the item twice (unbounded!).")
    print("  Going right-to-left ensures dp[w-weight] still holds the old value.")
    print("  This is the KEY difference between 0/1 and unbounded knapsack!")
