"""
Solution for Warmup 6: Move Zeros
============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use a write pointer that tracks where the next non-zero element should go.
Scan through the list: whenever we find a non-zero, place it at the write
pointer and advance. After the scan, fill all remaining positions with 0.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1) — done in place
"""


def solve(nums: list[int]) -> list[int]:
    """Move all zeros to the end in place and return the list."""
    write = 0

    # Move all non-zero elements to the front
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    # Fill the rest with zeros
    while write < len(nums):
        nums[write] = 0
        write += 1

    return nums


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    nums = list(map(int, line.split())) if line else []
    result = solve(nums)
    print(" ".join(map(str, result)))
