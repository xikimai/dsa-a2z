"""
Warmup 4: Remove Duplicates from Sorted List
=============================================
Chapter 5: Collections

PROBLEM
-------
Given a SORTED list of integers, remove duplicates and return the
deduplicated list. The relative order should be preserved.

INPUT FORMAT
------------
A single line of space-separated sorted integers.

OUTPUT FORMAT
-------------
The deduplicated list as space-separated integers.

CONSTRAINTS
-----------
- The input list is sorted in non-decreasing order
- The list can be empty or have one element
- Elements can be negative

EXAMPLES
--------
Input:  1 1 2
Output: 1 2

Input:  1 1 1 2 2 3
Output: 1 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Remove duplicates from a sorted list and return the result."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    result = solve(nums)
    print(" ".join(map(str, result)))
