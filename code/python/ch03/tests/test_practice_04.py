"""
Tests for Practice 04: Right Triangle
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_practice_04.py -v
"""

from ch03.practice.practice_04_right_triangle import solve


def test_one_row():
    """A triangle with 1 row is just a single star."""
    assert solve(1) == "*"


def test_three_rows():
    """A right-aligned triangle with 3 rows."""
    assert solve(3) == "  *\n **\n***"


def test_four_rows():
    """A right-aligned triangle with 4 rows."""
    assert solve(4) == "   *\n  **\n ***\n****"
