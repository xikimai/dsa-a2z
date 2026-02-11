"""
Practice 5: Find Minimum in Rotated Sorted Array
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
You are given a sorted array that has been rotated at some unknown
pivot (e.g., [3, 4, 5, 1, 2] was originally [1, 2, 3, 4, 5]).
Find and return the minimum element. The array contains no duplicates.
Your solution must run in O(log n) time.

INPUT FORMAT
------------
A single line of space-separated integers (a rotated sorted array).

OUTPUT FORMAT
-------------
A single integer: the minimum value in the array.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- All values are distinct.

EXAMPLES
--------
Input:
  3 4 5 1 2
Output: 1

Input:
  4 5 6 7 0 1 2
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> int:
    """Return the minimum value in a rotated sorted array."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
