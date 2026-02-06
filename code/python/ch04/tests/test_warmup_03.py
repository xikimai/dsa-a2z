"""
Tests for Warmup 3: Min of Three
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_warmup_03.py -v
"""

from ch04.practice.warmup_03_min_of_two import solve


def test_min_is_last():
    """Minimum is the third value."""
    assert solve(5, 3, 1) == 1


def test_min_is_first():
    """Minimum is the first value."""
    assert solve(1, 5, 3) == 1


def test_min_is_middle():
    """Minimum is the second value."""
    assert solve(5, 1, 3) == 1


def test_all_equal():
    """All three values are the same."""
    assert solve(4, 4, 4) == 4


def test_two_equal_min():
    """Two values tie for the minimum."""
    assert solve(2, 2, 5) == 2


def test_negative_numbers():
    """Negative numbers."""
    assert solve(-1, -5, 3) == -5


def test_all_negative():
    """All negative numbers."""
    assert solve(-10, -20, -5) == -20


def test_zero_included():
    """Zero is one of the values."""
    assert solve(0, 5, -3) == -3
