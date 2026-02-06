"""
Solution for Warmup 2: Reverse List
============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Two-pointer technique: place one pointer at the start and one at the end.
Swap the elements at these positions, then move both pointers inward.
Continue until they meet in the middle.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1) — done in place
"""


def solve(nums: list[int]) -> list[int]:
    """Reverse the list in place and return it."""
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    print(" ".join(map(str, result)))
