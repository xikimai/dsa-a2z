"""
Solution for Challenge 2: Single Element in Sorted Array
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
In a sorted array where every element appears twice except one, pairs
are aligned at even-odd indices BEFORE the single element, and at
odd-even indices AFTER it. Use binary search on this property:

- If mid is even and arr[mid] == arr[mid+1], the single element is to
  the right (pairs are still properly aligned).
- If mid is odd and arr[mid] == arr[mid-1], the single element is to
  the right (pairs are still properly aligned).
- Otherwise, the single element is at mid or to the left.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int]) -> int:
    """Find the element that appears exactly once."""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        # Ensure mid is even for consistent pair checking
        if mid % 2 == 1:
            mid -= 1
        if arr[mid] == arr[mid + 1]:
            # Pair is intact, single element is to the right
            lo = mid + 2
        else:
            # Pair is broken, single element is at mid or to the left
            hi = mid
    return arr[lo]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
