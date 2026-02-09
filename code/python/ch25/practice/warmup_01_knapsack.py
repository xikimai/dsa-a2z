"""
Warmup 1: 0/1 Knapsack
======================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the maximum value that fits in the knapsack.

EXAMPLES
--------
  solve([1, 3, 4, 5], [1, 4, 5, 7], 7) -> 9
  solve([2, 3, 4, 5], [3, 4, 5, 6], 5) -> 7
  solve([10], [10], 5) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized 1D DP. Process items, iterate capacity backwards. dp[w] = max value using capacity w.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(weights: list[int], values: list[int], capacity: int) -> int:
    """Return the maximum value that fits in the knapsack."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    weights = list(map(int, input().strip().split()))
    values = list(map(int, input().strip().split()))
    capacity = int(input().strip())
    print(solve(weights, values, capacity))
