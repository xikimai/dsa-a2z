"""
Solution for Warmup 1: Square Root (Integer)
=============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on answer space [0, n]. For each mid, check mid*mid <= n.
Find the maximum mid where mid*mid <= n.

TIME COMPLEXITY:  O(log n)
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return floor of square root of n."""
    if n < 0:
        return -1
    if n == 0:
        return 0
    lo, hi = 1, n
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2  # round up for "find maximum"
        if mid <= n // mid:  # avoid overflow: mid*mid <= n ↔ mid <= n/mid
            lo = mid
        else:
            hi = mid - 1
    return lo


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
