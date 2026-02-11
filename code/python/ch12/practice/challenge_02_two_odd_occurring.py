"""
Challenge 2: Two Numbers Appearing Odd Times
==============================================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Given an array of integers where every element appears an even number of
times except for exactly two elements (which appear an odd number of times),
find those two elements. Return them in sorted order.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A sorted list of the two odd-occurring elements.

CONSTRAINTS
-----------
- 2 <= len(nums) <= 10^5
- -10^6 <= nums[i] <= 10^6
- Exactly two distinct elements appear an odd number of times

EXAMPLES
--------
Input:
  2 4 7 9 2 4
Output: [7, 9]

Input:
  1 2 3 2 1 4
Output: [3, 4]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Return sorted list of two odd-occurring elements."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))

