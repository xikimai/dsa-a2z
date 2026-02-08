"""
Solution for Practice 3: Minimum Window Substring
===================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Build frequency map of t. Sliding window on s: expand right, track
"formed" unique chars. When all formed, shrink left to minimize.

TIME COMPLEXITY:  O(|s| + |t|) — each character enters/leaves window once
SPACE COMPLEXITY: O(|s| + |t|) — hash maps
"""


def solve(s: str, t: str) -> str:
    """Return minimum window substring containing all chars of t."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    t = input()
    print(solve(s, t))

