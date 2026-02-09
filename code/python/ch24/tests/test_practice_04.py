"""
Tests for Practice 4: Cherry Pickup II
=========================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_practice_04.py -v
"""
from ch24.practice.practice_04_cherry_pickup_ii import solve


def test_basic():
    assert solve([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]) == 24


def test_large():
    assert solve([[1, 0, 0, 0, 0, 0, 1],
                  [2, 0, 0, 0, 0, 3, 0],
                  [2, 0, 9, 0, 0, 0, 0],
                  [0, 3, 0, 5, 4, 0, 0],
                  [1, 0, 2, 3, 0, 0, 6]]) == 28


def test_two_cols():
    assert solve([[1, 1], [1, 1]]) == 4
