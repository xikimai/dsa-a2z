"""
Solution for Practice 3: Count Distinct Substrings
====================================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Generate all substrings and add them to a set. The count is
len(set) + 1 (for the empty string, which we count separately).

For larger inputs, a Trie or suffix array with LCP would be more
efficient, but for s up to 1000, O(n^2) substring generation works.

TIME COMPLEXITY:  O(n^2) for generating and hashing substrings
SPACE COMPLEXITY: O(n^2)
"""


def solve(s: str) -> int:
    """Count the number of distinct substrings of s (including empty string)."""
    substrings = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])
    return len(substrings) + 1  # +1 for empty string


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
