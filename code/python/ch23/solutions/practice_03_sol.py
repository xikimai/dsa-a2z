"""
Solution for Practice 3: Decode Ways
========================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
dp[i] = number of decodings for s[0..i-1].
If s[i-1] != '0': dp[i] += dp[i-1]  (single digit decode)
If s[i-2:i] is between "10" and "26": dp[i] += dp[i-2]  (two digit decode)

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(s: str) -> int:
    """Return the number of ways to decode the digit string."""
    if not s or s[0] == '0':
        return 0
    n = len(s)
    prev2 = 1  # dp[i-2], ways to decode empty string
    prev1 = 1  # dp[i-1], ways to decode s[0]
    for i in range(2, n + 1):
        current = 0
        # Single digit
        if s[i - 1] != '0':
            current += prev1
        # Two digits
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            current += prev2
        prev2 = prev1
        prev1 = current
    return prev1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
