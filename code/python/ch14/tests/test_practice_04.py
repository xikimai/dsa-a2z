"""
Tests for Practice 4: Range Update with Difference Array
==========================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_practice_04.py -v
"""
from ch14.practice.practice_04_range_update import solve


def test_basic():
    assert solve(5, [[1, 3, 2], [2, 4, 3], [0, 1, -1]]) == [-1, 1, 5, 5, 3]


def test_single_update():
    assert solve(4, [[0, 3, 5]]) == [5, 5, 5, 5]


def test_non_overlapping():
    assert solve(6, [[0, 1, 10], [4, 5, 20]]) == [10, 10, 0, 0, 20, 20]


def test_full_range():
    assert solve(3, [[0, 2, 7]]) == [7, 7, 7]


def test_single_element_update():
    assert solve(5, [[2, 2, 100]]) == [0, 0, 100, 0, 0]


def test_negative_updates():
    assert solve(4, [[0, 3, 10], [1, 2, -5]]) == [10, 5, 5, 10]
