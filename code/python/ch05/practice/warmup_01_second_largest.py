"""
Warmup 1: Second Largest
==============================
Chapter 5: Collections

PROBLEM
-------
Find the second largest element in a list of integers.
Return -1 if there is no second largest (all elements are the same
or the list has fewer than 2 elements).

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer: the second largest element, or -1.

CONSTRAINTS
-----------
- The list can be empty or have one element
- Elements can be negative
- Duplicate values are possible

EXAMPLES
--------
Input:  3 1 4 1 5
Output: 4

Input:  7 7 7
Output: -1

Input:  10
Output: -1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> int:
    """Return the second largest element, or -1 if none exists."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
