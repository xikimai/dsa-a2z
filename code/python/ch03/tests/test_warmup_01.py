"""
Tests for Warmup 01: Even or Odd
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_warmup_01.py -v
"""

from ch03.practice.warmup_01_even_odd import solve


def test_even_number():
    """4 is even."""
    assert solve(4) == "Even"


def test_odd_number():
    """7 is odd."""
    assert solve(7) == "Odd"


def test_zero_is_even():
    """0 is even."""
    assert solve(0) == "Even"


def test_negative_odd():
    """-3 is odd."""
    assert solve(-3) == "Odd"


def test_one_is_odd():
    """1 is odd."""
    assert solve(1) == "Odd"
