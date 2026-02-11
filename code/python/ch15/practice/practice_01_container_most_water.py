"""
Practice 1: Container With Most Water
=======================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given an array of non-negative integers where each element represents
the height of a vertical line, find two lines that together with the
x-axis form a container holding the most water. Return the maximum area.

INPUT FORMAT
------------
A single line of space-separated non-negative integers.

OUTPUT FORMAT
-------------
A single integer — the maximum water area.

CONSTRAINTS
-----------
- 2 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

EXAMPLES
--------
Input:
  1 8 6 2 5 4 8 3 7
Output: 49

Input:
  1 1
Output: 1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(heights: list[int]) -> int:
    """Return maximum water area."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    arr = list(map(int, line.split()))
    print(solve(arr))

