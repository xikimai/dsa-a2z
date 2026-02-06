"""
Solution for Practice 2: Anagram Check
========================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Convert both strings to lowercase, then count the frequency of each
character in both. If the frequency maps are identical, the strings
are anagrams.

Alternative: sort both strings and compare. Same result but O(n log n)
instead of O(n).

TIME COMPLEXITY:  O(n) where n = max(len(s1), len(s2))
SPACE COMPLEXITY: O(k) where k = number of unique characters
"""


def solve(s1: str, s2: str) -> bool:
    """Return True if s1 and s2 are anagrams (case-insensitive)."""
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        freq[ch] = freq.get(ch, 0) - 1

    for count in freq.values():
        if count != 0:
            return False
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(solve(s1, s2))
