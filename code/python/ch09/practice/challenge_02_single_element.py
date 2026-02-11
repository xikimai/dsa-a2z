"""
Challenge 2: Single Element in Sorted Array
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
You are given a sorted array where every element appears exactly twice,
except for one element which appears exactly once. Find and return that
single element. Your solution must run in O(log n) time.

INPUT FORMAT
------------
A single line of space-separated integers (a sorted array).

OUTPUT FORMAT
-------------
A single integer: the element that appears only once.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- len(arr) is always odd.
- Every element appears exactly twice except for one.
- The array is sorted in non-decreasing order.

EXAMPLES
--------
Input:
  1 1 2 3 3 4 4 8 8
Output: 2

Input:
  3 3 7 7 10 11 11
Output: 10

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> int:
    """Find the element that appears exactly once."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
