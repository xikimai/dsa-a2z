"""
Tests for Practice 4: Row with Maximum 1s
==========================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_practice_04.py -v
"""
from ch16.practice.practice_04_row_max_ones import solve


def test_basic():
    matrix = [
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    assert solve(matrix) == 3


def test_all_zeros():
    matrix = [[0, 0, 0], [0, 0, 0]]
    assert solve(matrix) == -1


def test_all_ones():
    matrix = [[1, 1, 1], [1, 1, 1]]
    assert solve(matrix) == 0  # first row (tie-break: first)


def test_single_row():
    assert solve([[0, 1, 1]]) == 0


def test_single_element():
    assert solve([[1]]) == 0
    assert solve([[0]]) == -1


def test_last_row_wins():
    matrix = [[0, 0, 0], [0, 0, 1], [0, 1, 1]]
    assert solve(matrix) == 2


def test_first_row_wins():
    matrix = [[1, 1, 1], [0, 0, 1], [0, 1, 1]]
    assert solve(matrix) == 0
