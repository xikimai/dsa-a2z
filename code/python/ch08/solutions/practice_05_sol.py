"""
Solution for Practice 5: Merge Two Sorted Arrays
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Two-pointer merge: maintain one pointer for each array. Compare the
elements at the front of each array and append the smaller one to the
result. When one array is exhausted, append the remainder of the other.

TIME COMPLEXITY:  O(n + m) where n, m are the lengths of the two arrays
SPACE COMPLEXITY: O(n + m) for the result
"""


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    """Merge two sorted arrays into one sorted array."""
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    line2 = input().strip()
    arr1 = list(map(int, line1.split())) if line1 else []
    arr2 = list(map(int, line2.split())) if line2 else []
    print(*solve(arr1, arr2))
