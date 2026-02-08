"""
Warmup 1: Climbing Stairs
=========================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
You are climbing a staircase with n steps. Each time you can
climb 1 or 2 steps. Return the number of distinct ways to reach the top.

EXAMPLES
--------
  n=1 -> 1
  n=2 -> 2
  n=3 -> 3
  n=5 -> 8

CONSTRAINTS
-----------
- 1 <= n <= 45

HINT
----
dp[n] = dp[n-1] + dp[n-2]. Base cases: dp[1]=1, dp[2]=2.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int) -> int:
    """Return the number of distinct ways to climb n stairs."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
