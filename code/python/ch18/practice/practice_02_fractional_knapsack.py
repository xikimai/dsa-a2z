"""
Practice 2: Fractional Knapsack
=================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given items with (weight, value) and a knapsack capacity,
maximize the total value. You can take fractions of items.

EXAMPLES
--------
>>> solve(50, [(10, 60), (20, 100), (30, 120)])
240.0

CONSTRAINTS
-----------
- 0 <= capacity <= 10^6
- 0 <= n <= 10^4
- weight > 0, value >= 0
"""


def solve(capacity: int, items: list[tuple[int, int]]) -> float:
    """Return maximum value achievable with fractional items."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    cap = int(input().strip())
    n = int(input().strip())
    items = []
    for _ in range(n):
        w, v = map(int, input().strip().split())
        items.append((w, v))
    print(f"{solve(cap, items):.4f}")
