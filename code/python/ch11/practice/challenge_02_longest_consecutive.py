"""
Challenge 2: Longest Consecutive Sequence
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an unsorted array of integers, find the length of the longest
consecutive elements sequence. Your algorithm should run in O(n) time.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the length of the longest consecutive sequence.

CONSTRAINTS
-----------
- 0 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

EXAMPLES
--------
Input:
  100 4 200 1 3 2
Output: 4   (the sequence is 1, 2, 3, 4)

Input:
  0 3 7 2 5 8 4 6 0 1
Output: 9   (the sequence is 0, 1, 2, 3, 4, 5, 6, 7, 8)

Input:
  (empty)
Output: 0

HINT
----
Add all numbers to a hash set. For each number where (num - 1) is NOT
in the set (i.e., it's the start of a consecutive run), count how many
consecutive numbers follow. Track the maximum length.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> int:
    """Find length of longest consecutive sequence in O(n)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    print(solve(nums))
