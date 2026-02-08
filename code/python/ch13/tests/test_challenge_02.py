"""
Tests for Challenge 2: Word Search
Run with: python -m pytest code/python/ch13/tests/test_challenge_02.py -v
"""
from ch13.practice.challenge_02_word_search import solve


def test_abcced():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert solve(board, "ABCCED") is True


def test_see():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert solve(board, "SEE") is True


def test_abcb():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert solve(board, "ABCB") is False


def test_single_cell_match():
    assert solve([["A"]], "A") is True


def test_single_cell_no_match():
    assert solve([["A"]], "B") is False


def test_word_longer_than_grid():
    board = [["A", "B"], ["C", "D"]]
    assert solve(board, "ABCDA") is False


def test_snake_path():
    board = [["A", "B", "C"], ["F", "E", "D"]]
    assert solve(board, "ABCDEF") is True
