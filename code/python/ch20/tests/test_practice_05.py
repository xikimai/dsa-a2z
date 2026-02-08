"""
Tests for Practice 5: Number of Enclaves
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_practice_05.py -v
"""
from ch20.practice.practice_05_number_of_enclaves import solve


def test_basic():
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    assert solve(grid) == 3


def test_no_enclaves():
    grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    assert solve(grid) == 0


def test_all_water():
    grid = [[0, 0], [0, 0]]
    assert solve(grid) == 0


def test_all_land_border():
    grid = [[1, 1], [1, 1]]
    assert solve(grid) == 0


def test_single_enclave():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert solve(grid) == 1


def test_border_connected():
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert solve(grid) == 0
