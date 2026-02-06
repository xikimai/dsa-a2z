"""
Solution for Practice 1: Contains Duplicate
============================================
Chapter 6: How Fast Is Your Code?

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use a set to track seen values.  For each element, check if it's already
in the set.  If yes, we found a duplicate.  If not, add it and continue.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(nums: list[int]) -> bool:
    """Return True if any value appears at least twice."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    print(solve(nums))
