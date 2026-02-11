"""
Warmup 1: Pair Sum in Sorted Array
====================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given a sorted array of integers and a target sum, find a pair of
elements that add up to the target. Return the pair [a, b] with the
smallest a. If no pair exists, return [-1, -1].

INPUT FORMAT
------------
First line: space-separated integers (sorted array, may be empty).
Second line: a single integer (target sum).

OUTPUT FORMAT
-------------
A list of two integers, or [-1, -1].

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- Array is sorted in non-decreasing order

EXAMPLES
--------
Input:
  1 3 5 8 12 15
  13
Output: [1, 12]

Input:
  1 2 3 4 5
  10
Output: [-1, -1]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> list[int]:
    """Return pair [a, b] that sums to target, or [-1, -1]."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))

