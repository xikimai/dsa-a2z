"""
Solution for Practice 2: Unbounded Knapsack
==============================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Like 0/1 Knapsack but iterate capacity FORWARDS (left to right)
so each item can be reused multiple times.

TIME COMPLEXITY:  O(n * capacity)
SPACE COMPLEXITY: O(capacity)
"""


def solve(weights: list[int], values: list[int], capacity: int) -> int:
    """Return the maximum value with unlimited item reuse."""
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    weights = list(map(int, input().strip().split()))
    values = list(map(int, input().strip().split()))
    capacity = int(input().strip())
    print(solve(weights, values, capacity))
