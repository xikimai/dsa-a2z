"""
Challenge 5: Minimum Insertions for Palindrome
==============================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the minimum number of insertions to make s a palindrome.

EXAMPLES
--------
  solve("zzazz") -> 0
  solve("mbadm") -> 2
  solve("leetcode") -> 5

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
min_insertions = len(s) - LPS(s), where LPS = Longest Palindromic Subsequence. LPS(s) = LCS(s, reverse(s)). Use space-optimized LCS.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> int:
    """Return the minimum number of insertions to make s a palindrome."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
