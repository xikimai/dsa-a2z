"""
Practice 1: Rabin-Karp Pattern Search
=====================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Return all starting indices where pattern occurs in text using Rabin-Karp.

EXAMPLES
--------
  solve("AABAACAADAABAABA", "AABA") -> [0, 9, 12]
  solve("ABABABAB", "ABAB") -> [0, 2, 4]
  solve("HELLO", "HELLO") -> [0]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Compute the hash of the pattern. Slide a window of length m across the text, updating the hash in O(1) using the rolling hash formula.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(text: str, pattern: str) -> list[int]:
    """Return all starting indices where pattern occurs in text using Rabin-Karp."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    text = data[0]
    pattern = data[1]
    result = solve(text, pattern)
    print(" ".join(str(r) for r in result))
