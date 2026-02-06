"""
Solution for Practice 3: Two Sum
==================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use a hash map (dictionary) to store each number and its index as we
iterate. For each number, compute the complement (target - num). If the
complement is already in the map, we found our pair. Otherwise, store
the current number and index for future lookups.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for the hash map
"""


def solve(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers that sum to target, or [-1, -1]."""
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return [-1, -1]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    result = solve(nums, target)
    print(" ".join(map(str, result)))
