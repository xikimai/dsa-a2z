"""
Solution for Practice 1: Subsets Using Bitmasks
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
For each mask from 0 to 2^n - 1, check each bit. If bit i is set,
include nums[i] in the subset.

TIME COMPLEXITY:  O(2^n * n)
SPACE COMPLEXITY: O(2^n * n) — storing all subsets
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Generate all subsets using bitmasks, sorted by length then lex."""
    nums.sort()
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    result.sort(key=lambda x: (len(x), x))
    return result


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
