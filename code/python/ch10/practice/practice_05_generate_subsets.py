"""
Practice 5: Generate All Subsets (Power Set)
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Given a list of distinct integers, generate all possible subsets
(the power set) using recursion/backtracking.

Return the subsets sorted by length first, then lexicographically.
The input should be sorted before generating subsets.

INPUT FORMAT
------------
A single line of space-separated integers (or an empty line for []).

OUTPUT FORMAT
-------------
One subset per line, printed as a Python list.

CONSTRAINTS
-----------
- 0 <= len(nums) <= 15
- -100 <= nums[i] <= 100
- All elements are distinct.

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
  3 1
Output:
  []
  [1]
  [3]
  [1, 3]

HINT
----
Sort the input first. Use backtracking: at each index, choose to
include or exclude the current element. When you reach the end of
the array, record the current subset. Finally, sort the result by
length first, then lexicographically.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Generate all subsets, sorted by length then lexicographically."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split())) if input().strip() else []
    result = solve(data)
    for subset in result:
        print(subset)
