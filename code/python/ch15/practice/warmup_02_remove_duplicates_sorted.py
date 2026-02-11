"""
Warmup 2: Remove Duplicates from Sorted Array
================================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given a sorted array of integers, remove duplicates in-place and return
the resulting array with each element appearing only once.

INPUT FORMAT
------------
A single line of space-separated integers (sorted, may be empty).

OUTPUT FORMAT
-------------
The de-duplicated array as a list.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- Array is sorted in non-decreasing order

EXAMPLES
--------
Input:
  1 1 2
Output: [1, 2]

Input:
  0 0 1 1 1 2 2 3 3 4
Output: [0, 1, 2, 3, 4]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Return array with duplicates removed."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

