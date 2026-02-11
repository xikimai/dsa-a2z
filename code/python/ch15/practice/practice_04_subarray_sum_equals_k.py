"""
Practice 4: Subarray Sum Equals K (Sliding Window)
====================================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given an array of positive integers and a target sum k, count the number
of contiguous subarrays whose sum equals exactly k.

INPUT FORMAT
------------
First line: space-separated positive integers.
Second line: a single integer k.

OUTPUT FORMAT
-------------
A single integer — the count of subarrays with sum equal to k.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- 1 <= arr[i] <= 10^4
- 1 <= k <= 10^9

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
    line = input().strip()
    arr = list(map(int, line.split()))
    k = int(input().strip())
    print(solve(arr, k))

