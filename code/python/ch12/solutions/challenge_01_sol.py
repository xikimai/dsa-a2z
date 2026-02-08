"""
Solution for Challenge 1: Single Number — Three Ways
======================================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH 1 (sort): Sort array, scan pairs. O(n log n) time, O(1) space.
APPROACH 2 (hash): Frequency map, find count==1. O(n) time, O(n) space.
APPROACH 3 (xor): XOR all. Pairs cancel. O(n) time, O(1) space.
"""


def solve_sort(nums: list[int]) -> int:
    """Find single number using sort + scan."""
    nums_sorted = sorted(nums)
    i = 0
    while i < len(nums_sorted) - 1:
        if nums_sorted[i] == nums_sorted[i + 1]:
            i += 2
        else:
            return nums_sorted[i]
    return nums_sorted[-1]


def solve_hash(nums: list[int]) -> int:
    """Find single number using hash map."""
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    for key, count in freq.items():
        if count == 1:
            return key
    return -1  # unreachable


def solve_xor(nums: list[int]) -> int:
    """Find single number using XOR."""
    result = 0
    for x in nums:
        result ^= x
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(f"Sort: {solve_sort(nums)}")
    print(f"Hash: {solve_hash(nums)}")
    print(f"XOR:  {solve_xor(nums)}")
