"""
Challenge 1: Sudoku Solver
============================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
Given a 9x9 Sudoku board with some cells filled (1-9) and some empty
(0), solve the puzzle. Each row, column, and 3x3 box must contain the
digits 1-9 exactly once.

INPUT FORMAT
------------
Nine lines, each with 9 space-separated integers (0 for empty cells).

OUTPUT FORMAT
-------------
Nine lines, each with 9 space-separated integers (the solved board).

CONSTRAINTS
-----------
- Board is always 9x9
- 0 <= board[i][j] <= 9
- The puzzle has exactly one solution

EXAMPLES
--------
Input:
  5 3 0 0 7 0 0 0 0
  6 0 0 1 9 5 0 0 0
  0 9 8 0 0 0 0 6 0
  8 0 0 0 6 0 0 0 3
  4 0 0 8 0 3 0 0 1
  7 0 0 0 2 0 0 0 6
  0 6 0 0 0 0 2 8 0
  0 0 0 4 1 9 0 0 5
  0 0 0 0 8 0 0 7 9
Output: (the completed board with all cells filled)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(board: list[list[int]]) -> list[list[int]]:
    """Solve the Sudoku puzzle and return the completed board."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    result = solve(board)
    for row in result:
        print(" ".join(map(str, row)))

