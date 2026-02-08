"""
Practice 3: Sliding Window Maximum
======================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given an array of integers and a window size k, return the maximum value
in each sliding window of size k as the window moves left to right.

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= len(nums)

EXAMPLES
--------
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

HINT
----
Use a deque storing indices in decreasing order of their values.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(nums: list[int], k: int) -> list[int]:
    """Return the maximum in each sliding window of size k."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
