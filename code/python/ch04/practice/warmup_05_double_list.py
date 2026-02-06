"""
Warmup 5: Double List
==============================
Chapter 4: Functions

PROBLEM
-------
Double every element in the list IN PLACE and return the same list.
This means you should modify the original list, not create a new one.

INPUT FORMAT
------------
A line of space-separated integers.

OUTPUT FORMAT
-------------
The same integers, each doubled, space-separated.

CONSTRAINTS
-----------
- List can be empty
- Elements can be negative or zero

EXAMPLES
--------
Input:  1 2 3
Output: 2 4 6

Input:  -1 0 5
Output: -2 0 10

Input:  (empty)
Output: (empty)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Double every element in nums in place and return the list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    result = solve(nums)
    print(" ".join(map(str, result)))
