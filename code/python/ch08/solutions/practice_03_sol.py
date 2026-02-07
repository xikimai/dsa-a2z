"""
Solution for Practice 3: Dutch National Flag
============================================
Chapter 8: The Art of Sorting — Putting Things in Order

APPROACH
--------
Three-pointer technique (Dijkstra's Dutch National Flag):
  - lo: boundary for 0s (everything before lo is 0)
  - mid: current element being examined
  - hi: boundary for 2s (everything after hi is 2)

Walk mid through the array:
  - If arr[mid] == 0: swap with lo, advance both lo and mid
  - If arr[mid] == 1: just advance mid
  - If arr[mid] == 2: swap with hi, shrink hi (don't advance mid —
    the swapped element needs to be examined)

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(1) — in-place
"""


def solve(arr: list[int]) -> list[int]:
    """Sort array of 0s, 1s, 2s in single pass, O(n) time, O(1) extra space."""
    arr = arr[:]
    lo, mid, hi = 0, 0, len(arr) - 1
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
