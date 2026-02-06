"""
Tests for Practice 1: Calculator
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_practice_01.py -v
"""

from ch04.practice.practice_01_calculator import solve


def test_addition():
    """Basic addition."""
    assert solve(10, "+", 3) == 13


def test_subtraction():
    """Basic subtraction."""
    assert solve(10, "-", 3) == 7


def test_multiplication():
    """Basic multiplication."""
    assert solve(10, "*", 3) == 30


def test_division():
    """Basic integer division."""
    assert solve(10, "/", 3) == 3


def test_division_by_zero():
    """Division by zero returns None."""
    assert solve(10, "/", 0) is None


def test_invalid_operator():
    """Invalid operator returns None."""
    assert solve(10, "^", 3) is None


def test_negative_numbers():
    """Operations with negative numbers."""
    assert solve(-5, "+", 3) == -2


def test_subtract_to_negative():
    """Subtraction resulting in negative."""
    assert solve(3, "-", 10) == -7
