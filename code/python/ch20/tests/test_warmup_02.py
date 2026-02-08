"""
Tests for Warmup 2: Number of Islands
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_warmup_02.py -v
"""
from ch20.practice.warmup_02_number_of_islands import solve


def test_three_islands():
    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
    assert solve(grid) == 3


def test_one_island():
    grid = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
    assert solve(grid) == 1


def test_no_islands():
    grid = [[0, 0, 0], [0, 0, 0]]
    assert solve(grid) == 0


def test_all_land():
    grid = [[1, 1], [1, 1]]
    assert solve(grid) == 1


def test_single_cell_land():
    grid = [[1]]
    assert solve(grid) == 1


def test_single_cell_water():
    grid = [[0]]
    assert solve(grid) == 0


def test_diagonal_not_connected():
    grid = [[1, 0], [0, 1]]
    assert solve(grid) == 2
