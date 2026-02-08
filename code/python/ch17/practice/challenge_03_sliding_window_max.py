"""
Challenge 3: Sliding Window Maximum
=======================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given an array of integers and a window size k, return an array of the
maximum value in each sliding window of size k as it moves from left to right.

INPUT FORMAT
------------
Line 1: space-separated integers (the array)
Line 2: integer k (window size)

OUTPUT FORMAT
-------------
A list of integers — the maximum in each window.

CONSTRAINTS
-----------
- 1 <= k <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4

EXAMPLES
--------
Input:
  1 3 -1 -3 5 3 6 7
  3
Output: [3, 3, 5, 5, 6, 7]
Explanation:
  Window [1,3,-1] max=3; [3,-1,-3] max=3; [-1,-3,5] max=5;
  [-3,5,3] max=5; [5,3,6] max=6; [3,6,7] max=7

Input:
  1
  1
Output: [1]

HINT
----
Option A (deque): Maintain a monotone decreasing deque of indices.
Option B (heap): Use a max-heap with lazy deletion — pop elements
  whose index is outside the window.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int], k: int) -> list[int]:
    """Return the maximum in each sliding window of size k."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
