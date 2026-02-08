"""
Solution for Challenge 1: Sudoku Solver
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Backtracking: find first empty cell (0), try digits 1-9, validate
against row/column/box constraints, recurse.

TIME COMPLEXITY:  O(9^(empty cells)) worst case, much less with pruning
SPACE COMPLEXITY: O(81) — the board itself + recursion depth
"""


def solve(board: list[list[int]]) -> list[list[int]]:
    """Solve the Sudoku puzzle and return the completed board."""

    def is_valid(row, col, num):
        # Check row
        if num in board[row]:
            return False
        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False
        # Check 3x3 box
        box_r, box_c = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if board[r][c] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = 0
                    return False
        return True

    backtrack()
    return [row[:] for row in board]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    result = solve(board)
    for row in result:
        print(" ".join(map(str, row)))
