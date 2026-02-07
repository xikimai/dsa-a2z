"""
Solution for Warmup 4: Check If Sorted
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Linear scan: check that arr[i] <= arr[i+1] for every consecutive pair.
If any pair violates this, the array is not sorted.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int]) -> bool:
    """Return True if the array is sorted in non-decreasing order."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    data = list(map(int, line.split())) if line else []
    print(solve(data))
