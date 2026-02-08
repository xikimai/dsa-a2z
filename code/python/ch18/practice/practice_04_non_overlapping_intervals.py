"""
Practice 4: Non-overlapping Intervals
========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given intervals, find the minimum number of intervals to remove
so the rest don't overlap.

EXAMPLES
--------
>>> solve([[1, 2], [2, 3], [3, 4], [1, 3]])
1
>>> solve([[1, 2], [1, 2], [1, 2]])
2

CONSTRAINTS
-----------
- 0 <= n <= 10^5
- -10^9 <= start < end <= 10^9
"""


def solve(intervals: list[list[int]]) -> int:
    """Return minimum number of intervals to remove."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    intervals = []
    for _ in range(n):
        s, e = map(int, input().strip().split())
        intervals.append([s, e])
    print(solve(intervals))
