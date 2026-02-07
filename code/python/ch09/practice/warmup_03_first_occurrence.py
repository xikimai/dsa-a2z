"""
Solution for Warmup 3: First Occurrence
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Modified binary search. When we find the target, we DON'T stop.
Instead, we save the index as a candidate answer and continue searching
LEFT (hi = mid - 1) to see if there's an earlier occurrence.

TIME COMPLEXITY:  O(log n) — always halves the search space
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> int:
    """Return the index of the first occurrence of target, or -1."""
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1  # keep searching left
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
