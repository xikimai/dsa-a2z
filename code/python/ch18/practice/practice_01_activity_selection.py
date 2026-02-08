"""
Practice 1: Activity Selection
================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given n activities with start and end times, find the maximum number
of non-overlapping activities one person can attend.

EXAMPLES
--------
>>> solve([[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]])
4
>>> solve([[1, 2], [3, 4], [5, 6]])
3

CONSTRAINTS
-----------
- 0 <= n <= 10^4
- 0 <= start < end <= 10^9
"""


def solve(activities: list[list[int]]) -> int:
    """Return the maximum number of non-overlapping activities."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    activities = []
    for _ in range(n):
        s, e = map(int, input().strip().split())
        activities.append([s, e])
    print(solve(activities))
