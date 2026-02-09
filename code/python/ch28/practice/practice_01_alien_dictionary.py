"""
Practice 1: Alien Dictionary
============================
Chapter 28: Topological Sort — Ordering Dependencies

PROBLEM
-------
Return the alien character ordering, or '' if invalid.

EXAMPLES
--------
  solve(["z", "x", "z"]) -> ""
  solve(["abc", "ab"]) -> ""

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Compare consecutive words to extract character ordering edges. 2. Topologically sort the characters using Kahn's algorithm.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque, defaultdict


def solve(words: list[str]) -> str:
    """Return the alien character ordering, or '' if invalid."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    words = sys.stdin.read().split()
    print(solve(words))
