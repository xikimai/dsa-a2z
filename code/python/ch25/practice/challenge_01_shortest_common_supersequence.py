"""
Challenge 1: Shortest Common Supersequence
==========================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the shortest common supersequence of str1 and str2.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Compute the LCS table (2D DP). 2. Backtrack through the table to build the SCS: when chars match,

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(str1: str, str2: str) -> str:
    """Return the shortest common supersequence of str1 and str2."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(solve(str1, str2))
