"""
Challenge 3: Minimum Platforms
================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
Given arrival and departure times of trains, find the minimum
number of platforms needed so no train waits.

EXAMPLES
--------
>>> solve([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])
3

CONSTRAINTS
-----------
- 0 <= n <= 10^5
- 0 <= arrival <= departure
"""


def solve(arrivals: list[int], departures: list[int]) -> int:
    """Return minimum platforms needed."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arrivals = list(map(int, input().strip().split()))
    departures = list(map(int, input().strip().split()))
    print(solve(arrivals, departures))
