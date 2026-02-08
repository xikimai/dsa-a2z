"""
Solution for Warmup 5: Check Tic-Tac-Toe Winner
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Check all 8 winning lines (3 rows, 3 columns, 2 diagonals).
If any line is all X or all O, return the winner.
If no winner and empty cells remain, return Ongoing. Otherwise Draw.

TIME COMPLEXITY:  O(1) — board is always 3x3
SPACE COMPLEXITY: O(1)
"""


def solve(board: list[list[str]]) -> str:
    """Return 'X', 'O', 'Draw', or 'Ongoing'."""
    lines = []
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]])  # rows
        lines.append([board[0][i], board[1][i], board[2][i]])  # cols
    lines.append([board[0][0], board[1][1], board[2][2]])       # main diag
    lines.append([board[0][2], board[1][1], board[2][0]])       # anti diag

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != '.':
            return line[0]

    for row in board:
        if '.' in row:
            return 'Ongoing'
    return 'Draw'


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    board = []
    for _ in range(3):
        board.append(input().split())
    print(solve(board))
