"""
Tests for Practice 5: Trailing Zeros in Factorial
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_practice_05.py -v
"""

from ch07.practice.practice_05_trailing_zeros import solve


def test_five():
    assert solve(5) == 1


def test_ten():
    assert solve(10) == 2


def test_twenty_five():
    """25 = 5*5, so it contributes 2 factors of 5!"""
    assert solve(25) == 6


def test_hundred():
    assert solve(100) == 24


def test_zero():
    assert solve(0) == 0
