"""
Practice 3: Longest Subarray with Sum K
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an integer array and a target sum K, find the length of the
longest contiguous subarray whose elements sum to K.

INPUT FORMAT
------------
Line 1: space-separated integers (the array).
Line 2: a single integer K.

OUTPUT FORMAT
-------------
A single integer — the length of the longest subarray with sum K.
Return 0 if no such subarray exists.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^5 <= arr[i] <= 10^5
- -10^9 <= K <= 10^9

EXAMPLES
--------
Input:
  1 2 3 1 1 1 1
  3
Output: 3

Input:
  -1 1 1
  1
Output: 3

Input:
  1 -1 1 -1 1
  0
Output: 4

HINT
----
Use prefix sums with a hash map. Store the earliest index where each
prefix sum occurs. If prefix_sum[j] - K appeared at index i, then the
subarray from i+1 to j has sum K.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], k: int) -> int:
    """Return length of longest contiguous subarray with sum K."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
