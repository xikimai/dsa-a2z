"""
Solution for Challenge 4: Cherry Pickup I (3D DP)
==================================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Model as two people walking simultaneously from (0,0) to (n-1,n-1).
After t steps, person 1 is at (r1, c1=t-r1), person 2 at (r2, c2=t-r2).
dp[r1][r2] = max cherries collected after t steps. Iterate over t from 1
to 2*(n-1). If both on same cell, count cherry once.

TIME COMPLEXITY:  O(n^3)
SPACE COMPLEXITY: O(n^2)
"""

from typing import List


def solve(grid: List[List[int]]) -> int:
    """Return the maximum cherries collected on a round trip."""
    n = len(grid)
    if n == 0 or grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
        return 0

    NEG_INF = float('-inf')
    dp = [[NEG_INF] * n for _ in range(n)]
    dp[0][0] = grid[0][0]

    max_t = 2 * (n - 1)
    for t in range(1, max_t + 1):
        new_dp = [[NEG_INF] * n for _ in range(n)]
        r_lo = max(0, t - (n - 1))
        r_hi = min(n - 1, t)
        for r1 in range(r_lo, r_hi + 1):
            c1 = t - r1
            if c1 < 0 or c1 >= n or grid[r1][c1] == -1:
                continue
            for r2 in range(r_lo, r_hi + 1):
                c2 = t - r2
                if c2 < 0 or c2 >= n or grid[r2][c2] == -1:
                    continue
                best = NEG_INF
                for pr1 in [r1, r1 - 1]:
                    for pr2 in [r2, r2 - 1]:
                        if 0 <= pr1 < n and 0 <= pr2 < n:
                            best = max(best, dp[pr1][pr2])
                if best == NEG_INF:
                    continue
                cherries = grid[r1][c1]
                if r1 != r2:
                    cherries += grid[r2][c2]
                new_dp[r1][r2] = best + cherries
        dp = new_dp

    return max(0, dp[n - 1][n - 1])


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    grid = json.loads(sys.stdin.readline())
    print(solve(grid))
