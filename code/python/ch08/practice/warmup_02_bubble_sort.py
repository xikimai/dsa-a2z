"""
Warmup 2: Bubble Sort
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Implement Bubble Sort with early termination: repeatedly compare adjacent
elements and swap them if they are out of order. If no swaps occur during
a pass, the array is already sorted — stop early!

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
  64 34 25 12 22 11 90
Output: 11 12 22 25 34 64 90

Input:
  1 2 3 4
Output: 1 2 3 4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using bubble sort with early termination."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
