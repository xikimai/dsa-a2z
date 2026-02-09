"""
Solution for Practice 5: Count Square Submatrices
===================================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Same DP as Maximal Square, but sum all dp values. dp[j] at (i,j)
gives the side of the largest square ending there, which equals
the count of squares ending at that cell. Sum them all.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""

from typing import List


def solve(matrix: List[List[int]]) -> int:
    """Return the total number of square submatrices with all ones."""
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    total = 0
    for i in range(m):
        prev_diag = 0
        for j in range(n):
            temp = dp[j]
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], dp[j - 1], prev_diag) + 1
                total += dp[j]
            else:
                dp[j] = 0
            prev_diag = temp
    return total


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    matrix = json.loads(sys.stdin.readline())
    print(solve(matrix))
