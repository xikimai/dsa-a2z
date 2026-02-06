"""
Tests for Challenge 01: Diamond Pattern
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_challenge_01.py -v
"""

from ch03.practice.challenge_01_diamond import solve


def test_one():
    """A diamond with n=1 is just a single star."""
    assert solve(1) == "*"


def test_two():
    """A diamond with n=2 has 3 rows."""
    assert solve(2) == " *\n***\n *"


def test_three():
    """A diamond with n=3 has 5 rows."""
    assert solve(3) == "  *\n ***\n*****\n ***\n  *"


def test_four_dimensions():
    """A diamond with n=4 should have 7 lines, middle line has 7 stars."""
    result = solve(4)
    lines = result.split("\n")
    assert len(lines) == 7
    assert lines[3] == "*******"
