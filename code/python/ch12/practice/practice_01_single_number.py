"""
Practice 1: Single Number
===========================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Given a non-empty array of integers where every element appears exactly
twice except for one, find that single element.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the element that appears only once.

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^5
- -10^6 <= nums[i] <= 10^6
- Every element appears twice except one

EXAMPLES
--------
Input:
  4 1 2 1 2
Output: 4

Input:
  2 2 1
Output: 1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> int:
    """Return the element that appears only once."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))

