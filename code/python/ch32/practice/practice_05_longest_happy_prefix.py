"""
Practice 5: Longest Happy Prefix
================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Return the longest prefix of s that is also a suffix (not entire string).

EXAMPLES
--------
  solve("level") -> "l"
  solve("ababab") -> "abab"
  solve("a") -> ""

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build the KMP failure function. The last value fail[n-1] gives the length of the longest proper prefix which is also a suffix of the

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> str:
    """Return the longest prefix of s that is also a suffix (not entire string)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
