"""
Solution for Challenge 4: Interval Scheduling
==============================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Classic greedy: sort intervals by end time. Greedily pick the interval
that ends earliest and does not overlap with the previously picked one.
Two intervals [a,b] and [c,d] do NOT overlap if b <= c (end <= start).

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""


def solve(intervals: list[list[int]]) -> int:
    """Return max number of non-overlapping intervals."""
    if not intervals:
        return 0
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    count = 1
    last_end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= last_end:
            count += 1
            last_end = intervals[i][1]
    return count


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    intervals = []
    for _ in range(n):
        s = int(tokens[idx]); idx += 1
        e = int(tokens[idx]); idx += 1
        intervals.append([s, e])
    print(solve(intervals))
