"""
Solution for Practice 2: Quick Sort
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Lomuto partition: choose the last element as pivot. Walk through the array
with pointer i tracking the boundary of "elements <= pivot". After
partitioning, place the pivot in its final position and recurse on both
sides.

TIME COMPLEXITY:  O(n log n) average, O(n^2) worst case
SPACE COMPLEXITY: O(log n) average recursion depth
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using quick sort with Lomuto partition."""
    arr = arr[:]
    _quicksort(arr, 0, len(arr) - 1)
    return arr


def _quicksort(arr, low, high):
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quicksort(arr, low, pivot_idx - 1)
        _quicksort(arr, pivot_idx + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
