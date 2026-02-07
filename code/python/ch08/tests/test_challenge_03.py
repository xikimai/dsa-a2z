"""
Tests for Challenge 3: Sort by Frequency
========================================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python -m pytest code/python/ch08/tests/test_challenge_03.py -v
"""

from ch08.practice.challenge_03_sort_by_frequency import solve


def test_basic():
    assert solve([1, 1, 2, 2, 2, 3]) == [2, 2, 2, 1, 1, 3]


def test_same_freq():
    assert solve([4, 4, 4, 5, 5, 6]) == [4, 4, 4, 5, 5, 6]


def test_all_unique():
    assert solve([1, 2, 3]) == [1, 2, 3]


def test_single():
    assert solve([5]) == [5]


def test_tiebreak():
    assert solve([3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3]
