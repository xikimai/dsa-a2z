"""
Solution for Practice 4: Sort by Frequency
============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
1. Count the frequency of each element using a dictionary.
2. Sort the list using a custom key: (-frequency, value).
   - Negate frequency so higher frequency comes first.
   - Use value as tiebreaker so smaller values come first.

TIME COMPLEXITY:  O(n log n) — dominated by sorting
SPACE COMPLEXITY: O(n) for the frequency map
"""


def solve(nums: list[int]) -> list[int]:
    """Sort by frequency (descending), then by value (ascending)."""
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return sorted(nums, key=lambda x: (-freq[x], x))


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = solve(nums)
    print(" ".join(map(str, result)))
