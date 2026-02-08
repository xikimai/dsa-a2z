"""
Solution for Warmup 4: Peak Element in Array
=============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search: if mid element is less than its right neighbor,
a peak exists on the right half; otherwise on the left half (including mid).

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int]) -> int:
    """Return index of any peak element (greater than its neighbors)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
