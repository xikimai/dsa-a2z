"""
Warmup 2: Sort Using Heap (Heapsort)
========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given an unsorted array of integers, return the array sorted in ascending order
using a heap-based approach (heapsort).

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
The sorted array as a list.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  5 3 8 1 2
Output: [1, 2, 3, 5, 8]

Input:
  1
Output: [1]

HINT
----
Push all elements into a min-heap, then pop them all out.
They come out in sorted order!

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Return arr sorted in ascending order using a heap."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
