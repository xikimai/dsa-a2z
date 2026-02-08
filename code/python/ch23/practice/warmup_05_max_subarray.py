"""
Warmup 5: Maximum Subarray
==========================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an integer array, find the contiguous subarray with the largest
sum and return that sum.

EXAMPLES
--------
  nums=[-2,1,-3,4,-1,2,1,-5,4] -> 6
  nums=[1] -> 1
  nums=[5,4,-1,7,8] -> 23

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int]) -> int:
    """Return the maximum contiguous subarray sum."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
