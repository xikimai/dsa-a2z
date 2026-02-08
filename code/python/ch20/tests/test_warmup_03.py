"""
Tests for Warmup 3: Max Area of Island
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_warmup_03.py -v
"""
from ch20.practice.warmup_03_max_area_of_island import solve


def test_basic():
    grid = [[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 1, 0, 0]]
    assert solve(grid) == 5


def test_no_island():
    grid = [[0, 0, 0, 0]]
    assert solve(grid) == 0


def test_single_cell():
    grid = [[1]]
    assert solve(grid) == 1


def test_all_land():
    grid = [[1, 1], [1, 1]]
    assert solve(grid) == 4


def test_multiple_islands():
    grid = [[1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 1]]
    assert solve(grid) == 2


def test_l_shaped():
    grid = [[1, 0], [1, 0], [1, 1]]
    assert solve(grid) == 4
