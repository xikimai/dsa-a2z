"""
Challenge 4: Subset Sum
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Given a list of non-negative integers and a target sum, determine
whether any subset of the numbers adds up to exactly the target.
Use recursion to explore all include/exclude choices.

INPUT FORMAT
------------
Line 1: space-separated integers (the array, or empty for []).
Line 2: a single integer (the target sum).

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 0 <= len(nums) <= 20
- 0 <= nums[i] <= 100
- 0 <= target <= 1000

EXAMPLES
--------
Input:
  3 34 4 12 5 2
  9
Output: True

Input:
  3 34 4 12 5 2
  30
Output: False

Input:
  1 2 3
  6
Output: True

HINT
----
Use a helper function with an index and the remaining target.
Base case 1: remaining == 0 means we found a valid subset (return True).
Base case 2: index past the end or remaining < 0 means no solution here.
Recursive case: try including nums[index] (subtract it from remaining)
OR excluding it (keep remaining the same). Return True if either branch
succeeds.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int], target: int) -> bool:
    """Return True if any subset of nums sums to target."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split())) if input().strip() else []
    target = int(input())
    print(solve(data, target))
