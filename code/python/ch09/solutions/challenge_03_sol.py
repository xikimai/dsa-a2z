"""
Solution for Challenge 3: Search in Rotated Sorted Array II
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Same idea as searching in a rotated sorted array without duplicates,
but with one extra case: when arr[lo] == arr[mid] == arr[hi], we can't
determine which half is sorted. In that case, shrink both ends
(lo++, hi--) and try again. This makes worst case O(n), but average
case is still O(log n).

TIME COMPLEXITY:  O(log n) average, O(n) worst case
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> bool:
    """Search for target in a rotated sorted array with duplicates."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return True

        # Can't determine which half is sorted
        if arr[lo] == arr[mid] == arr[hi]:
            lo += 1
            hi -= 1
        # Left half is sorted
        elif arr[lo] <= arr[mid]:
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
    return False


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
