"""
Practice 4: Sort by Frequency
==============================
Chapter 5: Collections

PROBLEM
-------
Sort a list of integers by frequency (most frequent first).
If two elements have the same frequency, the smaller element
comes first.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
The sorted list as space-separated integers.

CONSTRAINTS
-----------
- The list can have 1 to 10^4 elements
- Elements can be negative

EXAMPLES
--------
Input:  2 3 1 3 2
Output: 2 2 3 3 1

Input:  1 1 2 2 3
Output: 1 1 2 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Sort by frequency (descending), then by value (ascending)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    print(" ".join(map(str, result)))
