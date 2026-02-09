"""
Practice 3: Count Distinct Substrings
=====================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Count the number of distinct substrings of s (including empty string).

EXAMPLES
--------
  solve("abab") -> 8
  solve("aaa") -> 4
  solve("abc") -> 7

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Generate all substrings and add them to a set. The count is len(set) + 1 (for the empty string, which we count separately).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> int:
    """Count the number of distinct substrings of s (including empty string)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
