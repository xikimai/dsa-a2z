"""
Solution for Practice 1: Container With Most Water
====================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Converging two pointers. Start with widest container, move the
shorter side inward (only way to potentially increase area).

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(1) — constant extra space
"""


def solve(heights: list[int]) -> int:
    """Return maximum water area."""
    left, right = 0, len(heights) - 1
    best = 0

    while left < right:
        width = right - left
        h = min(heights[left], heights[right])
        best = max(best, width * h)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return best


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    arr = list(map(int, line.split()))
    print(solve(arr))
