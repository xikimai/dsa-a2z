"""
Solution for Practice 2: Longest Substring Without Repeating Characters
========================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Sliding window with hash map tracking each character's most recent index.
When a repeat is found within the window, jump left past the duplicate.

TIME COMPLEXITY:  O(n) — each character visited once by right pointer
SPACE COMPLEXITY: O(min(n, alphabet_size)) — hash map entries
"""


def solve(s: str) -> int:
    """Return length of longest substring without repeating characters."""
    char_index = {}
    left = 0
    best = 0

    for right in range(len(s)):
        ch = s[right]
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        best = max(best, right - left + 1)

    return best


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))
