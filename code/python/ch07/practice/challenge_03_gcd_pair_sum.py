"""
Challenge 3: Sum of GCD Pairs
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given a list of positive integers nums, compute the sum of
GCD(nums[i], nums[j]) for all pairs where i < j.

For example, given [2, 4, 6]:
  GCD(2,4) + GCD(2,6) + GCD(4,6) = 2 + 2 + 2 = 6

If the list has fewer than 2 elements, the sum is 0.

INPUT FORMAT
------------
A single line of space-separated positive integers.

OUTPUT FORMAT
-------------
A single integer: the sum of GCDs of all pairs.

CONSTRAINTS
-----------
- 1 <= len(nums) <= 1000
- 1 <= nums[i] <= 10^6

EXAMPLES
--------
Input:
  2 4 6
Output: 6

Input:
  3 6 9
Output: 9

Input:
  12 18 24
Output: 24

Input:
  7
Output: 0

Input:
  2 3 5 7
Output: 6

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> int:
    """Return the sum of GCD(nums[i], nums[j]) for all i < j."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
