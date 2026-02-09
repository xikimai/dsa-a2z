"""
Solution for Practice 1: Shortest Hamiltonian Path
===================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Bitmask DP like TSP but no return to start. Try all starting cities.
dp[mask][i] = min cost to visit cities in mask, ending at i.

TIME COMPLEXITY:  O(2^n * n^2)
SPACE COMPLEXITY: O(2^n * n)
"""


def solve(n: int, dist: list[list[int]]) -> int:
    """Return minimum cost Hamiltonian path (no return to start)."""
    INF = float('inf')
    full = (1 << n) - 1
    dp = [[INF] * n for _ in range(1 << n)]

    # Can start at any city
    for i in range(n):
        dp[1 << i][i] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] >= INF:
                continue
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                cost = dp[mask][u] + dist[u][v]
                if cost < dp[new_mask][v]:
                    dp[new_mask][v] = cost

    ans = INF
    for u in range(n):
        ans = min(ans, dp[full][u])
    return ans


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    dist = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(tokens[idx])); idx += 1
        dist.append(row)
    print(solve(n, dist))
