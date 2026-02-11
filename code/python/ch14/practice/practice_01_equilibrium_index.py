"""
Practice 1: Equilibrium Index
===============================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an array of integers, find the first equilibrium index. An index i
is an equilibrium index if the sum of elements to the left of i equals
the sum of elements to the right of i. Return -1 if no such index exists.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the first equilibrium index, or -1.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  -7 1 5 2 -4 3 0
Output: 3

Input:
  1 2 3
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> int:
    """Return the first equilibrium index, or -1 if none."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

