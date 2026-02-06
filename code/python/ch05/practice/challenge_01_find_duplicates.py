"""
Challenge 1: Find All Duplicates
==================================
Chapter 5: Collections

PROBLEM
-------
Given a list of integers, find all elements that appear more than once.
Return them as a sorted list.

You must implement THREE approaches:
  - solve_brute(nums): O(n^2) nested loop approach
  - solve_sort(nums):  O(n log n) sort-based approach
  - solve_set(nums):   O(n) hash set approach

The solve() function should call solve_set.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
The sorted list of duplicate elements as space-separated integers.

CONSTRAINTS
-----------
- The list can be empty
- Elements are positive integers

EXAMPLES
--------
Input:  4 3 2 7 8 2 3 1
Output: 2 3

Input:  1 2 3
Output: (empty line)

Input:  1 1 1 1
Output: 1

INSTRUCTIONS
------------
Replace the `pass` in each function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve_brute(nums: list[int]) -> list[int]:
    """Find duplicates using O(n^2) brute force."""
    pass  # TODO: Replace this with your solution


def solve_sort(nums: list[int]) -> list[int]:
    """Find duplicates using sorting."""
    pass  # TODO: Replace this with your solution


def solve_set(nums: list[int]) -> list[int]:
    """Find duplicates using a hash set."""
    pass  # TODO: Replace this with your solution


def solve(nums: list[int]) -> list[int]:
    """Return sorted list of duplicate elements (uses solve_set)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    result = solve(nums)
    print(" ".join(map(str, result)))
