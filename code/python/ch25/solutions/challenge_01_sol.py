"""
Solution for Challenge 1: Shortest Common Supersequence
=========================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
1. Compute the LCS table (2D DP).
2. Backtrack through the table to build the SCS: when chars match,
   include once; otherwise include the char from whichever direction
   we came from.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n) (need full table for backtracking)
"""


def solve(str1: str, str2: str) -> str:
    """Return the shortest common supersequence of str1 and str2."""
    m, n = len(str1), len(str2)
    # Build LCS table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to build SCS
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            result.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            result.append(str1[i - 1])
            i -= 1
        else:
            result.append(str2[j - 1])
            j -= 1

    while i > 0:
        result.append(str1[i - 1])
        i -= 1
    while j > 0:
        result.append(str2[j - 1])
        j -= 1

    return "".join(reversed(result))


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(solve(str1, str2))
