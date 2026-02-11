"""
Warmup 1: Generate All Permutations
=====================================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given a list of distinct integers, return all possible permutations
in lexicographic (sorted) order.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
Each permutation on its own line as a list.

CONSTRAINTS
-----------
- 1 <= len(nums) <= 8
- -100 <= nums[i] <= 100
- All elements are distinct

EXAMPLES
--------
Input:
  1 2 3
Output:
  [1, 2, 3]
  [1, 3, 2]
  [2, 1, 3]
  [2, 3, 1]
  [3, 1, 2]
  [3, 2, 1]

Input:
  2 1
Output:
  [1, 2]
  [2, 1]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return all permutations of nums, sorted lexicographically."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    for perm in result:
        print(perm)

