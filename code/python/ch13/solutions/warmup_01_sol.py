"""
Solution for Warmup 1: Generate All Permutations
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Backtracking: for each position, try each unused element.
Sort nums first to ensure lexicographic order.

TIME COMPLEXITY:  O(n! * n) — n! permutations, each takes O(n) to copy
SPACE COMPLEXITY: O(n) — recursion depth + used array
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return all permutations of nums, sorted lexicographically."""
    nums.sort()
    results = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            results.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    for perm in result:
        print(perm)
