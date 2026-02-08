"""
Practice 5: Jump Game II
==========================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given an array where each element is your max jump length,
find the minimum number of jumps to reach the last index.
(Guaranteed reachable.)

EXAMPLES
--------
>>> solve([2, 3, 1, 1, 4])
2
>>> solve([2, 3, 0, 1, 4])
2

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^4
- 0 <= nums[i] <= 1000
"""


def solve(nums: list[int]) -> int:
    """Return minimum number of jumps to reach the last index."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
