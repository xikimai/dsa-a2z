"""
Practice 3: Edit Distance
=========================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the minimum edit distance between word1 and word2.

EXAMPLES
--------
  solve("horse", "ros") -> 3
  solve("intention", "execution") -> 5
  solve("", "abc") -> 3

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized 2-row DP. dp[i][j] = min operations to convert word1[:i] to word2[:j].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(word1: str, word2: str) -> int:
    """Return the minimum edit distance between word1 and word2."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    word1 = input().strip()
    word2 = input().strip()
    print(solve(word1, word2))
