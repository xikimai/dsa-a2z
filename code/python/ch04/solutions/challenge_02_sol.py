"""
Solution for Challenge 2: Apply Operations
============================================
Chapter 4: Functions

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Define a helper function for each operation (double, negate, sort, reverse).
Use a dictionary to map operation names to functions. Loop through the
operations list and apply each one in order. Unknown operations are ignored.

TIME COMPLEXITY:  O(k * n) where k = number of operations, n = len(nums)
                  (sort is O(n log n) but we treat it as the dominant term)
SPACE COMPLEXITY: O(1) — all operations are in-place
"""


def op_double(nums: list[int]) -> list[int]:
    """Multiply every element by 2 (in place) and return the list."""
    for i in range(len(nums)):
        nums[i] *= 2
    return nums


def op_negate(nums: list[int]) -> list[int]:
    """Flip the sign of every element (in place) and return the list."""
    for i in range(len(nums)):
        nums[i] = -nums[i]
    return nums


def op_sort(nums: list[int]) -> list[int]:
    """Sort the list in ascending order (in place) and return it."""
    nums.sort()
    return nums


def op_reverse(nums: list[int]) -> list[int]:
    """Reverse the list (in place) and return it."""
    nums.reverse()
    return nums


def solve(nums: list[int], operations: list[str]) -> list[int]:
    """Apply each operation in order and return the final list."""
    dispatch = {
        "double": op_double,
        "negate": op_negate,
        "sort": op_sort,
        "reverse": op_reverse,
    }
    for op_name in operations:
        if op_name in dispatch:
            dispatch[op_name](nums)
    return nums


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    if line1:
        nums = list(map(int, line1.split()))
    else:
        nums = []
    line2 = input().strip()
    if line2:
        operations = line2.split()
    else:
        operations = []
    result = solve(nums, operations)
    print(" ".join(map(str, result)))
