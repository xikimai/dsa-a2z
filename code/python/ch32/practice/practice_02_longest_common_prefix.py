"""
Practice 2: Longest Common Prefix (Trie-based)
==============================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Return the longest common prefix of all words.

EXAMPLES
--------
  solve(["flower", "flow", "flight"]) -> "fl"
  solve(["dog", "racecar", "car"]) -> ""
  solve(["interstellar", "internet", "internal"]) -> "inter"

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Insert all words into a Trie. Then walk from the root, following the single child path as long as:

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(words: list[str]) -> str:
    """Return the longest common prefix of all words."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    words = []
    for _ in range(n):
        words.append(tokens[idx]); idx += 1
    print(solve(words))
