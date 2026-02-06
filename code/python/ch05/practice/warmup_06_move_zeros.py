"""
Warmup 6: Move Zeros
==============================
Chapter 5: Collections

PROBLEM
-------
Move all zeros in a list to the end while maintaining the relative
order of the non-zero elements. Do this in place.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
The modified list as space-separated integers.

CONSTRAINTS
-----------
- The list can be empty
- Elements can be negative (only 0 is moved)

EXAMPLES
--------
Input:  0 1 0 3 12
Output: 1 3 12 0 0

Input:  0 0 1
Output: 1 0 0

Input:  1 2 3
Output: 1 2 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Move all zeros to the end in place and return the list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    result = solve(nums)
    print(" ".join(map(str, result)))
