"""
Warmup 1: Trie Insert and Search
================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Insert all words into a trie, return whether each query is a complete word.

EXAMPLES
--------
  solve(["a", "b"], []) -> []
  solve(["cat", "dog"], ["bird", "fish"]) -> [False, False]
  solve(["application"], ["app", "application"]) -> [False, True]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build a Trie. Insert all words, marking end-of-word nodes. For each query, walk down the trie; return True only if we reach

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(words: list[str], queries: list[str]) -> list[bool]:
    """Insert all words into a trie, return whether each query is a complete word."""
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
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        queries.append(tokens[idx]); idx += 1
    result = solve(words, queries)
    print(" ".join(str(r) for r in result))
