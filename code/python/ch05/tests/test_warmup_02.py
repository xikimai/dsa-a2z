"""
Tests for Warmup 2: Reverse List
========================================
Chapter 5: Collections

Run with:
    python -m pytest code/python/ch05/tests/test_warmup_02.py -v
"""

from ch05.practice.warmup_02_reverse_list import solve


def test_basic_case():
    """Reverse a list of five elements."""
    assert solve([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_single_element():
    """Single element stays the same."""
    assert solve([1]) == [1]


def test_empty_list():
    """Empty list stays empty."""
    assert solve([]) == []


def test_two_elements():
    """Two elements swap."""
    assert solve([1, 2]) == [2, 1]


def test_already_reversed():
    """A descending list becomes ascending."""
    assert solve([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
