"""
Practice 2: House Robber II (Circular)
======================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Houses are arranged in a circle (first and last are adjacent).
Given an array of non-negative integers representing money at each house,
return the maximum amount you can rob without robbing two adjacent houses.

EXAMPLES
--------
  nums=[2,3,2] -> 3
  nums=[1,2,3,1] -> 4
  nums=[1,2,3] -> 3

CONSTRAINTS
-----------
- 1 <= len(nums) <= 100
- 0 <= nums[i] <= 1000

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int]) -> int:
    """Return maximum money from circular houses without robbing adjacent."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
