"""
Solution for Challenge 4: Palindrome Partitioning II
=====================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
1. Precompute is_pal[i][j] = whether s[i..j] is a palindrome using DP.
2. dp[i] = minimum cuts to partition s[0..i] into palindromes.
   dp[i] = 0 if s[0..i] is a palindrome, else
   dp[i] = min(dp[j] + 1) for all j where s[j+1..i] is a palindrome.

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n^2)
"""


def solve(s: str) -> int:
    """Return minimum cuts to partition s into palindromes."""
    n = len(s)
    if n <= 1:
        return 0

    # Precompute palindrome table
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for i in range(n - 1):
        is_pal[i][i + 1] = (s[i] == s[i + 1])
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_pal[i][j] = (s[i] == s[j]) and is_pal[i + 1][j - 1]

    # DP for minimum cuts
    dp = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            dp[i] = i  # worst case: cut every character
            for j in range(1, i + 1):
                if is_pal[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[n - 1]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
