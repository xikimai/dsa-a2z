"""
Challenge 2: Shortest Palindrome (KMP)
======================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Return the shortest palindrome by adding characters to the front of s.

EXAMPLES
--------
  solve("aacecaaa") -> "aaacecaaa"
  solve("abcd") -> "dcbabcd"
  solve("a") -> "a"

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
To make s a palindrome by adding characters to the front: 1. We need to find the longest palindromic prefix of s.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str) -> str:
    """Return the shortest palindrome by adding characters to the front of s."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    print(solve(s))
