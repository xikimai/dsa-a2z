"""
Tests for Practice 3: Merge Intervals
========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_practice_03.py -v
"""
from ch18.practice.practice_03_merge_intervals import solve


def test_basic():
    assert solve([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_touching():
    assert solve([[1, 4], [4, 5]]) == [[1, 5]]


def test_contained():
    assert solve([[1, 4], [2, 3]]) == [[1, 4]]


def test_no_overlap():
    assert solve([[1, 2], [5, 6], [9, 10]]) == [[1, 2], [5, 6], [9, 10]]


def test_all_same():
    assert solve([[1, 5], [1, 5], [1, 5]]) == [[1, 5]]


def test_single():
    assert solve([[1, 10]]) == [[1, 10]]


def test_unsorted():
    assert solve([[1, 4], [0, 4]]) == [[0, 4]]


def test_empty():
    assert solve([]) == []
