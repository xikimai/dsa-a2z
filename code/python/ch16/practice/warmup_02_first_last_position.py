"""
Solution for Warmup 2: First and Last Position
================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Two binary searches: one for the leftmost occurrence, one for the rightmost.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> list[int]:
    """Return [first, last] indices of target in sorted array, or [-1, -1]."""
    pass  # TODO: Replace this with your solution

    # Find first occurrence
    lo, hi = 0, len(arr) - 1
    first = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            first = mid
            hi = mid - 1  # keep searching left
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    if first == -1:
        return [-1, -1]

    # Find last occurrence
    lo, hi = first, len(arr) - 1
    last = first
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            last = mid
            lo = mid + 1  # keep searching right
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return [first, last]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))
