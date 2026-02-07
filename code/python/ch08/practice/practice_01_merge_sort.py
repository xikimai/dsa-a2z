"""
Practice 1: Merge Sort
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Implement Merge Sort: a divide-and-conquer algorithm that splits the array
in half, recursively sorts each half, then merges the two sorted halves
back together. Merge Sort always runs in O(n log n) time.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single line of space-separated integers in non-decreasing order.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  38 27 43 3 9 82 10
Output: 3 9 10 27 38 43 82

Input:
  5 4 3 2 1
Output: 1 2 3 4 5

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using merge sort."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
