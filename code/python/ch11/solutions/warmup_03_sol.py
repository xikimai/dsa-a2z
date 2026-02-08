"""
Solution for Warmup 3: First Non-Repeating Character
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Build a frequency map (Python dicts preserve insertion order since 3.7).
Scan the string again and return the first character with count == 1.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1) — at most 26 lowercase letters
"""


def solve(s: str) -> str:
    """Return first character appearing exactly once, or '_' if none."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return "_"


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
