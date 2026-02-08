"""
Solution for Challenge 5: Longest Increasing Subsequence
===========================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
O(n^2) DP. dp[i] = length of LIS ending at index i.
For each i, check all j < i where nums[j] < nums[i].

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(n)
"""


def solve(nums: list[int]) -> int:
    """Return the length of the longest increasing subsequence."""
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n  # each element is an LIS of length 1 by itself
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
