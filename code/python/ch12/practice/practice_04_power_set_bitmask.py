"""
Practice 4: Power Set Using Bitmasks
======================================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Given a list of distinct integers, return all possible subsets (the power
set) using bitmask enumeration. Subsets should be ordered by their bitmask
value (0 to 2^n - 1).

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
Each subset on its own line as a list.

CONSTRAINTS
-----------
- 0 <= len(nums) <= 15
- -100 <= nums[i] <= 100
- All elements are distinct

EXAMPLES
--------
Input:
  1 2 3
Output:
  []
  [1]
  [2]
  [1, 2]
  [3]
  [1, 3]
  [2, 3]
  [1, 2, 3]

Input:
  (empty)
Output:
  []

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return all subsets using bitmask enumeration."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    result = solve(nums)
    for subset in result:
        print(subset)

