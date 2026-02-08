"""
Tests for Practice 4: Non-overlapping Intervals
=================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_practice_04.py -v
"""
from ch18.practice.practice_04_non_overlapping_intervals import solve


def test_basic():
    assert solve([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1


def test_all_same():
    assert solve([[1, 2], [1, 2], [1, 2]]) == 2


def test_no_overlap():
    assert solve([[1, 2], [2, 3]]) == 0


def test_all_overlap():
    assert solve([[1, 5], [2, 6], [3, 7]]) == 2


def test_single():
    assert solve([[1, 2]]) == 0


def test_nested():
    assert solve([[1, 100], [2, 3], [4, 5], [6, 7]]) == 1


def test_empty():
    assert solve([]) == 0
