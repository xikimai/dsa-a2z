"""
Warmup 2: Binary Search
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
Given a sorted array of integers and a target value, find the index
of the target using binary search. If the target is not present,
return -1.

INPUT FORMAT
------------
First line: space-separated integers (a sorted array).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer: the index of the target, or -1 if not found.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- The array is sorted in non-decreasing order.

EXAMPLES
--------
Input:
  1 3 5 7 9 11
  7
Output: 3

Input:
  2 4 6 8 10
  2
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Binary search for target in sorted array. Return index or -1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
