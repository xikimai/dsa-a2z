"""
Warmup 2: Jump Game I
======================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given an array of non-negative integers, you start at index 0.
Each element is your maximum jump length from that position.
Can you reach the last index?

EXAMPLES
--------
>>> solve([2, 3, 1, 1, 4])
True
>>> solve([3, 2, 1, 0, 4])
False

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^4
- 0 <= nums[i] <= 10^5
"""


def solve(nums: list[int]) -> bool:
    """Return True if you can reach the last index."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
