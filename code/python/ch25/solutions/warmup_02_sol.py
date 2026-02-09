"""
Solution for Warmup 2: Subset Sum
====================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
1D boolean DP. dp[s] = True if sum s is achievable.
Iterate backwards to avoid using same element twice.

TIME COMPLEXITY:  O(n * target)
SPACE COMPLEXITY: O(target)
"""


def solve(nums: list[int], target: int) -> bool:
    """Return True if a subset of nums sums to target."""
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
    return dp[target]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    print(solve(nums, target))
