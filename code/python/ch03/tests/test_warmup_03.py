"""
Tests for Warmup 03: Largest of Three
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_warmup_03.py -v
"""

from ch03.practice.warmup_03_largest_of_three import solve


def test_ascending():
    """Largest of (1, 2, 3) is 3."""
    assert solve(1, 2, 3) == 3


def test_descending():
    """Largest of (3, 2, 1) is 3."""
    assert solve(3, 2, 1) == 3


def test_all_equal():
    """Largest of (5, 5, 5) is 5."""
    assert solve(5, 5, 5) == 5


def test_all_negative():
    """Largest of (-1, -2, -3) is -1."""
    assert solve(-1, -2, -3) == -1


def test_tie_for_largest():
    """Largest of (10, 5, 10) is 10."""
    assert solve(10, 5, 10) == 10
