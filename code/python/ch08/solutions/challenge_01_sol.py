"""
Solution for Challenge 1: Sort Three Ways
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Three algorithms with different performance:
  1. Bubble sort:  O(n^2) — compare adjacent, swap, early termination
  2. Merge sort:   O(n log n) — divide, conquer, merge
  3. Built-in:     O(n log n) — Python's Timsort (hybrid merge+insertion)

TIME COMPLEXITY:  O(n^2) for bubble, O(n log n) for merge and built-in
SPACE COMPLEXITY: O(1) for bubble, O(n) for merge and built-in
"""


def solve_bubble(arr: list[int]) -> list[int]:
    """Sort using bubble sort with early termination."""
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


def solve_merge(arr: list[int]) -> list[int]:
    """Sort using merge sort."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = solve_merge(arr[:mid])
    right = solve_merge(arr[mid:])

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


def solve_builtin(arr: list[int]) -> list[int]:
    """Sort using Python's built-in sorted()."""
    return sorted(arr)


def solve(arr: list[int]) -> list[int]:
    """Default sort — uses merge sort."""
    return solve_merge(arr)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
