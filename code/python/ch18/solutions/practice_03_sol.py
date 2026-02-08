"""
Solution for Practice 3: Merge Intervals
==========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Sort by start time. Scan and merge overlapping intervals.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n) for result
"""


def solve(intervals: list[list[int]]) -> list[list[int]]:
    """Return merged intervals."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    intervals = []
    for _ in range(n):
        s, e = map(int, input().strip().split())
        intervals.append([s, e])
    result = solve(intervals)
    for s, e in result:
        print(s, e)
