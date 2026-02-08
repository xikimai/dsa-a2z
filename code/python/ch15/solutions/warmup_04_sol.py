"""
Solution for Warmup 4: Move Zeros to End
==========================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Use a slow pointer for the write position. Fast pointer scans.
When a non-zero is found, swap it with slow and advance slow.

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(1) — in-place swaps
"""


def solve(arr: list[int]) -> list[int]:
    """Return array with zeros moved to end."""
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return arr


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
