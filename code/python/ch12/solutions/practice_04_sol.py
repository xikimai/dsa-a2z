"""
Solution for Practice 4: Power Set Using Bitmasks
===================================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
Iterate mask from 0 to 2^n - 1. For each mask, include element i
if (mask >> i) & 1 == 1.

TIME COMPLEXITY:  O(n * 2^n) — 2^n subsets, each up to n elements
SPACE COMPLEXITY: O(n * 2^n) — for the result
"""


def solve(nums: list[int]) -> list[list[int]]:
    """Return all subsets using bitmask enumeration."""
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))
    else:
        nums = []
    result = solve(nums)
    for subset in result:
        print(subset)
