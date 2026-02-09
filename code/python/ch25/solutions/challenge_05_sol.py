"""
Solution for Challenge 5: Minimum Insertions for Palindrome
==============================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
min_insertions = len(s) - LPS(s), where LPS = Longest Palindromic
Subsequence. LPS(s) = LCS(s, reverse(s)). Use space-optimized LCS.

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n)
"""


def solve(s: str) -> int:
    """Return the minimum number of insertions to make s a palindrome."""
    t = s[::-1]
    n = len(s)
    prev = [0] * (n + 1)
    for i in range(1, n + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    lps = prev[n]
    return n - lps


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
