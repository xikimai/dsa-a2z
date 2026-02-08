"""
Solution for Practice 1: Single Number
========================================
Chapter 12: Bit Manipulation — The Language of Computers

APPROACH
--------
XOR all elements. Since a ^ a = 0 and a ^ 0 = a, pairs cancel
and only the single element remains.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return the element that appears only once."""
    result = 0
    for x in nums:
        result ^= x
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
