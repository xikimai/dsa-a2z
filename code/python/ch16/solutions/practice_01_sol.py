"""
Solution for Practice 1: Koko Eating Bananas
=============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on answer space [1, max(piles)]. For each candidate speed k,
check if Koko can finish all piles within h hours.

TIME COMPLEXITY:  O(n * log(max(piles)))
SPACE COMPLEXITY: O(1)
"""

import math


def solve(piles: list[int], h: int) -> int:
    """Return minimum eating speed to finish all piles in h hours."""
    def feasible(k):
        hours = sum(math.ceil(p / k) for p in piles)
        return hours <= h

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    piles = list(map(int, line.split()))
    h = int(input().strip())
    print(solve(piles, h))
