"""
Solution for Warmup 3: Search in Rotated Sorted Array
======================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Modified binary search. At each step, determine which half is sorted,
then check if target lies in the sorted half.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> int:
    """Return index of target in rotated sorted array, or -1."""
    if not arr:
        return -1
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        # Left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))
