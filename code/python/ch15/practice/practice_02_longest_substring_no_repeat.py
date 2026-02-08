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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))

