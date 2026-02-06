"""
Solution for Challenge 1: Two Sum Three Ways
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Three approaches to the same problem, each with different time/space:

1. solve_brute — O(n^2) time, O(1) space
   Check every pair (i, j) with i < j.

2. solve_sort — O(n log n) time, O(n) space
   Create (value, original_index) pairs, sort by value, then use two
   pointers from both ends to find the target sum.

3. solve_hash — O(n) time, O(n) space
   For each element, check if (target - element) was seen before.
   Store index in a dictionary.

TIME COMPLEXITY:  O(n) for solve / solve_hash
SPACE COMPLEXITY: O(n) for solve / solve_hash
"""


def solve_brute(nums: list[int], target: int) -> list[int]:
    """O(n^2) brute force: check every pair."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]


def solve_sort(nums: list[int], target: int) -> list[int]:
    """O(n log n) sort-based: sort with indices, then two-pointer scan."""
    indexed = sorted(enumerate(nums), key=lambda x: x[1])
    left = 0
    right = len(indexed) - 1

    while left < right:
        current_sum = indexed[left][1] + indexed[right][1]
        if current_sum == target:
            i, j = indexed[left][0], indexed[right][0]
            return [min(i, j), max(i, j)]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def solve_hash(nums: list[int], target: int) -> list[int]:
    """O(n) hash map: store complements as you go."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return [-1, -1]


def solve(nums: list[int], target: int) -> list[int]:
    """Default solver — uses the hash approach."""
    return solve_hash(nums, target)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input().strip())
    result = solve(nums, target)
    print(" ".join(map(str, result)))
