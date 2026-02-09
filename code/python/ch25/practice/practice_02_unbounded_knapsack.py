"""
Practice 2: Unbounded Knapsack
==============================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the maximum value with unlimited item reuse.

EXAMPLES
--------
  solve([2, 4, 6], [5, 11, 13], 10) -> 27
  solve([1, 3, 4, 5], [10, 40, 50, 70], 8) -> 110
  solve([3], [7], 9) -> 21

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Like 0/1 Knapsack but iterate capacity FORWARDS (left to right) so each item can be reused multiple times.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(weights: list[int], values: list[int], capacity: int) -> int:
    """Return the maximum value with unlimited item reuse."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    weights = list(map(int, input().strip().split()))
    values = list(map(int, input().strip().split()))
    capacity = int(input().strip())
    print(solve(weights, values, capacity))
