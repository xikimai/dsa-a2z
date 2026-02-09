"""
Tests for Practice 2: Minimum Falling Path Sum
=================================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_practice_02.py -v
"""
from ch24.practice.practice_02_min_falling_path import solve


def test_basic():
    assert solve([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13


def test_negative():
    assert solve([[-19, 57], [-40, -5]]) == -59


def test_single():
    assert solve([[-48]]) == -48


def test_all_same():
    assert solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3


def test_two_by_two():
    assert solve([[1, 2], [3, 4]]) == 4
