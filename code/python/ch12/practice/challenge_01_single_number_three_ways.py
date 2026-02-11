"""
Challenge 1: Single Number — Three Ways
=========================================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Given a non-empty array of integers where every element appears exactly
twice except for one, find that single element using THREE different
approaches: sorting, hashing, and XOR.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
Three lines, each showing the result from one approach:
  Sort: <answer>
  Hash: <answer>
  XOR:  <answer>

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^5
- -10^6 <= nums[i] <= 10^6
- Every element appears twice except one

EXAMPLES
--------
Input:
  4 1 2 1 2
Output:
  Sort: 4
  Hash: 4
  XOR:  4

Input:
  2 2 1
Output:
  Sort: 1
  Hash: 1
  XOR:  1

INSTRUCTIONS
------------
Replace the `pass` in solve_sort(), solve_hash(), and solve_xor() with your solutions.
The main block at the bottom handles input/output — don't change it.
"""


def solve_sort(nums: list[int]) -> int:
    """Find single number using sort + scan."""
    pass  # TODO: Replace this with your solution


def solve_hash(nums: list[int]) -> int:
    """Find single number using hash map."""
    pass  # TODO: Replace this with your solution


def solve_xor(nums: list[int]) -> int:
    """Find single number using XOR."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(f"Sort: {solve_sort(nums)}")
    print(f"Hash: {solve_hash(nums)}")
    print(f"XOR:  {solve_xor(nums)}")

