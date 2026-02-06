"""
Tests for Challenge 01: Extract Digits
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_challenge_01.py -v
"""

from ch02.practice.challenge_01_extract_digits import solve


def test_123():
    """123 should give (1, 2, 3)."""
    assert solve(123) == (1, 2, 3)


def test_907():
    """907 should give (9, 0, 7) — tens digit is zero."""
    assert solve(907) == (9, 0, 7)


def test_100():
    """100 should give (1, 0, 0) — smallest 3-digit number with zeros."""
    assert solve(100) == (1, 0, 0)


def test_999():
    """999 should give (9, 9, 9) — largest 3-digit number."""
    assert solve(999) == (9, 9, 9)


def test_456():
    """456 should give (4, 5, 6)."""
    assert solve(456) == (4, 5, 6)


def test_500():
    """500 should give (5, 0, 0)."""
    assert solve(500) == (5, 0, 0)
