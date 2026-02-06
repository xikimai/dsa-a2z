"""
Practice 3: Two Sum
==============================
Chapter 5: Collections

PROBLEM
-------
Given a list of integers and a target value, return the indices of the
two numbers that add up to the target. If no such pair exists, return
[-1, -1].

You may assume that each input has at most one valid answer, and you
may not use the same element twice.

INPUT FORMAT
------------
First line: space-separated integers (the list).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
Two space-separated indices.

CONSTRAINTS
-----------
- 2 <= len(nums) <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

EXAMPLES
--------
Input:
2 7 11 15
9
Output: 0 1

Input:
3 2 4
6
Output: 1 2

Input:
3 3
6
Output: 0 1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers that sum to target, or [-1, -1]."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    result = solve(nums, target)
    print(" ".join(map(str, result)))
