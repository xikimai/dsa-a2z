"""
Solution for Warmup 3: Search in Rotated Sorted Array
======================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Modified binary search. At each step, determine which half is sorted,
then check if target lies in the sorted half.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(arr: list[int], target: int) -> int:
    """Return index of target in rotated sorted array, or -1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))
