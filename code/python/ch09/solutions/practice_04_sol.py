"""
Solution for Practice 4: Search in Rotated Sorted Array
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Modified binary search. At each step, at least one half of the array
is sorted. Determine which half is sorted, then check if the target
falls within that sorted range. If yes, search that half. If no,
search the other half.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> int:
    """Search for target in a rotated sorted array (no duplicates)."""
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
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
