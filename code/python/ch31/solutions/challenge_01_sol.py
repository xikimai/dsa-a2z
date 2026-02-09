"""
Solution for Challenge 1: Minimum Cost to Merge Stones
=======================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Interval DP. Each merge reduces pile count by k-1. So we need
(n-1) % (k-1) == 0 for it to be possible. dp[i][j] = min cost
to merge piles i..j into as few piles as possible. Only add
prefix sum when the range can be merged into one pile.

TIME COMPLEXITY:  O(n^3)
SPACE COMPLEXITY: O(n^2)
"""


def solve(stones: list[int], k: int) -> int:
    """Return minimum cost to merge all stones, or -1 if impossible."""
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1
    if n == 1:
        return 0

    # Prefix sums for range sum queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]

    def range_sum(i, j):
        return prefix[j + 1] - prefix[i]

    INF = float('inf')
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            # Try all split points with step k-1
            for mid in range(i, j, k - 1):
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
            # If this range can be merged into one pile, add the cost
            if (j - i) % (k - 1) == 0:
                dp[i][j] += range_sum(i, j)

    return dp[0][n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    k_val = int(tokens[idx]); idx += 1
    stones = []
    for _ in range(n):
        stones.append(int(tokens[idx])); idx += 1
    print(solve(stones, k_val))
