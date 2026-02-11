"""
Practice 2: Subarray Sum Equals K (Count)
==========================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an array of integers and an integer k, return the total number
of contiguous subarrays whose sum equals k.

INPUT FORMAT
------------
First line: space-separated integers (the array).
Second line: a single integer k.

OUTPUT FORMAT
-------------
A single integer — the count of subarrays with sum equal to k.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- -10^9 <= k <= 10^9

EXAMPLES
--------
Input:
  1 1 1
  2
Output: 2

Input:
  1 2 3
  3
Output: 2

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], k: int) -> int:
    """Return count of subarrays with sum equal to k."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))

