"""
Tests for Practice 02: Digit Count
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_practice_02.py -v
"""

from ch03.practice.practice_02_digit_count import solve


def test_five_digits():
    """12345 has 5 digits."""
    assert solve(12345) == 5


def test_zero():
    """0 has 1 digit."""
    assert solve(0) == 1


def test_single_digit():
    """9 has 1 digit."""
    assert solve(9) == 1


def test_negative():
    """-42 has 2 digits (ignore the sign)."""
    assert solve(-42) == 2


def test_seven_digits():
    """1000000 has 7 digits."""
    assert solve(1000000) == 7
