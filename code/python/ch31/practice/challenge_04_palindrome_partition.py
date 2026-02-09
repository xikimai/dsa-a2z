"""
Challenge 4: Palindrome Partitioning II
=======================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

PROBLEM
-------
Return minimum cuts to partition s into palindromes.

EXAMPLES
--------
  solve("aab") -> 1
  solve("a") -> 0
  solve("ab") -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Precompute is_pal[i][j] = whether s[i..j] is a palindrome using DP. 2. dp[i] = minimum cuts to partition s[0..i] into palindromes.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> int:
    """Return minimum cuts to partition s into palindromes."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
