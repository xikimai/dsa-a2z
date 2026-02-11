"""
Practice 3: Product of Array Except Self
==========================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an integer array, return an array where each element is the product
of all elements except the one at that index. You must solve it without
using division.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
The result array as a list.

CONSTRAINTS
-----------
- 2 <= len(arr) <= 10^5
- -30 <= arr[i] <= 30
- The product of any prefix or suffix fits in a 32-bit integer

EXAMPLES
--------
Input:
  1 2 3 4
Output: [24, 12, 8, 6]

Input:
  -1 1 0 -3 3
Output: [0, 0, 9, 0, 0]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Return array of products except self, without using division."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(solve(arr))

