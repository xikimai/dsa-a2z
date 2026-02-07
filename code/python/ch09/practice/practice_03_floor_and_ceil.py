"""
Solution for Practice 3: Floor and Ceil
============================================
Chapter 9: Finding Needles — The Power of Searching

APPROACH
--------
Use lower_bound internally to find the first index where arr[i] >= target.
- Ceil: if lb < n, then arr[lb] is the ceil (first element >= target).
  Otherwise, no ceil exists (-1).
- Floor: if lb < n and arr[lb] == target, floor = target. Otherwise,
  if lb > 0, floor = arr[lb - 1] (the element just before lower bound).
  If lb == 0, no floor exists (-1).

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def _lower_bound(arr: list[int], target: int) -> int:
    """Return first index where arr[i] >= target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def solve(arr: list[int], target: int) -> list[int]:
    """Return [floor, ceil] for target in sorted array."""
    n = len(arr)
    lb = _lower_bound(arr, target)

    # Ceil: first element >= target
    if lb < n:
        ceil_val = arr[lb]
    else:
        ceil_val = -1

    # Floor: largest element <= target
    if lb < n and arr[lb] == target:
        floor_val = target
    elif lb > 0:
        floor_val = arr[lb - 1]
    else:
        floor_val = -1

    return [floor_val, ceil_val]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    result = solve(data, target)
    print(result[0], result[1])
