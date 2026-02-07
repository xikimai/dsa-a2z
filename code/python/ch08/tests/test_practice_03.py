"""
Tests for Practice 3: Dutch National Flag
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_practice_03.py -v
"""

from ch08.practice.practice_03_dutch_national_flag import solve


def test_basic():
    assert solve([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]


def test_single():
    assert solve([0]) == [0]


def test_reverse():
    assert solve([2, 1, 0]) == [0, 1, 2]


def test_all_same():
    assert solve([0, 0, 0]) == [0, 0, 0]


def test_mixed():
    assert solve([1, 0, 2, 1, 0, 2, 1]) == [0, 0, 1, 1, 1, 2, 2]
