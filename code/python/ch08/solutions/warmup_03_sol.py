"""
Solution for Warmup 3: Insertion Sort
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Build the sorted portion one element at a time. For each element, shift
all larger elements to the right, then insert the current element into
its correct position.

TIME COMPLEXITY:  O(n^2) worst case, O(n) best case (already sorted)
SPACE COMPLEXITY: O(1) — in-place
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using insertion sort."""
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
