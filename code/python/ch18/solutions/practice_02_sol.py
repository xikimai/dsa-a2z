"""
Solution for Practice 2: Fractional Knapsack
==============================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Sort by value/weight ratio descending. Take greedily.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(1) extra
"""


def solve(capacity: int, items: list[tuple[int, int]]) -> float:
    """Return maximum value achievable with fractional items."""
    if capacity == 0 or not items:
        return 0.0
    # Sort by value/weight ratio descending
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    remaining = capacity
    for weight, value in items:
        if remaining <= 0:
            break
        take = min(weight, remaining)
        total_value += take * (value / weight)
        remaining -= take
    return total_value


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    cap = int(input().strip())
    n = int(input().strip())
    items = []
    for _ in range(n):
        w, v = map(int, input().strip().split())
        items.append((w, v))
    print(f"{solve(cap, items):.4f}")
