"""
Solution for Warmup 2: Remove Duplicates from Sorted Array
============================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Use slow/fast pointers. Slow pointer marks where to write.
Fast pointer scans; when a new value is found, write it at slow.

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(1) — in-place (we return a slice)
"""


def solve(arr: list[int]) -> list[int]:
    """Return array with duplicates removed."""
    if len(arr) <= 1:
        return arr[:]

    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return arr[:slow + 1]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
