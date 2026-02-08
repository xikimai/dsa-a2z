"""
Solution for Warmup 2: Jump Game I
====================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Track the maximum reachable index. If current index > max_reach, stuck.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> bool:
    """Return True if you can reach the last index."""
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
