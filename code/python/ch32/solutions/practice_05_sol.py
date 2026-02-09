"""
Solution for Practice 5: Longest Happy Prefix
===============================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Build the KMP failure function. The last value fail[n-1] gives the
length of the longest proper prefix which is also a suffix of the
entire string. Return s[:fail[n-1]].

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(s: str) -> str:
    """Return the longest prefix of s that is also a suffix (not entire string)."""
    n = len(s)
    if n <= 1:
        return ""

    # Build KMP failure function
    fail = [0] * n
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            fail[i] = length
            i += 1
        elif length > 0:
            length = fail[length - 1]
        else:
            fail[i] = 0
            i += 1

    return s[:fail[n - 1]]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
