"""
Practice 5: Maximum Subarray Sum (Kadane's Algorithm)
======================================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an integer array, find the contiguous subarray with the largest
sum and return that sum. The subarray must contain at least one element.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the maximum subarray sum.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  -2 1 -3 4 -1 2 1 -5 4
Output: 6

Input:
  5 4 -1 7 8
Output: 23

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> int:
    """Return the maximum subarray sum."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

