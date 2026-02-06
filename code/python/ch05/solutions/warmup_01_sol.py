"""
Solution for Warmup 1: Second Largest
============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Single pass: track the largest and second largest values seen so far.
Initialize both to negative infinity. As we iterate, update them
accordingly, being careful to only update second when we see a value
that is strictly less than the current largest.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return the second largest element, or -1 if none exists."""
    if len(nums) < 2:
        return -1

    first = second = float("-inf")

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float("-inf") else -1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
