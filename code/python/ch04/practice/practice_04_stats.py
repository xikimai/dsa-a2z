"""
Practice 4: Statistics
==============================
Chapter 4: Functions

PROBLEM
-------
Given a list of integers, return [min, max, average] as a list of floats.
You must define find_min(nums), find_max(nums), and find_average(nums)
helper functions. Do NOT use Python's built-in min(), max(), or sum().
Round the average to 2 decimal places.

INPUT FORMAT
------------
A line of space-separated integers.

OUTPUT FORMAT
-------------
Three floats on one line: min, max, average (space-separated).

CONSTRAINTS
-----------
- The list is non-empty
- Elements can be negative

EXAMPLES
--------
Input:  3 1 4 1 5 9
Output: 1.0 9.0 3.83

Input:  7
Output: 7.0 7.0 7.0

Input:  -5 -2 -8
Output: -8.0 -2.0 -5.0

INSTRUCTIONS
------------
Replace the `pass` in each helper function and solve() with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def find_min(nums: list[int]) -> int:
    """Return the minimum value in nums (no built-in min)."""
    pass  # TODO: Replace this with your solution


def find_max(nums: list[int]) -> int:
    """Return the maximum value in nums (no built-in max)."""
    pass  # TODO: Replace this with your solution


def find_average(nums: list[int]) -> float:
    """Return the average of nums rounded to 2 decimal places (no built-in sum)."""
    pass  # TODO: Replace this with your solution


def solve(nums: list[int]) -> list[float]:
    """Return [min, max, average] as floats."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    print(" ".join(str(x) for x in result))
