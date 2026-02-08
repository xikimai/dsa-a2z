"""
Solution for Warmup 1: Climbing Stairs
=========================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Space-optimized bottom-up DP. dp[i] = dp[i-1] + dp[i-2].

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the number of distinct ways to climb n stairs."""
    if n <= 2:
        return n
    prev2 = 1
    prev1 = 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
