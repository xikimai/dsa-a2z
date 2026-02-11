"""
Challenge 2: Word Search
==========================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given an m x n grid of characters and a target word, determine if the
word exists in the grid. The word can be constructed from letters of
adjacent cells (horizontally or vertically). Each cell may be used at
most once per word.

INPUT FORMAT
------------
First line: two integers m and n (rows and columns).
Next m lines: n space-separated characters.
Last line: the target word.

OUTPUT FORMAT
-------------
True or False.

CONSTRAINTS
-----------
- 1 <= m, n <= 6
- 1 <= len(word) <= 15
- Board cells and word contain uppercase English letters

EXAMPLES
--------
Input:
  3 4
  A B C E
  S F C S
  A D E E
  ABCCED
Output: True

Input:
  3 4
  A B C E
  S F C S
  A D E E
  ABCB
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(board: list[list[str]], word: str) -> bool:
    """Return True if word exists in the grid."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    m, n = map(int, input().split())
    board = []
    for _ in range(m):
        board.append(input().split())
    word = input().strip()
    print(solve(board, word))

