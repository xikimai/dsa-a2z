"""
Challenge 2: Gas Station
==========================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
There are n gas stations in a circle. gas[i] = fuel at station i,
cost[i] = fuel needed to reach station i+1. Find the starting
station index for a complete circuit, or -1 if impossible.

EXAMPLES
--------
>>> solve([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
3
>>> solve([2, 3, 4], [3, 4, 3])
-1

CONSTRAINTS
-----------
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
"""


def solve(gas: list[int], cost: list[int]) -> int:
    """Return starting station index, or -1 if impossible."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    gas = list(map(int, input().strip().split()))
    cost = list(map(int, input().strip().split()))
    print(solve(gas, cost))
