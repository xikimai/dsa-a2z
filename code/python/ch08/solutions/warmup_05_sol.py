"""
Solution for Warmup 5: Sort by Absolute Value
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Use Python's sorted() with key=abs. Python's sort is stable, so elements
with the same absolute value keep their original relative order.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int]) -> list[int]:
    """Sort the array by absolute value (stable)."""
    return sorted(arr, key=abs)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
