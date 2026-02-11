"""
Warmup 1: Build Prefix Sum Array
==================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an array of integers, build its prefix sum array. The prefix sum
array has length n+1, where prefix[0] = 0 and prefix[i] = sum of the
first i elements.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
The prefix sum array as a list.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  3 1 4 1 5
Output: [0, 3, 4, 8, 9, 14]

Input:
  5
Output: [0, 5]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Return the prefix sum array of length n+1."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

