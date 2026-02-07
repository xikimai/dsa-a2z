"""
Solution for Warmup 1: Linear Search
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Scan through the array from left to right. Return the index of the
first element that matches the target. If we reach the end without
finding it, return -1.

TIME COMPLEXITY:  O(n) — we may check every element
SPACE COMPLEXITY: O(1) — only a loop variable
"""


def solve(arr: list[int], target: int) -> int:
    """Return the index of the first occurrence of target, or -1."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
