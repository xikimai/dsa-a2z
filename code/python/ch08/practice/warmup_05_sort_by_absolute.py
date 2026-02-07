"""
Warmup 5: Sort by Absolute Value
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Sort an array of integers by their absolute value in non-decreasing order.
If two elements have the same absolute value, maintain their relative order
from the original array (i.e., the sort must be stable).

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single line of space-separated integers sorted by absolute value.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  3 -1 2 -5 4
Output: -1 2 3 4 -5

Input:
  -10 7 -3 1
Output: 1 -3 7 -10

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array by absolute value (stable)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
