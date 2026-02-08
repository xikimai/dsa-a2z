"""
Challenge 2: Generate All Permutations
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Given a list of distinct integers, generate all permutations using
recursion/backtracking. Return the permutations in lexicographic order.

A permutation is a rearrangement of all the elements. For n elements,
there are n! permutations.

INPUT FORMAT
------------
A single line of space-separated integers (or an empty line for []).

OUTPUT FORMAT
-------------
One permutation per line, printed as a Python list.

CONSTRAINTS
-----------
- 0 <= len(nums) <= 8
- -100 <= nums[i] <= 100
- All elements are distinct.

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
  1
Output:
  [1]

HINT
----
Sort the input first. Use a "used" boolean array. At each recursion
level, try each unused element, mark it as used, add it to the current
permutation, recurse, then backtrack (pop and unmark). Because you
iterate in order over a sorted input, permutations come out sorted.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Generate all permutations, sorted lexicographically."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split())) if input().strip() else []
    result = solve(data)
    for perm in result:
        print(perm)
