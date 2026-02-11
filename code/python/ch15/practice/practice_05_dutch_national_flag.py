"""
Practice 5: Dutch National Flag
=================================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given an array containing only 0s, 1s, and 2s, sort it in a single
pass without using a standard sorting algorithm.

INPUT FORMAT
------------
A single line of space-separated integers (each 0, 1, or 2; may be empty).

OUTPUT FORMAT
-------------
The sorted array as a list.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- arr[i] is 0, 1, or 2

EXAMPLES
--------
Input:
  2 0 2 1 1 0
Output: [0, 0, 1, 1, 2, 2]

Input:
  2 0 1
Output: [0, 1, 2]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort array of 0s, 1s, 2s in one pass."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

