"""
Challenge 3: Subarray Sum Divisible by K
==========================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an integer array and an integer k, return the number of contiguous
subarrays whose sum is divisible by k.

INPUT FORMAT
------------
First line: space-separated integers (the array).
Second line: a single integer k.

OUTPUT FORMAT
-------------
A single integer — the count of subarrays with sum divisible by k.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- 2 <= k <= 10^4

EXAMPLES
--------
Input:
  4 5 0 -2 -3 1
  5
Output: 7

Input:
  5 10 15
  5
Output: 6

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], k: int) -> int:
    """Return count of subarrays with sum divisible by k."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))

