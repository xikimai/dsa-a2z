"""
Solution for Warmup 4: House Robber
======================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Space-optimized to two variables.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return maximum money you can rob without robbing adjacent houses."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    return prev1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
