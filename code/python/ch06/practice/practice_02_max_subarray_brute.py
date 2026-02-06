"""
Practice 2: Max Subarray Sum (Brute Force)
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Find the maximum sum of any contiguous subarray using an O(n^2)
brute-force approach.

For each starting index i, compute sums of all subarrays starting
at i and track the overall maximum.

If the list is empty, return 0.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
A single integer: the maximum subarray sum.

CONSTRAINTS
-----------
- 0 <= len(nums) <= 10^4
- -10^4 <= nums[i] <= 10^4

EXAMPLES
--------
Input:  -2 1 -3 4 -1 2 1 -5 4
Output: 6

Input:  5 4 -1 7 8
Output: 23

Input:  -1 -2 -3
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> int:
    """Return the maximum contiguous subarray sum using O(n^2) brute force."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    print(solve(nums))
