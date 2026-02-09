"""
Challenge 4: Longest String Chain
=================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

PROBLEM
-------
Return the length of the longest string chain.

EXAMPLES
--------
  solve(["a", "b", "ba", "bca", "bda", "bdca"]) -> 4
  solve(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) -> 5
  solve(["abc"]) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Sort words by length. For each word, try removing each character to form a predecessor and look it up in a hash map.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(words: list[str]) -> int:
    """Return the length of the longest string chain."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    words = input().strip().split()
    print(solve(words))
