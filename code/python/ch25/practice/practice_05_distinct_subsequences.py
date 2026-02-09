"""
Practice 5: Distinct Subsequences
=================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the count of distinct subsequences of s that equal t.

EXAMPLES
--------
  solve("rabbbit", "rabbit") -> 3
  solve("babgbag", "bag") -> 5
  solve("aaa", "a") -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized 1D DP. dp[j] = number of ways to form t[:j] from s[:i].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str, t: str) -> int:
    """Return the count of distinct subsequences of s that equal t."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(solve(s, t))
