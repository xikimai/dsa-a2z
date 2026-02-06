"""
Tests for Warmup 02: Absolute Value
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_warmup_02.py -v
"""

from ch03.practice.warmup_02_absolute_value import solve


def test_positive():
    """Absolute value of 5 is 5."""
    assert solve(5) == 5


def test_negative():
    """Absolute value of -5 is 5."""
    assert solve(-5) == 5


def test_zero():
    """Absolute value of 0 is 0."""
    assert solve(0) == 0


def test_large_negative():
    """Absolute value of -100 is 100."""
    assert solve(-100) == 100


def test_one():
    """Absolute value of 1 is 1."""
    assert solve(1) == 1
