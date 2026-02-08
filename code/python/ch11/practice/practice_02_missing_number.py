"""
Practice 2: Missing Number
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an array containing n distinct numbers from the range [0, n],
find the one number that is missing from the array.

Use a hash set approach: add all numbers to a set, then check
each number from 0 to n.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the missing number.

CONSTRAINTS
-----------
- 1 <= n <= 10^4
- All numbers are distinct and in the range [0, n]

EXAMPLES
--------
Input:
  3 0 1
Output: 2

Input:
  0 1
Output: 2

Input:
  9 6 4 2 3 5 7 0 1
Output: 8

HINT
----
Add all numbers to a hash set. Then iterate from 0 to n and check
which number is not in the set.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> int:
    """Find the missing number in [0, n]."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
