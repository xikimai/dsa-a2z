"""
Practice 2: Quick Sort
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Implement Quick Sort using the Lomuto partition scheme: choose the last
element as the pivot, partition the array so all elements <= pivot are
on the left and all elements > pivot are on the right, then recursively
sort each side.

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
  10 7 8 9 1 5
Output: 1 5 7 8 9 10

Input:
  3 2 1
Output: 1 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using quick sort with Lomuto partition."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
