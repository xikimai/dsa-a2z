"""
Warmup 1: Linear Search
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
Given an array of integers and a target value, find the index of the
first occurrence of the target in the array. If the target is not
present, return -1.

INPUT FORMAT
------------
First line: space-separated integers (the array).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer: the index of the first occurrence, or -1 if not found.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 3 5 7 9
  5
Output: 2

Input:
  1 3 5 7 9
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
