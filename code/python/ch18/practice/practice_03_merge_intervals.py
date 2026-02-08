"""
Practice 3: Merge Intervals
==============================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given a collection of intervals, merge all overlapping intervals.

EXAMPLES
--------
>>> solve([[1, 3], [2, 6], [8, 10], [15, 18]])
[[1, 6], [8, 10], [15, 18]]
>>> solve([[1, 4], [4, 5]])
[[1, 5]]

CONSTRAINTS
-----------
- 0 <= n <= 10^4
- 0 <= start <= end <= 10^9
"""


def solve(intervals: list[list[int]]) -> list[list[int]]:
    """Return merged intervals."""
    pass  # TODO: Replace this with your solution


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
