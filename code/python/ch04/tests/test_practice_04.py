"""
Tests for Practice 4: Statistics
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_practice_04.py -v
"""

from ch04.practice.practice_04_stats import solve


def test_normal_list():
    """Normal list of positive integers."""
    assert solve([3, 1, 4, 1, 5, 9]) == [1.0, 9.0, 3.83]


def test_single_element():
    """Single element: min = max = avg."""
    assert solve([7]) == [7.0, 7.0, 7.0]


def test_all_same():
    """All elements are the same."""
    assert solve([5, 5, 5]) == [5.0, 5.0, 5.0]


def test_negative_numbers():
    """All negative numbers."""
    assert solve([-5, -2, -8]) == [-8.0, -2.0, -5.0]


def test_mixed_positive_negative():
    """Mix of positive and negative."""
    assert solve([-3, 0, 3]) == [-3.0, 3.0, 0.0]


def test_two_elements():
    """Two elements."""
    assert solve([10, 20]) == [10.0, 20.0, 15.0]


def test_average_rounding():
    """Average needs rounding to 2 decimal places."""
    assert solve([1, 2, 3]) == [1.0, 3.0, 2.0]
