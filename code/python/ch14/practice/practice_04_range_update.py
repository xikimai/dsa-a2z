"""
Practice 4: Range Update with Difference Array
================================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an array of size n (initially all zeros) and a list of range
updates, each of the form [l, r, val] meaning "add val to all elements
from index l to r (inclusive)", return the final array after all updates.

INPUT FORMAT
------------
First line: integer n (array size).
Second line: integer q (number of updates).
Next q lines: three integers l, r, val.

OUTPUT FORMAT
-------------
The final array as a list.

CONSTRAINTS
-----------
- 1 <= n <= 10^5
- 1 <= q <= 10^5
- 0 <= l <= r < n
- -10^6 <= val <= 10^6

EXAMPLES
--------
Input:
  5
  3
  1 3 2
  2 4 3
  0 1 -1
Output: [-1, 1, 5, 5, 3]

Input:
  4
  1
  0 3 5
Output: [5, 5, 5, 5]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, updates: list[list[int]]) -> list[int]:
    """Return the final array after all range updates."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    q = int(input())
    updates = []
    for _ in range(q):
        parts = list(map(int, input().split()))
        updates.append(parts)
    print(solve(n, updates))

