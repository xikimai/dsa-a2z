"""
Challenge 4: Minimum Operations to Make All Elements Equal
===========================================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an array of integers, find the minimum number of operations to
make all elements equal. In one operation you can increment or decrement
any element by 1. The target value must be one of the existing elements.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the minimum total operations.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  1 2 3
Output: 2

Input:
  1 5
Output: 4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> int:
    """Return minimum operations to make all elements equal."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

