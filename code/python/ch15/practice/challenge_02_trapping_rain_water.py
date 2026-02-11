"""
Challenge 2: Trapping Rain Water
==================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given an array of non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water can be trapped
after raining.

INPUT FORMAT
------------
A single line of space-separated non-negative integers (may be empty).

OUTPUT FORMAT
-------------
A single integer — the total units of trapped water.

CONSTRAINTS
-----------
- 0 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

EXAMPLES
--------
Input:
  0 1 0 2 1 0 1 3 2 1 2 1
Output: 6

Input:
  4 2 0 3 2 5
Output: 9

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(heights: list[int]) -> int:
    """Return total units of water trapped."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

