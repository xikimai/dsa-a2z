"""
Practice 6: Wildcard Matching
=============================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return True if s matches pattern p with wildcards.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
2D DP. dp[i][j] = True if s[:i] matches p[:j]. Space-optimized to two rows.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str, p: str) -> bool:
    """Return True if s matches pattern p with wildcards."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    s = input().strip()
    p = input().strip()
    print(solve(s, p))
