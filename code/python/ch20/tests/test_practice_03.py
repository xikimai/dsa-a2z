"""
Tests for Practice 3: Pacific Atlantic Water Flow
========================================
Chapter 20: Graphs II — Real Problems

Run with:
    python -m pytest code/python/ch20/tests/test_practice_03.py -v
"""
from ch20.practice.practice_03_pacific_atlantic import solve


def test_basic():
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert solve(heights) == expected


def test_single_cell():
    assert solve([[1]]) == [[0, 0]]


def test_flat():
    heights = [[1, 1], [1, 1]]
    expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert solve(heights) == expected


def test_downhill():
    heights = [[3, 3, 3], [3, 3, 3]]
    # All cells equal height -> water flows everywhere -> all reach both
    result = solve(heights)
    assert [0, 0] in result
    assert [1, 2] in result


def test_uphill():
    heights = [[1, 2, 3], [4, 5, 6]]
    # Higher cells reach both
    result = solve(heights)
    assert [1, 2] in result
