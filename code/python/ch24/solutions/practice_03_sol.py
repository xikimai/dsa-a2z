"""
Solution for Practice 3: Maximal Square
=========================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Space-optimized 1D DP. dp[j] = side length of largest square with
bottom-right at (i,j). Track prev_diag for dp[i-1][j-1].
Answer = max_side^2.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the area of the largest square of all 1s."""
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    max_side = 0
    for i in range(m):
        prev_diag = 0
        for j in range(n):
            temp = dp[j]
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], dp[j - 1], prev_diag) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev_diag = temp
    return max_side * max_side


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
