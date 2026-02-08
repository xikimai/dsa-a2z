"""
Challenge 1: Largest Rectangle in Histogram
===============================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given an array of integers representing bar heights in a histogram
(each bar has width 1), find the area of the largest rectangle that
can be formed within the histogram.

CONSTRAINTS
-----------
- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

EXAMPLES
--------
Input: 2 1 5 6 2 3
Output: 10   (rectangle of height 5, width 2 at indices 2-3)

Input: 2 4
Output: 4

HINT
----
Use a monotonic stack (increasing). When a shorter bar arrives, pop
and compute area. A sentinel of 0 at the end flushes remaining bars.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(heights: list[int]) -> int:
    """Return the area of the largest rectangle in the histogram."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    heights = list(map(int, input().strip().split()))
    print(solve(heights))
