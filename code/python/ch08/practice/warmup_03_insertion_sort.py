"""
Warmup 3: Insertion Sort
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Implement Insertion Sort: build a sorted array one element at a time by
picking the next element and inserting it into the correct position among
the already-sorted elements on the left.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single line of space-separated integers in non-decreasing order.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 1000
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  12 11 13 5 6
Output: 5 6 11 12 13

Input:
  3 2 1
Output: 1 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using insertion sort."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
