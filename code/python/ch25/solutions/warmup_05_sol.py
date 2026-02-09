"""
Solution for Warmup 5: Longest Common Subsequence
====================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Space-optimized 2-row DP.
dp[j] = LCS length of text1[:i] and text2[:j].

TIME COMPLEXITY:  O(m * n) where m, n are string lengths
SPACE COMPLEXITY: O(n)
"""


def solve(text1: str, text2: str) -> int:
    """Return the length of the longest common subsequence."""
    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[n]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    text1 = input().strip()
    text2 = input().strip()
    print(solve(text1, text2))
