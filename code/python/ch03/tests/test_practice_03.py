"""
Tests for Practice 03: Reverse Number
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_practice_03.py -v
"""

from ch03.practice.practice_03_reverse_number import solve


def test_1234():
    """Reverse of 1234 is 4321."""
    assert solve(1234) == 4321


def test_trailing_zeros():
    """Reverse of 1200 is 21 (leading zeros dropped)."""
    assert solve(1200) == 21


def test_single_digit():
    """Reverse of 5 is 5."""
    assert solve(5) == 5


def test_negative():
    """Reverse of -123 is -321."""
    assert solve(-123) == -321


def test_zero():
    """Reverse of 0 is 0."""
    assert solve(0) == 0


def test_100():
    """Reverse of 100 is 1."""
    assert solve(100) == 1
