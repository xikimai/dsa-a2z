"""
Solution for Challenge 4: Subset Sum
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Use a recursive helper with index and remaining target.
Base case 1: remaining == 0, we found a valid subset.
Base case 2: index past end or remaining < 0, no solution here.
Recursive case: include nums[index] (subtract from remaining) OR
exclude it (keep remaining the same).

TIME COMPLEXITY:  O(2^n) — try include/exclude for each element
SPACE COMPLEXITY: O(n) — recursion stack depth
"""


def solve(nums: list[int], target: int) -> bool:
    """Return True if any subset of nums sums to target."""
    def helper(idx, remaining):
        if remaining == 0:
            return True
        if idx == len(nums) or remaining < 0:
            return False
        # Include nums[idx] or exclude it
        return helper(idx + 1, remaining - nums[idx]) or helper(idx + 1, remaining)

    return helper(0, target)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split())) if input().strip() else []
    target = int(input())
    print(solve(data, target))
