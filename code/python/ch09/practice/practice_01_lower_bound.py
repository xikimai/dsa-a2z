"""
Practice 1: Lower Bound
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
Given a sorted array of integers and a target value, find the lower
bound: the index of the first element that is greater than or equal
to the target. If all elements are smaller than the target, return
len(arr) (one past the last index).

INPUT FORMAT
------------
First line: space-separated integers (a sorted array).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer: the first index where arr[i] >= target.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- The array is sorted in non-decreasing order.

EXAMPLES
--------
Input:
  1 3 5 7 9
  5
Output: 2

Input:
  1 3 5 7 9
  4
Output: 2

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Return the first index where arr[i] >= target."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
