"""
Tests for Practice 2: Range Max Query with Point Update
=======================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_practice_02.py -v
"""
from ch30.practice.practice_02_range_max import solve


def test_basic():
    assert solve([3, 1, 4, 1, 5, 9, 2, 6], [[1, 0, 7], [2, 5, 1], [1, 0, 7]]) == [9, 6]


def test_small():
    assert solve([1, 2, 3], [[1, 0, 2], [2, 1, 5], [1, 0, 2]]) == [3, 5]


def test_single():
    assert solve([10], [[1, 0, 0], [2, 0, 20], [1, 0, 0]]) == [10, 20]
