"""
Solution for Challenge 1: Find Peak Element
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Linear (O(n)): Scan each element, check if it's greater than both neighbors
(treating out-of-bounds as -infinity).

Binary (O(log n)): If arr[mid] < arr[mid+1], there must be a peak to the
right (values go up, so they either reach the end or drop — either way,
a peak exists). Otherwise, a peak exists at mid or to the left.

TIME COMPLEXITY:  O(log n) for solve_binary, O(n) for solve_linear
SPACE COMPLEXITY: O(1)
"""


def solve_linear(arr: list[int]) -> int:
    """Find a peak element using linear scan. O(n)."""
    n = len(arr)
    for i in range(n):
        left_ok = (i == 0) or (arr[i] > arr[i - 1])
        right_ok = (i == n - 1) or (arr[i] > arr[i + 1])
        if left_ok and right_ok:
            return i
    return 0  # should never reach here if input is valid


def solve_binary(arr: list[int]) -> int:
    """Find a peak element using binary search. O(log n)."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def solve(arr: list[int]) -> int:
    """Find a peak element (calls solve_binary)."""
    return solve_binary(arr)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
