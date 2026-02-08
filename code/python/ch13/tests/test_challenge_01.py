"""
Tests for Challenge 1: Sudoku Solver
Run with: python -m pytest code/python/ch13/tests/test_challenge_01.py -v
"""
from ch13.practice.challenge_01_sudoku_solver import solve


def _is_valid_sudoku(board):
    """Check if a completed board is a valid Sudoku solution."""
    for i in range(9):
        row = set(board[i])
        if row != set(range(1, 10)):
            return False
        col = set(board[r][i] for r in range(9))
        if col != set(range(1, 10)):
            return False
    for br in range(3):
        for bc in range(3):
            box = set()
            for r in range(br * 3, br * 3 + 3):
                for c in range(bc * 3, bc * 3 + 3):
                    box.add(board[r][c])
            if box != set(range(1, 10)):
                return False
    return True


def test_standard_puzzle():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    result = solve(board)
    assert _is_valid_sudoku(result)
    assert result[0][0] == 5
    assert result[0][2] == 4


def test_easy_puzzle():
    board = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]
    result = solve(board)
    assert _is_valid_sudoku(result)


def test_almost_complete():
    board = [
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 3, 6, 5, 8, 9, 7],
        [3, 6, 5, 8, 9, 7, 2, 1, 4],
        [8, 9, 7, 2, 1, 4, 3, 6, 5],
        [5, 3, 1, 6, 4, 2, 9, 7, 8],
        [6, 4, 2, 9, 7, 8, 5, 3, 1],
        [9, 7, 8, 5, 3, 1, 6, 4, 2]
    ]
    result = solve(board)
    assert _is_valid_sudoku(result)
    assert result[0][8] == 9


def test_preserves_given_values():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    result = solve(board)
    assert result[0][0] == 5
    assert result[1][3] == 1
    assert result[8][8] == 9
