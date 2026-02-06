"""
Tests for Warmup 06: Multiplication Table
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_warmup_06.py -v
"""

from ch03.practice.warmup_06_multiplication_table import solve


def test_seven():
    """Multiplication table of 7."""
    result = solve(7)
    assert result == [
        "1 x 7 = 7",
        "2 x 7 = 14",
        "3 x 7 = 21",
        "4 x 7 = 28",
        "5 x 7 = 35",
        "6 x 7 = 42",
        "7 x 7 = 49",
        "8 x 7 = 56",
        "9 x 7 = 63",
        "10 x 7 = 70",
    ]


def test_one():
    """Multiplication table of 1."""
    result = solve(1)
    assert result[0] == "1 x 1 = 1"
    assert result[-1] == "10 x 1 = 10"


def test_five_first_and_last():
    """First and last entries of table of 5."""
    result = solve(5)
    assert result[0] == "1 x 5 = 5"
    assert result[-1] == "10 x 5 = 50"


def test_length():
    """Every table has exactly 10 entries."""
    assert len(solve(3)) == 10
    assert len(solve(99)) == 10
