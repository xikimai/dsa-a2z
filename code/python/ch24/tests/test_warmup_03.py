"""
Tests for Warmup 3: Minimum Path Sum
=======================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_warmup_03.py -v
"""
from ch24.practice.warmup_03_min_path_sum import solve


def test_basic():
    assert solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7


def test_single_row():
    assert solve([[1, 2, 3]]) == 6


def test_single_col():
    assert solve([[1], [2], [3]]) == 6


def test_single_cell():
    assert solve([[5]]) == 5


def test_two_by_two():
    assert solve([[1, 2], [3, 4]]) == 7
