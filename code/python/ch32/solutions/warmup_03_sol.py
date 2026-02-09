"""
Solution for Warmup 3: KMP Pattern Search
==========================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
1. Build the KMP failure function for the pattern.
2. Scan the text with two pointers (i for text, j for pattern).
3. On mismatch, use the failure function to jump j back.
4. When j == m, record a match and continue.

TIME COMPLEXITY:  O(n + m)
SPACE COMPLEXITY: O(m)
"""


def solve(text: str, pattern: str) -> list[int]:
    """Return all starting indices where pattern occurs in text using KMP."""
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    # Build failure function
    fail = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            fail[i] = length
            i += 1
        elif length > 0:
            length = fail[length - 1]
        else:
            fail[i] = 0
            i += 1

    # Search
    matches = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = fail[j - 1]
    return matches


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    text = data[0]
    pattern = data[1]
    result = solve(text, pattern)
    print(" ".join(str(r) for r in result))
