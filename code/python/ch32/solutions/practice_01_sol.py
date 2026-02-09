"""
Solution for Practice 1: Rabin-Karp Pattern Search
===================================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Compute the hash of the pattern. Slide a window of length m across
the text, updating the hash in O(1) using the rolling hash formula.
When hashes match, verify with actual string comparison.

TIME COMPLEXITY:  O(n + m) expected
SPACE COMPLEXITY: O(1) extra (beyond output)
"""


def solve(text: str, pattern: str) -> list[int]:
    """Return all starting indices where pattern occurs in text using Rabin-Karp."""
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    BASE, MOD = 131, 10**9 + 7

    # Compute hash of pattern and first window of text
    p_hash = 0
    t_hash = 0
    power = pow(BASE, m - 1, MOD)

    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD

    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * power) * BASE
                      + ord(text[i + m])) % MOD
    return matches


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    text = data[0]
    pattern = data[1]
    result = solve(text, pattern)
    print(" ".join(str(r) for r in result))
