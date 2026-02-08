"""
Tests for Warmup 5: Check Tic-Tac-Toe Winner
Run with: python -m pytest code/python/ch13/tests/test_warmup_05.py -v
"""
from ch13.practice.warmup_05_tic_tac_toe import solve


def test_x_wins_row():
    assert solve([['X', 'X', 'X'], ['O', 'O', '.'], ['.', '.', '.']]) == 'X'


def test_o_wins_col():
    assert solve([['X', 'O', '.'], ['X', 'O', '.'], ['.', 'O', 'X']]) == 'O'


def test_x_wins_diagonal():
    assert solve([['X', 'O', 'O'], ['.', 'X', '.'], ['.', '.', 'X']]) == 'X'


def test_draw():
    assert solve([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]) == 'Draw'


def test_ongoing():
    assert solve([['X', 'O', '.'], ['O', 'X', '.'], ['.', '.', '.']]) == 'Ongoing'


def test_o_wins_anti_diagonal():
    assert solve([['.', '.', 'O'], ['.', 'O', 'X'], ['O', 'X', 'X']]) == 'O'
