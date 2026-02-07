"""
Solution for Warmup 4: Last Occurrence
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Modified binary search. When we find the target, save the index and
continue searching RIGHT (lo = mid + 1) to find later occurrences.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> int:
    """Return the index of the last occurrence of target, or -1."""
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1  # keep searching right
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
