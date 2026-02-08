"""
Solution for Challenge 2: Trapping Rain Water
==================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Two-pointer approach: maintain left_max and right_max. Water at each
position is min(left_max, right_max) - height[i]. Process from the
side with the smaller max.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(height: list[int]) -> int:
    """Return total trapped water."""
    if len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        height = list(map(int, line.split()))
    else:
        height = []
    print(solve(height))
