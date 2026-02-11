"""
Practice 4: Search in Rotated Sorted Array
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
You are given a sorted array that has been rotated at some unknown
pivot (e.g., [4, 5, 6, 7, 0, 1, 2] was originally [0, 1, 2, 4, 5, 6, 7]).
The array contains no duplicate values. Given a target value, return
its index, or -1 if it is not in the array. Your solution must run
in O(log n) time.

INPUT FORMAT
------------
First line: space-separated integers (a rotated sorted array).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer: the index of the target, or -1 if not found.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- All values are distinct.

EXAMPLES
--------
Input:
  4 5 6 7 0 1 2
  0
Output: 4

Input:
  4 5 6 7 0 1 2
  3
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Search for target in a rotated sorted array (no duplicates)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
