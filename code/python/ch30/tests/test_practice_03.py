"""
Tests for Practice 3: Count of Elements in Range
=================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_practice_03.py -v
"""
from ch30.practice.practice_03_count_in_range import solve


def test_basic():
    assert solve([1, 3, 5, 7, 9, 2, 4, 6],
                 [[0, 7, 3, 7], [0, 3, 1, 5], [2, 5, 5, 9]]) == [5, 3, 3]


def test_single_match():
    assert solve([10, 20, 30], [[0, 2, 15, 25]]) == [1]


def test_no_match():
    assert solve([1, 2, 3], [[0, 2, 10, 20]]) == [0]


def test_all_match():
    assert solve([5, 5, 5], [[0, 2, 5, 5]]) == [3]
