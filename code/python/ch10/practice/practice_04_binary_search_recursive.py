"""
Practice 4: Binary Search (Recursive)
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Given a sorted array of integers and a target value, find the index
of the target using a recursive binary search. Return -1 if the
target is not in the array.

INPUT FORMAT
------------
Line 1: space-separated integers (a sorted array).
Line 2: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer — the index of the target, or -1 if not found.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- The array is sorted in non-decreasing order.

EXAMPLES
--------
Input:
  1 3 5 7 9 11
  7
Output: 3

Input:
  2 4 6 8 10
  5
Output: -1

Input:
  10
  10
Output: 0

HINT
----
Write a helper function with lo and hi bounds. Compute mid, compare
arr[mid] with target, and recurse on the left or right half. Base
case: lo > hi means the target is not present (return -1).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Binary search using recursion. Return index or -1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
