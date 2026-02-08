"""
Solution for Warmup 3: Min Cost Climbing Stairs
===================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
dp[i] = min cost to reach step i. Can start at 0 or 1. Need to reach n (top).
dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]) for i >= 2.
Base: dp[0] = 0, dp[1] = 0 (can start at either).

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(cost: list[int]) -> int:
    """Return minimum cost to reach the top of the staircase."""
    n = len(cost)
    prev2 = 0  # cost to reach step 0 (free start)
    prev1 = 0  # cost to reach step 1 (free start)
    for i in range(2, n + 1):
        current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2 = prev1
        prev1 = current
    return prev1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    cost = list(map(int, input().split()))
    print(solve(cost))
