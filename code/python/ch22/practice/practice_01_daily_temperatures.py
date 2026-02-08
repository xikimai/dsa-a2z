"""
Practice 1: Daily Temperatures
==================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given a list of daily temperatures, return a list where result[i] is the number
of days you have to wait after day i to get a warmer temperature. If there is
no future warmer day, put 0.

CONSTRAINTS
-----------
- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100

EXAMPLES
--------
Input: 73 74 75 71 69 72 76 73
Output: [1, 1, 4, 2, 1, 1, 0, 0]

HINT
----
Use a monotonic stack of indices, processing left to right.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(temperatures: list[int]) -> list[int]:
    """Return list of days until a warmer temperature."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    temps = list(map(int, input().strip().split()))
    print(solve(temps))
