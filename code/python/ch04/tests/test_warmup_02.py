"""
Tests for Warmup 2: Power
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_warmup_02.py -v
"""

from ch04.practice.warmup_02_power import solve


def test_two_to_the_ten():
    """2^10 = 1024."""
    assert solve(2, 10) == 1024


def test_five_cubed():
    """5^3 = 125."""
    assert solve(5, 3) == 125


def test_exponent_zero():
    """Anything to the power of 0 is 1."""
    assert solve(7, 0) == 1


def test_exponent_one():
    """Anything to the power of 1 is itself."""
    assert solve(9, 1) == 9


def test_base_zero():
    """0 raised to any positive power is 0."""
    assert solve(0, 5) == 0


def test_base_one():
    """1 raised to any power is 1."""
    assert solve(1, 100) == 1


def test_negative_base_even_exponent():
    """Negative base with even exponent gives positive result."""
    assert solve(-2, 4) == 16


def test_negative_base_odd_exponent():
    """Negative base with odd exponent gives negative result."""
    assert solve(-2, 3) == -8
