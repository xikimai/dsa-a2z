"""
Solution for Challenge 2: Count Inversions
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Modified merge sort: during the merge step, whenever we pick an element
from the right half (because it's smaller than the current left element),
ALL remaining elements in the left half form inversions with it. So we
add (len(left) - i) to the inversion count.

This gives us O(n log n) instead of the brute-force O(n^2).

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int]) -> int:
    """Count the number of inversions using modified merge sort."""
    if len(arr) <= 1:
        return 0

    _, count = _merge_count(arr)
    return count


def _merge_count(arr):
    if len(arr) <= 1:
        return arr[:], 0

    mid = len(arr) // 2
    left, left_inv = _merge_count(arr[:mid])
    right, right_inv = _merge_count(arr[mid:])

    merged = []
    inversions = left_inv + right_inv
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
