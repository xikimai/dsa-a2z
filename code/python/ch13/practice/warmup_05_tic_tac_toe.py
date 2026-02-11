"""
Warmup 5: Check Tic-Tac-Toe Winner
====================================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given a 3x3 tic-tac-toe board, determine the current state of the game.
Return 'X' if X wins, 'O' if O wins, 'Draw' if no winner and no empty
cells, or 'Ongoing' if the game is still in progress.

INPUT FORMAT
------------
Three lines, each containing three space-separated characters ('X', 'O', or '.').

OUTPUT FORMAT
-------------
One of: 'X', 'O', 'Draw', or 'Ongoing'.

CONSTRAINTS
-----------
- Board is always 3x3
- Characters are 'X', 'O', or '.' (empty)

EXAMPLES
--------
Input:
  X X X
  O O .
  . . .
Output: X

Input:
  X O X
  O X O
  O X O
Output: Draw

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(board: list[list[str]]) -> str:
    """Return 'X', 'O', 'Draw', or 'Ongoing'."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    board = []
    for _ in range(3):
        board.append(input().split())
    print(solve(board))

