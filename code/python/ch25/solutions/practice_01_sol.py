"""
Solution for Practice 1: Partition Equal Subset Sum
=====================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Reduce to Subset Sum: if total is odd, impossible.
Otherwise find if a subset sums to total // 2.

TIME COMPLEXITY:  O(n * sum/2)
SPACE COMPLEXITY: O(sum/2)
"""


def solve(nums: list[int]) -> bool:
    """Return True if nums can be split into two equal-sum subsets."""
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
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
    print(solve(nums))
