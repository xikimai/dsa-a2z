"""
Warmup 4: Move Zeros to End
==============================
Chapter 15: Two Pointers & Sliding Window — The Dance of Indices

PROBLEM
-------
Given an array of integers, move all zeros to the end while maintaining
the relative order of the non-zero elements.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
The modified array as a list.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  0 1 0 3 12
Output: [1, 3, 12, 0, 0]

Input:
  0 0 1
Output: [1, 0, 0]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Return array with zeros moved to end."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

