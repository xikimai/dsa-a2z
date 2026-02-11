"""
Challenge 1: Three Sum
========================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given an array of integers, find all unique triplets [a, b, c] such
that a + b + c = 0. Return the list of triplets sorted, with no
duplicate triplets.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
A list of triplets.

CONSTRAINTS
-----------
- 3 <= len(nums) <= 3000
- -10^5 <= nums[i] <= 10^5

EXAMPLES
--------
Input:
  -1 0 1 2 -1 -4
Output: [[-1, -1, 2], [-1, 0, 1]]

Input:
  0 0 0
Output: [[0, 0, 0]]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return sorted list of unique triplets that sum to zero."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    print(solve(nums))

