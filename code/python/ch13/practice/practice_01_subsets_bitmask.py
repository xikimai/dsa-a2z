"""
Practice 1: Subsets Using Bitmasks
====================================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given a list of distinct integers, generate all subsets using bitmask
enumeration. Return subsets sorted by length first, then lexicographically.

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
  [3]
  [1, 2]
  [1, 3]
  [2, 3]
  [1, 2, 3]

Input:
  5
Output:
  []
  [5]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Generate all subsets using bitmasks, sorted by length then lex."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    result = solve(nums)
    for s in result:
        print(s)

