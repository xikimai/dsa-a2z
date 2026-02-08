"""
Solution for Warmup 2: Generate All Subsets
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Recursion: for each element, include or exclude.
Sort inputs and results for deterministic output.

TIME COMPLEXITY:  O(2^n * n)
SPACE COMPLEXITY: O(n) — recursion depth
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return all subsets sorted by length then lexicographically."""
    nums.sort()
    results = []

    def backtrack(index, current):
        if index == len(nums):
            results.append(current[:])
            return
        # Exclude nums[index]
        backtrack(index + 1, current)
        # Include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()

    backtrack(0, [])
    results.sort(key=lambda x: (len(x), x))
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    result = solve(nums)
    for s in result:
        print(s)
