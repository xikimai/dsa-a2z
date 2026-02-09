"""
Tests for Practice 1: Unique Paths III
=========================================
Chapter 24: Dynamic Programming II — Grids and Paths

Run with:
    python -m pytest code/python/ch24/tests/test_practice_01.py -v
"""
from ch24.practice.practice_01_unique_paths_iii import solve


def test_basic():
    assert solve([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2


def test_full_grid():
    assert solve([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4


def test_no_path():
    assert solve([[0, 1], [2, 0]]) == 0


def test_minimal():
    assert solve([[1, 2]]) == 1
