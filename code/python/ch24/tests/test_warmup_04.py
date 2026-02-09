"""
Tests for Warmup 4: Triangle Minimum Total
=============================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_warmup_04.py -v
"""
from ch24.practice.warmup_04_triangle import solve


def test_basic():
    assert solve([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11


def test_single():
    assert solve([[-10]]) == -10


def test_negative():
    assert solve([[-1], [2, 3], [1, -1, -3]]) == -1


def test_two_rows():
    assert solve([[1], [2, 3]]) == 3


def test_all_zeros():
    assert solve([[0], [0, 0], [0, 0, 0]]) == 0
