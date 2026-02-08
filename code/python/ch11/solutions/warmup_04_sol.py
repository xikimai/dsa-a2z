"""
Solution for Warmup 4: Valid Anagram
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Build frequency maps for both strings and compare them.
If the maps are equal, the strings are anagrams.

TIME COMPLEXITY:  O(n) where n = max(len(s1), len(s2))
SPACE COMPLEXITY: O(1) — at most 26 lowercase letters
"""


def solve(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams."""
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
    s1 = input().strip()
    s2 = input().strip()
    print(solve(s1, s2))
