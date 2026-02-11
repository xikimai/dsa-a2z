"""
Challenge 1: Find Peak Element
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
A peak element is an element that is strictly greater than its neighbors.
Given an array of integers, find the index of ANY peak element. Assume
that arr[-1] = arr[n] = -infinity (elements outside the array are
negative infinity).

Implement THREE functions:
- solve_linear: find a peak using a simple linear scan (O(n)).
- solve_binary: find a peak using binary search (O(log n)).
- solve: a wrapper that calls solve_binary.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer: the index of a peak element.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- No two adjacent elements are equal.

EXAMPLES
--------
Input:
  1 2 3 1
Output: 2

Input:
  1 2 1 3 5 6 4
Output: 1 (or 5 — any valid peak index is accepted)

INSTRUCTIONS
------------
Replace the `pass` in each function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve_linear(arr: list[int]) -> int:
    """Find a peak element using linear scan. O(n)."""
    pass  # TODO: Replace this with your solution


def solve_binary(arr: list[int]) -> int:
    """Find a peak element using binary search. O(log n)."""
    pass  # TODO: Replace this with your solution


def solve(arr: list[int]) -> int:
    """Find a peak element (calls solve_binary)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
