"""
Challenge 5: Longest Increasing Subsequence
=============================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an integer array, return the length of the longest strictly
increasing subsequence.

EXAMPLES
--------
  nums=[10,9,2,5,3,7,101,18] -> 4  (e.g., [2,3,7,101])
  nums=[0,1,0,3,2,3] -> 4
  nums=[7,7,7,7] -> 1

CONSTRAINTS
-----------
- 1 <= len(nums) <= 2500
- -10^4 <= nums[i] <= 10^4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int]) -> int:
    """Return the length of the longest increasing subsequence."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
