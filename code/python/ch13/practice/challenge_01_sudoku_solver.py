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
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))
    result = solve(board)
    for row in result:
        print(" ".join(map(str, row)))

