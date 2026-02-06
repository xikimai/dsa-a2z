"""
Tests for Practice 4: Majority Element
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_practice_04.py -v
"""

from ch06.practice.practice_04_majority_element import solve


def test_small_odd():
    """Majority in a short list."""
    assert solve([3, 2, 3]) == 3


def test_longer():
    """Majority in a longer mixed list."""
    assert solve([2, 2, 1, 1, 1, 2, 2]) == 2


def test_single():
    """Single element is trivially the majority."""
    assert solve([1]) == 1


def test_majority_not_at_end():
    """Majority element appears mostly at the front."""
    assert solve([6, 6, 6, 7, 7]) == 6
