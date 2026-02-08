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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    for perm in result:
        print(perm)

