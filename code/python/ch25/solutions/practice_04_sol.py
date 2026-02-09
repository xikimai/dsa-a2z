"""
Solution for Practice 4: Longest Increasing Subsequence
=========================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
O(n^2) DP. dp[i] = length of LIS ending at index i.
For each i, check all j < i where nums[j] < nums[i].

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n)
"""


def solve(nums: list[int]) -> int:
    """Return the length of the longest strictly increasing subsequence."""
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
