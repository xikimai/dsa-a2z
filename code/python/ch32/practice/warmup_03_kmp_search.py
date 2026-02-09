"""
Warmup 3: KMP Pattern Search
============================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Return all starting indices where pattern occurs in text using KMP.

EXAMPLES
--------
  solve("AABAACAADAABAABA", "AABA") -> [0, 9, 12]
  solve("ABCABC", "ABC") -> [0, 3]
  solve("AAAAA", "AA") -> [0, 1, 2, 3]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Build the KMP failure function for the pattern. 2. Scan the text with two pointers (i for text, j for pattern).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(text: str, pattern: str) -> list[int]:
    """Return all starting indices where pattern occurs in text using KMP."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    text = data[0]
    pattern = data[1]
    result = solve(text, pattern)
    print(" ".join(str(r) for r in result))
