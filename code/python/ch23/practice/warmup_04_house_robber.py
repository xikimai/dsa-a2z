"""
Warmup 4: House Robber
======================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an array of non-negative integers representing money at each house,
return the maximum amount you can rob without robbing two adjacent houses.

EXAMPLES
--------
  nums=[1,2,3,1] -> 4  (rob house 0 and 2)
  nums=[2,7,9,3,1] -> 12  (rob house 0, 2, 4)

CONSTRAINTS
-----------
- 1 <= len(nums) <= 100
- 0 <= nums[i] <= 400

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int]) -> int:
    """Return maximum money you can rob without robbing adjacent houses."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
