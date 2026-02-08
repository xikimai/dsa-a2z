"""
Solution for Warmup 5: Maximum Subarray
==========================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Kadane's algorithm. current = max(current + nums[i], nums[i]).
Track the global best.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return the maximum contiguous subarray sum."""
    current = nums[0]
    best = nums[0]
    for i in range(1, len(nums)):
        current = max(current + nums[i], nums[i])
        best = max(best, current)
    return best


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
