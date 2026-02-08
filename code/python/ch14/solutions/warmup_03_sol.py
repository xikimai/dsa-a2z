"""
Solution for Warmup 3: Running Sum of Array
=============================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Accumulate sum while iterating.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) — the output array
"""


def solve(arr: list[int]) -> list[int]:
    """Return the running sum array (same length as input)."""
    if not arr:
        return []
    result = [0] * len(arr)
    result[0] = arr[0]
    for i in range(1, len(arr)):
        result[i] = result[i - 1] + arr[i]
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
