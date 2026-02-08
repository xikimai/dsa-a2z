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
    if not t or not s:
        return ""

    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    required = len(need)
    formed = 0
    window = {}
    left = 0
    best_len = float('inf')
    best_start = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] == need[ch]:
            formed += 1

        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left

            out = s[left]
            window[out] -= 1
            if out in need and window[out] < need[out]:
                formed -= 1
            left += 1

    return "" if best_len == float('inf') else s[best_start:best_start + best_len]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    t = input()
    print(solve(s, t))
