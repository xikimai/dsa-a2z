"""
Practice 3: Dutch National Flag
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Given an array containing only 0s, 1s, and 2s, sort it in a single pass
using O(n) time and O(1) extra space. This is the famous Dutch National
Flag problem proposed by Edsger Dijkstra.

Use three pointers to partition the array into three regions:
  - [0..lo-1]  = all 0s
  - [lo..mid-1] = all 1s
  - [hi+1..end] = all 2s
  - [mid..hi] = unprocessed

INPUT FORMAT
------------
A single line of space-separated integers (each 0, 1, or 2).

OUTPUT FORMAT
-------------
A single line of space-separated integers in non-decreasing order.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- arr[i] is 0, 1, or 2

EXAMPLES
--------
Input:
  2 0 2 1 1 0
Output: 0 0 1 1 2 2

Input:
  2 1 0
Output: 0 1 2

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort array of 0s, 1s, 2s in single pass, O(n) time, O(1) extra space."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
