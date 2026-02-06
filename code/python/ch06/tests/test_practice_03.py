"""
Tests for Practice 3: Sorted Squares
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_practice_03.py -v
"""

from ch06.practice.practice_03_sorted_squares import solve


def test_mixed_negatives_positives():
    """Mix of negative and positive values."""
    assert solve([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_all_negative():
    """All negatives — result is reversed squares."""
    assert solve([-3, -2, -1]) == [1, 4, 9]


def test_all_positive():
    """All non-negative — squares stay in order."""
    assert solve([0, 1, 2, 3]) == [0, 1, 4, 9]


def test_empty():
    """Empty input."""
    assert solve([]) == []


def test_symmetric():
    """Symmetric values around zero."""
    assert solve([-5, 5]) == [25, 25]
