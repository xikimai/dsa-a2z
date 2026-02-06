"""
Solution for Warmup 5: Double List
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Loop through the list by index and multiply each element by 2 in place.
Return the same list object (not a new list).

TIME COMPLEXITY:  O(n) where n = len(nums)
SPACE COMPLEXITY: O(1) — modifies in place
"""


def solve(nums: list[int]) -> list[int]:
    """Double every element in nums in place and return the list."""
    for i in range(len(nums)):
        nums[i] *= 2
    return nums


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    result = solve(nums)
    print(" ".join(map(str, result)))
