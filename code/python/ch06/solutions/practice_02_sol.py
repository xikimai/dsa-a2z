"""
Solution for Practice 2: Max Subarray Sum (Brute Force)
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
For each starting index i, walk forward through the array summing
elements.  Track the maximum sum seen across all subarrays.

This is intentionally O(n^2) — the chapter later shows how Kadane's
algorithm solves it in O(n).

TIME COMPLEXITY:  O(n^2)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return the maximum contiguous subarray sum using O(n^2) brute force."""
    if not nums:
        return 0

    n = len(nums)
    max_sum = nums[0]

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    print(solve(nums))
