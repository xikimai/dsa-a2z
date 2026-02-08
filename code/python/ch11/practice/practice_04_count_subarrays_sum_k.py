"""
Practice 4: Count Subarrays with Sum K
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an integer array and a target sum K, count the total number
of contiguous subarrays whose elements sum to K.

INPUT FORMAT
------------
Line 1: space-separated integers (the array).
Line 2: a single integer K.

OUTPUT FORMAT
-------------
A single integer — the count of subarrays with sum K.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^5 <= arr[i] <= 10^5
- -10^9 <= K <= 10^9

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

Input:
  0 0 0
  0
Output: 6

HINT
----
Use prefix sums with a frequency hash map. Initialize with {0: 1}.
For each prefix sum, add the count of (prefix_sum - K) from the map,
then increment the count of the current prefix sum.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], k: int) -> int:
    """Count contiguous subarrays whose sum equals K."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(solve(arr, k))
