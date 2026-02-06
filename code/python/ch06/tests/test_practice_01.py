"""
Tests for Practice 1: Contains Duplicate
========================================
Chapter 6: How Fast Is Your Code?

Run with:
    python -m pytest code/python/ch06/tests/test_practice_01.py -v
"""

from ch06.practice.practice_01_contains_duplicate import solve


def test_has_duplicate():
    """List with a repeated element."""
    assert solve([1, 2, 3, 1]) is True


def test_no_duplicate():
    """All elements distinct."""
    assert solve([1, 2, 3, 4]) is False


def test_empty():
    """Empty list has no duplicates."""
    assert solve([]) is False


def test_single_element():
    """Single element, no duplicate possible."""
    assert solve([1]) is False


def test_pair_duplicate():
    """Two identical elements."""
    assert solve([1, 1]) is True
