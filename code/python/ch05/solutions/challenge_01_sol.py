"""
Solution for Challenge 1: Find All Duplicates
===============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Three progressively optimized versions:

solve_brute — O(n^2): For each element, scan the rest of the list to
  check if it appears again. Use a set to avoid adding the same
  duplicate twice.

solve_sort — O(n log n): Sort the list first, then scan for adjacent
  equal elements.

solve_set — O(n): Use a "seen" set. For each element, if it is already
  in "seen", it is a duplicate. Otherwise, add it to "seen".

TIME COMPLEXITY:  O(n) for solve_set
SPACE COMPLEXITY: O(n) for the seen set and duplicates set
"""


def solve_brute(nums: list[int]) -> list[int]:
    """Find duplicates using O(n^2) brute force."""
    duplicates = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                duplicates.add(nums[i])
    return sorted(duplicates)


def solve_sort(nums: list[int]) -> list[int]:
    """Find duplicates using sorting."""
    if len(nums) <= 1:
        return []
    sorted_nums = sorted(nums)
    duplicates = set()
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            duplicates.add(sorted_nums[i])
    return sorted(duplicates)


def solve_set(nums: list[int]) -> list[int]:
    """Find duplicates using a hash set."""
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return sorted(duplicates)


def solve(nums: list[int]) -> list[int]:
    """Return sorted list of duplicate elements (uses solve_set)."""
    return solve_set(nums)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    result = solve(nums)
    print(" ".join(map(str, result)))
