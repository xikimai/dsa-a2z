"""
Solution for Challenge 2: Trapping Rain Water
===============================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Two pointers from both ends. Track left_max and right_max.
Process the side with the smaller max — water level there is known.

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(1) — constant extra space
"""


def solve(heights: list[int]) -> int:
    """Return total units of water trapped."""
    if len(heights) < 3:
        return 0

    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]

    return water


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
