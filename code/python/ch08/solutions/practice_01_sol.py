"""
Solution for Practice 1: Merge Sort
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Divide-and-conquer: split the array in half, recursively sort each half,
then merge the two sorted halves using a two-pointer technique.

TIME COMPLEXITY:  O(n log n) — always
SPACE COMPLEXITY: O(n) — for the temporary merge arrays
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using merge sort."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = solve(arr[:mid])
    right = solve(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
