"""
Solution for Practice 5: Find Minimum in Rotated Sorted Array
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Binary search comparing arr[mid] with arr[hi].
- If arr[mid] > arr[hi], the minimum is in the right half (lo = mid + 1).
- Otherwise, the minimum is at mid or to the left (hi = mid).
When lo == hi, we've found the minimum.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int]) -> int:
    """Return the minimum value in a rotated sorted array."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
