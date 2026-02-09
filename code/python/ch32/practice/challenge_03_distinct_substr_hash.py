"""
Challenge 3: Distinct Substrings of Length K (Rolling Hash)
===========================================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Count distinct substrings of length k.

EXAMPLES
--------
  solve("abcabc", 3) -> 3
  solve("aaaa", 2) -> 1
  solve("abcdef", 1) -> 6

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Use a rolling hash to compute the hash of each substring of length k. Store all hashes in a set. The size of the set is the answer.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(s: str, k: int) -> int:
    """Count distinct substrings of length k."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    print(solve(data[0], int(data[1])))
