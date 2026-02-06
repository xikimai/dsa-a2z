"""
Challenge 1: Two Sum Three Ways
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Given a list of integers and a target value, find two indices i and j
(i < j) such that nums[i] + nums[j] == target.

Return [i, j] if found, or [-1, -1] if no such pair exists.

Implement the solution THREE different ways to see how algorithmic
choices affect performance:

  solve_brute:  O(n^2) — check every pair with nested loops
  solve_sort:   O(n log n) — sort with original indices, two pointers
  solve_hash:   O(n) — hash map storing complement lookups

The default solve() function should call solve_hash.

INPUT FORMAT
------------
Line 1: space-separated integers (the array)
Line 2: a single integer (the target)

OUTPUT FORMAT
-------------
Two space-separated indices, or "-1 -1" if not found.

CONSTRAINTS
-----------
- 2 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9
- At most one valid answer exists (or none)

EXAMPLES
--------
Input:
  2 7 11 15
  9
Output: 0 1

Input:
  1 2 3
  10
Output: -1 -1

INSTRUCTIONS
------------
Replace the `pass` in each solve function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve_brute(nums: list[int], target: int) -> list[int]:
    """O(n^2) brute force: check every pair."""
    pass  # TODO: Replace this with your solution


def solve_sort(nums: list[int], target: int) -> list[int]:
    """O(n log n) sort-based: sort with indices, then two-pointer scan."""
    pass  # TODO: Replace this with your solution


def solve_hash(nums: list[int], target: int) -> list[int]:
    """O(n) hash map: store complements as you go."""
    pass  # TODO: Replace this with your solution


def solve(nums: list[int], target: int) -> list[int]:
    """Default solver — uses the hash approach."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input().strip())
    result = solve(nums, target)
    print(" ".join(map(str, result)))
