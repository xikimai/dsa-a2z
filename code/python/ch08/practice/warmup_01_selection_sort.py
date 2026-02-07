"""
Warmup 1: Selection Sort
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Implement Selection Sort: repeatedly find the minimum element from the
unsorted portion and swap it into the correct position at the front.

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
  64 25 12 22 11
Output: 11 12 22 25 64

Input:
  1
Output: 1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using selection sort."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
