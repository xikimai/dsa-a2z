"""
Warmup 3: First Occurrence
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
Given a sorted array of integers (which may contain duplicates) and a
target value, find the index of the FIRST occurrence of the target.
If the target is not present, return -1.

INPUT FORMAT
------------
First line: space-separated integers (a sorted array).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer: the index of the first occurrence, or -1 if not found.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- The array is sorted in non-decreasing order.

EXAMPLES
--------
Input:
  1 2 2 2 3 4
  2
Output: 1

Input:
  1 3 5 7
  4
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Return the index of the first occurrence of target, or -1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
