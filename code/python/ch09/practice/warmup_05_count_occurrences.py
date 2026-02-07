"""
Solution for Warmup 5: Count Occurrences
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Find the first and last occurrence using binary search (same technique
as W3 and W4). The count is last - first + 1 (or 0 if not found).

TIME COMPLEXITY:  O(log n) — two binary searches
SPACE COMPLEXITY: O(1)
"""


def _first_occurrence(arr: list[int], target: int) -> int:
    """Find index of first occurrence, or -1."""
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def _last_occurrence(arr: list[int], target: int) -> int:
    """Find index of last occurrence, or -1."""
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def solve(arr: list[int], target: int) -> int:
    """Count occurrences of target in sorted array in O(log n)."""
    first = _first_occurrence(arr, target)
    if first == -1:
        return 0
    last = _last_occurrence(arr, target)
    return last - first + 1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
