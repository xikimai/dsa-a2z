"""
Solution for Warmup 4: Remove Duplicates from Sorted List
===========================================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Two-pointer technique on a sorted list. Use a "write" pointer that tracks
where the next unique element should go. The "read" pointer scans forward.
When a new value is found (different from the value at the write pointer),
advance the write pointer and copy the value there.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1) — done in place (we return a slice at the end)
"""


def solve(nums: list[int]) -> list[int]:
    """Remove duplicates from a sorted list and return the result."""
    if len(nums) <= 1:
        return nums

    write = 0
    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]

    return nums[: write + 1]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    result = solve(nums)
    print(" ".join(map(str, result)))
