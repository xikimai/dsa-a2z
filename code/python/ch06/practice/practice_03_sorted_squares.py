"""
Practice 3: Sorted Squares
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Given a sorted array of integers (which may include negative numbers),
return an array of the squares of each number, also sorted in ascending
order.

Must be O(n) — use the two-pointer approach.  The key insight: the
largest squares are at the extremes (far left or far right) of the
sorted input, because those have the largest absolute values.

INPUT FORMAT
------------
A single line of space-separated integers (sorted in non-decreasing order).

OUTPUT FORMAT
-------------
Space-separated squared values, sorted in ascending order.

CONSTRAINTS
-----------
- 0 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- Input is sorted in non-decreasing order

EXAMPLES
--------
Input:  -4 -1 0 3 10
Output: 0 1 9 16 100

Input:  -3 -2 -1
Output: 1 4 9

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Return sorted squares of a sorted input array using two pointers."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    print(" ".join(map(str, solve(nums))))
