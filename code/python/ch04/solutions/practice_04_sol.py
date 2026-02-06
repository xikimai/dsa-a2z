"""
Solution for Practice 4: Statistics
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Implement find_min, find_max, and find_average manually using loops
(without built-in min, max, or sum). Combine them in solve to return
[min, max, average] as floats.

TIME COMPLEXITY:  O(n) where n = len(nums) — three passes
SPACE COMPLEXITY: O(1)
"""


def find_min(nums: list[int]) -> int:
    """Return the minimum value in nums (no built-in min)."""
    result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < result:
            result = nums[i]
    return result


def find_max(nums: list[int]) -> int:
    """Return the maximum value in nums (no built-in max)."""
    result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > result:
            result = nums[i]
    return result


def find_average(nums: list[int]) -> float:
    """Return the average of nums rounded to 2 decimal places (no built-in sum)."""
    total = 0
    for num in nums:
        total += num
    return round(total / len(nums), 2)


def solve(nums: list[int]) -> list[float]:
    """Return [min, max, average] as floats."""
    return [float(find_min(nums)), float(find_max(nums)), find_average(nums)]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    print(" ".join(str(x) for x in result))
