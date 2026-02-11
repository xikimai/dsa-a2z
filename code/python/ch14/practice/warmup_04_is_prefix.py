"""
Warmup 4: Is Array Prefix of Another
======================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given two arrays arr1 and arr2, determine if arr1 is a prefix of arr2.
An array is a prefix if it matches the beginning of the other array
element by element. An empty array is a prefix of any array.

INPUT FORMAT
------------
Two lines, each containing space-separated integers.

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 0 <= len(arr1), len(arr2) <= 10^5
- -10^6 <= elements <= 10^6

EXAMPLES
--------
Input:
  1 2 3
  1 2 3 4 5
Output: True

Input:
  1 2 4
  1 2 3 4 5
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr1: list[int], arr2: list[int]) -> bool:
    """Return True if arr1 is a prefix of arr2."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    arr1 = list(map(int, line1.split())) if line1 else []
    arr2 = list(map(int, line2.split())) if line2 else []
    print(solve(arr1, arr2))

