"""
Solution for Practice 3: Minimum Score Triangulation of Polygon
================================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Interval DP. dp[i][j] = min score to triangulate polygon vertices i..j.
For each pair (i, j), try every intermediate vertex k as the triangle
(i, k, j). The edge (i, j) is shared, k is the apex.

TIME COMPLEXITY:  O(n^3)
SPACE COMPLEXITY: O(n^2)
"""


def solve(values: list[int]) -> int:
    """Return minimum score triangulation of the polygon."""
    n = len(values)
    if n < 3:
        return 0

    dp = [[0] * n for _ in range(n)]

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    values = [int(x) for x in tokens]
    print(solve(values))
