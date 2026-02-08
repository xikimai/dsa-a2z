"""
Challenge 3: Repeating and Missing Number
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an array of n integers where the array should contain numbers
from 1 to n, but one number appears twice and one number is missing.
Find both the repeating and the missing number.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A list of two integers: [repeating_number, missing_number].

CONSTRAINTS
-----------
- 2 <= n <= 10^5
- 1 <= nums[i] <= n
- Exactly one number repeats, exactly one is missing

EXAMPLES
--------
Input:
  3 1 2 5 3
Output: [3, 4]

Input:
  1 1
Output: [1, 2]

Input:
  4 3 6 2 1 1
Output: [1, 5]

HINT
----
Use a hash set. Iterate through the array — if a number is already in
the set, it's the repeating number. Then check 1..n to find the number
not present in the set (the missing number).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[int]:
    """Return [repeating_number, missing_number]."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
