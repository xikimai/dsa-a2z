"""
Warmup 3: Min Cost Climbing Stairs
==================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Given an integer array `cost` where cost[i] is the cost of the ith step,
you can start from step 0 or step 1. Return the minimum cost to reach
the top (one step past the last index). Each step you can climb 1 or 2 steps.

EXAMPLES
--------
  cost=[10,15,20] -> 15
  cost=[1,100,1,1,1,100,1,1,100,1] -> 6

CONSTRAINTS
-----------
- 2 <= len(cost) <= 1000
- 0 <= cost[i] <= 999

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(cost: list[int]) -> int:
    """Return minimum cost to reach the top of the staircase."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    cost = list(map(int, input().split()))
    print(solve(cost))
