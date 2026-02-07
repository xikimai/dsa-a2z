"""
Solution for Warmup 1: Selection Sort
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Find the minimum element in the unsorted portion (from index i to end),
then swap it with the element at index i. Repeat for each position.

TIME COMPLEXITY:  O(n^2) — always, even on sorted input
SPACE COMPLEXITY: O(1) — in-place
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array using selection sort."""
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
