"""
Warmup 5: Array Intersection
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given two arrays of integers, find the unique elements that appear
in both arrays. Return the result as a sorted list.

INPUT FORMAT
------------
Two lines, each containing space-separated integers.

OUTPUT FORMAT
-------------
A sorted list of unique common elements.

CONSTRAINTS
-----------
- 0 <= len(a), len(b) <= 10^5
- -10^9 <= a[i], b[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 2 1
  2 2
Output: [2]

Input:
  4 9 5
  9 4 9 8 4
Output: [4, 9]

Input:
  1 2 3
  4 5 6
Output: []

HINT
----
Convert both arrays to sets and use set intersection. Then sort
the result.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(a: list[int], b: list[int]) -> list[int]:
    """Return sorted list of unique common elements."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    a = list(map(int, line1.split())) if line1 else []
    b = list(map(int, line2.split())) if line2 else []
    print(solve(a, b))
