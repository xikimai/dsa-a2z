"""
Tests for Warmup 4: Surrounded Regions
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_warmup_04.py -v
"""
from ch20.practice.warmup_04_surrounded_regions import solve


def test_basic():
    board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    result = solve(board)
    assert result == [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]


def test_border_connected():
    board = [['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'X', 'X']]
    result = solve(board)
    assert result == [['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'X', 'X']]


def test_all_x():
    board = [['X', 'X'], ['X', 'X']]
    result = solve(board)
    assert result == [['X', 'X'], ['X', 'X']]


def test_all_o():
    board = [['O', 'O'], ['O', 'O']]
    result = solve(board)
    # All O's are on the border, so none should be flipped
    assert result == [['O', 'O'], ['O', 'O']]


def test_single_cell():
    board = [['O']]
    result = solve(board)
    assert result == [['O']]


def test_inner_surrounded():
    board = [['X', 'X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'O', 'X'],
             ['X', 'O', 'X', 'O', 'X'],
             ['X', 'O', 'O', 'O', 'X'],
             ['X', 'X', 'X', 'X', 'X']]
    result = solve(board)
    assert result == [['X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X']]
