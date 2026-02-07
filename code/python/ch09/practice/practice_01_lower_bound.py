"""
Solution for Practice 1: Lower Bound
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Binary search with lo < hi loop. hi starts at len(arr) (not len-1)
because the answer could be "past the end" if all elements are smaller.
If arr[mid] < target, the answer is to the right (lo = mid + 1).
Otherwise, mid could be the answer (hi = mid).

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> int:
    """Return the first index where arr[i] >= target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
