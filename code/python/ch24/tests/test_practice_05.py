"""
Tests for Practice 5: Count Square Submatrices
=================================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_practice_05.py -v
"""
from ch24.practice.practice_05_count_squares import solve


def test_basic():
    assert solve([[0, 1, 1, 1],
                  [1, 1, 1, 1],
                  [0, 1, 1, 1]]) == 15


def test_mixed():
    assert solve([[1, 0, 1],
                  [1, 1, 0],
                  [1, 1, 0]]) == 7


def test_all_ones():
    assert solve([[1, 1], [1, 1]]) == 5


def test_all_zeros():
    assert solve([[0, 0], [0, 0]]) == 0


def test_single():
    assert solve([[1]]) == 1
