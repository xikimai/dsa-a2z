"""
Solution for Practice 4: Cherry Pickup II
===========================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
3D DP bottom-up. dp[c1][c2] = max cherries from current row to last row,
with robot 1 at column c1 and robot 2 at column c2.
Process rows from bottom to top. Each robot has 3 moves.

TIME COMPLEXITY:  O(m * n^2 * 9) = O(m * n^2)
SPACE COMPLEXITY: O(n^2)
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the maximum cherries collected by both robots."""
    m, n = len(grid), len(grid[0])
    # dp[c1][c2] = max cherries from this row onward
    dp = [[-1] * n for _ in range(n)]
    # Base case: last row
    for c1 in range(n):
        for c2 in range(n):
            val = grid[m - 1][c1]
            if c1 != c2:
                val += grid[m - 1][c2]
            dp[c1][c2] = val

    for i in range(m - 2, -1, -1):
        new_dp = [[-1] * n for _ in range(n)]
        for c1 in range(n):
            for c2 in range(n):
                best = -1
                for d1 in [-1, 0, 1]:
                    for d2 in [-1, 0, 1]:
                        nc1, nc2 = c1 + d1, c2 + d2
                        if 0 <= nc1 < n and 0 <= nc2 < n and dp[nc1][nc2] != -1:
                            best = max(best, dp[nc1][nc2])
                if best == -1:
                    continue
                val = grid[i][c1]
                if c1 != c2:
                    val += grid[i][c2]
                new_dp[c1][c2] = val + best
        dp = new_dp

    return dp[0][n - 1] if dp[0][n - 1] != -1 else 0


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
