"""
Practice 1: Union of Two Arrays
================================
Chapter 5: Collections

PROBLEM
-------
Given two lists of integers, return their sorted union — a sorted list
containing all unique elements that appear in either list.

INPUT FORMAT
------------
Two lines, each containing space-separated integers.

OUTPUT FORMAT
-------------
A single line of space-separated integers (the sorted union).

CONSTRAINTS
-----------
- Lists can be empty
- Lists may contain duplicates
- Elements can be negative

EXAMPLES
--------
Input:
1 2 3
3 4 5
Output: 1 2 3 4 5

Input:
1 1 2
2 3 3
Output: 1 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(a: list[int], b: list[int]) -> list[int]:
    """Return the sorted union of two lists (unique elements from both)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = solve(a, b)
    print(" ".join(map(str, result)))
