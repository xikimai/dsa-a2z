"""
Solution for Challenge 3: Target Sum
=======================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Reduce to subset sum count. P + N = total, P - N = target.
So P = (total + target) / 2. Count subsets summing to P.

TIME COMPLEXITY:  O(n * P)
SPACE COMPLEXITY: O(P)
"""


def solve(nums: list[int], target: int) -> int:
    """Return the number of ways to assign +/- to reach target."""
    total = sum(nums)
    if (total + target) % 2 != 0 or total + target < 0:
        return 0
    p = (total + target) // 2
    if p < 0:
        return 0
    dp = [0] * (p + 1)
    dp[0] = 1
    for num in nums:
        for s in range(p, num - 1, -1):
            dp[s] += dp[s - num]
    return dp[p]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    print(solve(nums, target))
