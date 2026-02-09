"""
Warmup 1: Unique Paths
======================
Chapter 24: Dynamic Programming II — Grids and Paths

PROBLEM
-------
Return the number of unique paths from top-left to bottom-right.

EXAMPLES
--------
  solve(3, 7) -> 28
  solve(1, 1) -> 1
  solve(3, 2) -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized bottom-up DP. Use 1D array of size n, fill left to right. dp[j] += dp[j-1] for each row. Initially all 1s.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(m: int, n: int) -> int:
    """Return the number of unique paths from top-left to bottom-right."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    m, n = map(int, input().strip().split())
    print(solve(m, n))
