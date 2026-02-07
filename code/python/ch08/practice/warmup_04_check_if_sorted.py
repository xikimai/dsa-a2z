"""
Warmup 4: Check If Sorted
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Given an array of integers, return True if the array is sorted in
non-decreasing order, and False otherwise. An empty array or an array
with a single element is considered sorted.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
True or False

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  1 2 3 4 5
Output: True

Input:
  1 3 2 4 5
Output: False

Input:

Output: True

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> bool:
    """Return True if the array is sorted in non-decreasing order."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    data = list(map(int, line.split())) if line else []
    print(solve(data))
