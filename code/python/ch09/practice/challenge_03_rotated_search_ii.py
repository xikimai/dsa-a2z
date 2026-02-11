"""
Challenge 3: Search in Rotated Sorted Array with Duplicates
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
You are given a sorted array that has been rotated at some unknown
pivot, and it MAY contain duplicate values. Given a target value,
return True if the target exists in the array, or False otherwise.

INPUT FORMAT
------------
First line: space-separated integers (a rotated sorted array with possible duplicates).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- The array may contain duplicates.

EXAMPLES
--------
Input:
  2 5 6 0 0 1 2
  0
Output: True

Input:
  2 5 6 0 0 1 2
  3
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> bool:
    """Search for target in a rotated sorted array with duplicates."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
