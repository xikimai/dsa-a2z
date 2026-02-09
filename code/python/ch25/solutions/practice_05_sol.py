"""
Solution for Practice 5: Distinct Subsequences
=================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Space-optimized 1D DP.
dp[j] = number of ways to form t[:j] from s[:i].
Iterate j backwards to avoid overwriting needed values.

TIME COMPLEXITY:  O(m * n) where m = len(s), n = len(t)
SPACE COMPLEXITY: O(n)
"""


def solve(s: str, t: str) -> int:
    """Return the count of distinct subsequences of s that equal t."""
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1  # empty t is always a subsequence
    for i in range(1, m + 1):
        for j in range(min(i, n), 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[n]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(solve(s, t))
