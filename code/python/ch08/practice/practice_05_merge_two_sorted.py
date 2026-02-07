"""
Practice 5: Merge Two Sorted Arrays
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Given two sorted arrays, merge them into a single sorted array without
using a built-in sort function. Use a two-pointer approach: compare the
front elements of both arrays and take the smaller one each time.

INPUT FORMAT
------------
Two lines of space-separated integers (each line is a sorted array).
A line may be empty (representing an empty array).

OUTPUT FORMAT
-------------
A single line of space-separated integers: the merged sorted array.

CONSTRAINTS
-----------
- 0 <= len(arr1), len(arr2) <= 10^5
- -10^6 <= elements <= 10^6
- Both input arrays are sorted in non-decreasing order

EXAMPLES
--------
Input:
  1 3 5
  2 4 6
Output: 1 2 3 4 5 6

Input:

  1 2 3
Output: 1 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    """Merge two sorted arrays into one sorted array."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    arr1 = list(map(int, line1.split())) if line1 else []
    arr2 = list(map(int, line2.split())) if line2 else []
    print(*solve(arr1, arr2))
