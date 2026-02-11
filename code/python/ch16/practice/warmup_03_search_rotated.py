"""
Warmup 3: Search in Rotated Sorted Array
==========================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given a sorted array that has been rotated at some pivot, search for a
target value and return its index. Return -1 if not found. All elements
are distinct.

INPUT FORMAT
------------
First line: space-separated integers (rotated sorted array, may be empty).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer — the index of the target, or -1.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- All elements are distinct

EXAMPLES
--------
Input:
  4 5 6 7 0 1 2
  0
Output: 4

Input:
  4 5 6 7 0 1 2
  3
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Return index of target in rotated sorted array, or -1."""
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
