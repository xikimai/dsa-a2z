"""
Warmup 3: Max Sum of Fixed Window
====================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given an array of integers and a window size k, find the maximum sum
of any k consecutive elements. Return 0 if k is larger than the array.

INPUT FORMAT
------------
First line: space-separated integers (may be empty).
Second line: a single integer k.

OUTPUT FORMAT
-------------
A single integer — the maximum window sum.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- 1 <= k <= 10^5

EXAMPLES
--------
Input:
  2 1 5 1 3 2
  3
Output: 9

Input:
  -1 -2 -3 -4
  2
Output: -3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], k: int) -> int:
    """Return maximum sum of k consecutive elements."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    k = int(input().strip())
    print(solve(arr, k))

