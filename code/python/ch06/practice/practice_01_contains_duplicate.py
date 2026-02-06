"""
Practice 1: Contains Duplicate
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Given a list of integers, return True if any value appears at least
twice in the list.  Return False if every element is distinct.

Use a set for O(n) time complexity.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
True or False

CONSTRAINTS
-----------
- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

EXAMPLES
--------
Input:  1 2 3 1
Output: True

Input:  1 2 3 4
Output: False

Input:  (empty)
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> bool:
    """Return True if any value appears at least twice."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    print(solve(nums))
