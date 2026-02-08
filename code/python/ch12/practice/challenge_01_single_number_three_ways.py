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
    pass  # TODO: Replace this with your solution


def solve_hash(nums: list[int]) -> int:
    """Find single number using hash map."""
    pass  # TODO: Replace this with your solution


def solve_xor(nums: list[int]) -> int:
    """Find single number using XOR."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(f"Sort: {solve_sort(nums)}")
    print(f"Hash: {solve_hash(nums)}")
    print(f"XOR:  {solve_xor(nums)}")

