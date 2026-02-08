"""
Solution for Practice 5: Dutch National Flag
==============================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

APPROACH
--------
Three-pointer partition: low, mid, high.
  - arr[mid]==0 → swap with low, advance both
  - arr[mid]==1 → advance mid
  - arr[mid]==2 → swap with high, decrement high (don't advance mid)

TIME COMPLEXITY:  O(n) — single pass
SPACE COMPLEXITY: O(1) — in-place swaps
"""


def solve(arr: list[int]) -> list[int]:
    """Sort array of 0s, 1s, 2s in one pass."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

