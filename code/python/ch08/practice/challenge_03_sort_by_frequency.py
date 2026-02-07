"""
Challenge 3: Sort by Frequency
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Sort an array by frequency: elements with higher frequency come first.
If two elements have the same frequency, the one with the smaller value
comes first (tiebreak by value ascending).

For example, [1,1,2,2,2,3] → [2,2,2,1,1,3] because 2 appears 3 times,
1 appears 2 times, and 3 appears 1 time.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single line of space-separated integers sorted by frequency.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  1 1 2 2 2 3
Output: 2 2 2 1 1 3

Input:
  3 3 1 1 2 2
Output: 1 1 2 2 3 3

Input:
  1 2 3
Output: 1 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Sort by frequency descending, tiebreak by value ascending."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
