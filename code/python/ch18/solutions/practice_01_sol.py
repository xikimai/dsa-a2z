"""
Solution for Practice 1: Activity Selection
=============================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Sort by end time. Greedily pick each activity that starts >= last end.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(1) extra
"""


def solve(activities: list[list[int]]) -> int:
    """Return the maximum number of non-overlapping activities."""
    if not activities:
        return 0
    activities.sort(key=lambda x: x[1])
    count = 0
    last_end = 0
    for start, end in activities:
        if start >= last_end:
            count += 1
            last_end = end
    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    activities = []
    for _ in range(n):
        s, e = map(int, input().strip().split())
        activities.append([s, e])
    print(solve(activities))
