"""
Challenge 4: Fence Painting (USACO Bronze Style)
==================================================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given N fence segments, each defined by a start and end position on a
number line, compute the total length of fence that is painted. Overlapping
segments should not be double-counted.

INPUT FORMAT
------------
First line: integer N (number of segments).
Next N lines: two integers (start and end of each segment).

OUTPUT FORMAT
-------------
A single integer — the total painted length.

CONSTRAINTS
-----------
- 1 <= N <= 10^4
- -10^6 <= start < end <= 10^6

EXAMPLES
--------
Input:
  2
  1 5
  3 8
Output: 7

Input:
  2
  1 3
  5 7
Output: 4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(fences: list[list[int]]) -> int:
    """Return total painted length (no double counting)."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    fences = []
    for _ in range(n):
        s, e = map(int, input().split())
        fences.append([s, e])
    print(solve(fences))

