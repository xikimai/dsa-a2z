"""
Warmup 2: Trie Prefix Count
===========================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Count how many words have each prefix.

EXAMPLES
--------
  solve(["abc", "abd"], ["xyz"]) -> [0]
  solve(["a", "ab", "abc"], ["a", "ab", "abc", "abcd"]) -> [3, 2, 1, 0]
  solve(["hello"], []) -> []

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Build a Trie with prefix counters. Each node stores how many words pass through it. For each prefix query, walk down the trie and return

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(words: list[str], prefixes: list[str]) -> list[int]:
    """Count how many words have each prefix."""
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
    prefixes = []
    for _ in range(q):
        prefixes.append(tokens[idx]); idx += 1
    result = solve(words, prefixes)
    print(" ".join(str(r) for r in result))
