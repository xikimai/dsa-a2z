"""
Solution for Warmup 2: Binary Search
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Classic binary search on a sorted array. Maintain lo and hi pointers.
Compare the middle element with the target:
- If equal, return the index.
- If arr[mid] < target, search the right half.
- If arr[mid] > target, search the left half.

TIME COMPLEXITY:  O(log n) — halve the search space each step
SPACE COMPLEXITY: O(1) — only a few variables
"""


def solve(arr: list[int], target: int) -> int:
    """Binary search for target in sorted array. Return index or -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
