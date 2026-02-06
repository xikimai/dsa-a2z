"""
Warmup 2: Reverse List
==============================
Chapter 5: Collections

PROBLEM
-------
Reverse a list of integers in place without using the built-in reverse()
method or slicing tricks. Return the reversed list.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
The reversed list as space-separated integers.

CONSTRAINTS
-----------
- The list can be empty or have one element
- Elements can be negative

EXAMPLES
--------
Input:  1 2 3 4 5
Output: 5 4 3 2 1

Input:  1
Output: 1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Reverse the list in place and return it."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    print(" ".join(map(str, result)))
