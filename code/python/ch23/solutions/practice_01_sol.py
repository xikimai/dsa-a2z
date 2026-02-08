"""
Solution for Practice 1: Frog Jump with K Steps
===================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
dp[i] = min cost to reach stone i. For each stone, check all possible
jumps from i-1, i-2, ..., i-k. dp[i] = min(dp[j] for valid j) + costs[i].

TIME COMPLEXITY:  O(n * k)
SPACE COMPLEXITY: O(n)
"""


def solve(costs: list[int], k: int) -> int:
    """Return minimum cost for frog to reach the last stone."""
    n = len(costs)
    if n <= 1:
        return costs[0] if n == 1 else 0
    dp = [float('inf')] * n
    dp[0] = costs[0]
    for i in range(1, n):
        for j in range(1, min(k, i) + 1):
            dp[i] = min(dp[i], dp[i - j])
        dp[i] += costs[i]
    return dp[n - 1]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().split()
    k = int(parts[-1])
    costs = list(map(int, parts[:-1]))
    print(solve(costs, k))
