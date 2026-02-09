"""
Solution for Challenge 1: Dungeon Game
========================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Reverse DP from bottom-right to top-left. dp[j] = minimum health
needed at cell (i,j) to survive to the end.
dp[j] = max(1, min(dp[j], dp[j+1]) - dungeon[i][j]).

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""

from typing import List


def solve(dungeon: List[List[int]]) -> int:
    """Return the minimum initial health to reach the bottom-right."""
    m, n = len(dungeon), len(dungeon[0])
    dp = [float('inf')] * (n + 1)
    dp[n - 1] = 1  # need at least 1 health when reaching the end
    for i in range(m - 1, -1, -1):
        new_dp = [float('inf')] * (n + 1)
        for j in range(n - 1, -1, -1):
            min_next = min(dp[j], new_dp[j + 1])
            new_dp[j] = max(1, min_next - dungeon[i][j])
        dp = new_dp
    return dp[0]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    dungeon = json.loads(sys.stdin.readline())
    print(solve(dungeon))
