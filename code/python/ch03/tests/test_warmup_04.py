"""
Tests for Warmup 04: Count Down
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_warmup_04.py -v
"""

from ch03.practice.warmup_04_count_down import solve


def test_five():
    """Count down from 5."""
    assert solve(5) == [5, 4, 3, 2, 1]


def test_one():
    """Count down from 1."""
    assert solve(1) == [1]


def test_three():
    """Count down from 3."""
    assert solve(3) == [3, 2, 1]


def test_ten():
    """Count down from 10."""
    assert solve(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
