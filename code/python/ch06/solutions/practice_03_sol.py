"""
Solution for Practice 3: Sorted Squares
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Two-pointer technique.  Place one pointer at the start (most negative)
and one at the end (most positive).  Compare absolute values — the
larger one produces the next-largest square.  Fill the result array
from the back (largest to smallest).

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for the result array
"""


def solve(nums: list[int]) -> list[int]:
    """Return sorted squares of a sorted input array using two pointers."""
    if not nums:
        return []

    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1  # fill from the back

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    print(" ".join(map(str, solve(nums))))
