"""
Solution for Practice 2: Ship Packages Within D Days
=====================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on answer space [max(weights), sum(weights)]. For each
candidate capacity, greedily load packages and count days needed.

TIME COMPLEXITY:  O(n * log(sum(weights)))
SPACE COMPLEXITY: O(1)
"""


def solve(weights: list[int], d: int) -> int:
    """Return minimum ship capacity to deliver all packages in d days."""
    def feasible(cap):
        days, load = 1, 0
        for w in weights:
            if load + w > cap:
                days += 1
                load = 0
            load += w
        return days <= d

    lo, hi = max(weights), sum(weights)
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
    weights = list(map(int, line.split()))
    d = int(input().strip())
    print(solve(weights, d))
