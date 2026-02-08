"""
Warmup 4: Check if Array is a Min-Heap
==========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given an array of integers, determine whether it satisfies the min-heap
property: for every node at index i, arr[i] <= arr[2*i+1] (if exists)
and arr[i] <= arr[2*i+2] (if exists).

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
True or False

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 3 2 7 6 5 4
Output: True

Input:
  1 2 3 4 5 6 7
Output: True

Input:
  7 3 2 1 6 5 4
Output: False

HINT
----
Check every parent node (indices 0 to n//2 - 1) against its children.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> bool:
    """Return True if arr satisfies the min-heap property."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
