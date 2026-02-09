"""
Solution for Practice 6: Wildcard Matching
============================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
2D DP. dp[i][j] = True if s[:i] matches p[:j].
Space-optimized to two rows.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(n) where n = len(p)
"""


def solve(s: str, p: str) -> bool:
    """Return True if s matches pattern p with wildcards."""
    m, n = len(s), len(p)
    prev = [False] * (n + 1)
    prev[0] = True
    # Base: empty s matches p only if all '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            prev[j] = prev[j - 1]
        else:
            break
    for i in range(1, m + 1):
        curr = [False] * (n + 1)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' matches empty (curr[j-1]) or one more char (prev[j])
                curr[j] = curr[j - 1] or prev[j]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                curr[j] = prev[j - 1]
        prev = curr
    return prev[n]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    s = input().strip()
    p = input().strip()
    print(solve(s, p))
