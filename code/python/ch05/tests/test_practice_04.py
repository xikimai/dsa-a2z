"""
Tests for Practice 4: Sort by Frequency
=========================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_practice_04.py -v
"""

from ch05.practice.practice_04_sort_by_frequency import solve


def test_basic_case():
    """Mixed frequencies: 2 appears twice, 3 appears twice, 1 once."""
    assert solve([2, 3, 1, 3, 2]) == [2, 2, 3, 3, 1]


def test_equal_frequencies():
    """Equal frequencies — sort by value ascending."""
    assert solve([1, 1, 2, 2, 3]) == [1, 1, 2, 2, 3]


def test_single_element():
    """Single element list."""
    assert solve([1]) == [1]


def test_negative_numbers():
    """Negative numbers with ties."""
    assert solve([-1, -1, 2, 2, 3]) == [-1, -1, 2, 2, 3]


def test_all_same():
    """All elements the same."""
    assert solve([5, 5, 5]) == [5, 5, 5]
