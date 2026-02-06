"""
Tests for Warmup 05: Last Digit
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_warmup_05.py -v
"""

from ch02.practice.warmup_05_last_digit import solve


def test_last_digit_of_12345():
    """Last digit of 12345 is 5."""
    assert solve(12345) == 5


def test_last_digit_of_100():
    """Last digit of 100 is 0."""
    assert solve(100) == 0


def test_last_digit_of_negative():
    """Last digit of -789 is 9 (use absolute value)."""
    assert solve(-789) == 9


def test_last_digit_of_single():
    """Last digit of 7 is 7."""
    assert solve(7) == 7


def test_last_digit_of_zero():
    """Last digit of 0 is 0."""
    assert solve(0) == 0


def test_last_digit_of_negative_ten():
    """Last digit of -10 is 0."""
    assert solve(-10) == 0
