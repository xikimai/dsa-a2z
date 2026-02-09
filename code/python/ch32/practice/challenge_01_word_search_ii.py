"""
Challenge 1: Word Search II (Trie + Backtracking)
=================================================
Chapter 32: String Algorithms — Beyond Brute Force

PROBLEM
-------
Find all words from the list that can be formed by adjacent cells on the board.

EXAMPLES
--------
  solve(board, words) -> []
  solve(board, words) -> ["a"]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
1. Build a Trie from the word list. 2. For each cell on the board, start a DFS/backtracking search.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(board: list[list[str]], words: list[str]) -> list[str]:
    """Find all words from the list that can be formed by adjacent cells on the board."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    rows = int(tokens[idx]); idx += 1
    cols = int(tokens[idx]); idx += 1
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(tokens[idx]); idx += 1
        board.append(row)
    n = int(tokens[idx]); idx += 1
    words = []
    for _ in range(n):
        words.append(tokens[idx]); idx += 1
    result = solve(board, words)
    print(" ".join(result))
