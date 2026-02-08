"""
Solution for Practice 4: Non-overlapping Intervals
====================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Sort by end time. Count max non-overlapping (activity selection).
Answer = total - max_non_overlapping.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(1) extra
"""


def solve(intervals: list[list[int]]) -> int:
    """Return minimum number of intervals to remove."""
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    keep = 0
    last_end = float('-inf')
    for start, end in intervals:
        if start >= last_end:
            keep += 1
            last_end = end
    return len(intervals) - keep


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    intervals = []
    for _ in range(n):
        s, e = map(int, input().strip().split())
        intervals.append([s, e])
    print(solve(intervals))
