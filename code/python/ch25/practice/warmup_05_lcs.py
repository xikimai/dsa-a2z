"""
Warmup 5: Longest Common Subsequence
====================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the length of the longest common subsequence.

EXAMPLES
--------
  solve("abcde", "ace") -> 3
  solve("abc", "abc") -> 3
  solve("abc", "def") -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Space-optimized 2-row DP. dp[j] = LCS length of text1[:i] and text2[:j].

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(text1: str, text2: str) -> int:
    """Return the length of the longest common subsequence."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    text1 = input().strip()
    text2 = input().strip()
    print(solve(text1, text2))
