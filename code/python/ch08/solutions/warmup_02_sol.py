"""
Solution for Warmup 2: Bubble Sort
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Compare adjacent elements and swap if out of order. After each pass, the
largest unsorted element "bubbles" to its correct position. If no swaps
happen during a pass, the array is sorted — stop early.

TIME COMPLEXITY:  O(n^2) worst case, O(n) best case (already sorted)
SPACE COMPLEXITY: O(1) — in-place
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using bubble sort with early termination."""
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
