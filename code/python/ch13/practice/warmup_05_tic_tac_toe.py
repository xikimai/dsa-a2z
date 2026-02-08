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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    board = []
    for _ in range(3):
        board.append(input().split())
    print(solve(board))

