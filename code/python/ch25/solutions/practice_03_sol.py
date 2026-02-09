"""
Solution for Practice 3: Edit Distance
=========================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Space-optimized 2-row DP.
dp[i][j] = min operations to convert word1[:i] to word2[:j].

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n)
"""


def solve(word1: str, word2: str) -> int:
    """Return the minimum edit distance between word1 and word2."""
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr
    return prev[n]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    word1 = input().strip()
    word2 = input().strip()
    print(solve(word1, word2))
