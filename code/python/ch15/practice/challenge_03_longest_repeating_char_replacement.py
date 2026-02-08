"""
Solution for Challenge 3: Longest Repeating Character Replacement
==================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Sliding window with character frequency tracking. A window is valid
if (window_size - max_frequency) <= k. When invalid, shrink left.

TIME COMPLEXITY:  O(n) — single pass (max_freq tracking is O(1) per step)
SPACE COMPLEXITY: O(1) — at most 26 characters in frequency array
"""


def solve(s: str, k: int) -> int:
    """Return length of longest substring after at most k replacements."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    print(solve(s, k))

