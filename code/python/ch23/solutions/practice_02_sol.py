"""
Solution for Practice 2: House Robber II (Circular)
======================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Since first and last houses are adjacent, we can't rob both.
Run linear House Robber on [0..n-2] and [1..n-1]. Take the max.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return maximum money from circular houses without robbing adjacent."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    def rob_linear(arr):
        prev2 = arr[0]
        prev1 = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            current = max(prev1, prev2 + arr[i])
            prev2 = prev1
            prev1 = current
        return prev1

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
