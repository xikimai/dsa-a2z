"""
Tests for Practice 2: Password Strength
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_practice_02.py -v
"""

from ch04.practice.practice_02_password_strength import solve


def test_short_password():
    """Less than 8 characters is weak."""
    assert solve("hello") == "weak"


def test_empty_password():
    """Empty password is weak."""
    assert solve("") == "weak"


def test_seven_chars_no_digit():
    """Exactly 7 chars without digit is weak."""
    assert solve("abcdefg") == "weak"


def test_long_no_digit():
    """8+ chars but no digit is weak."""
    assert solve("ABCDEFGH") == "weak"


def test_medium_password():
    """8+ chars with digit but no uppercase."""
    assert solve("hello123") == "medium"


def test_strong_password():
    """8+ chars with digit and uppercase."""
    assert solve("Hello123") == "strong"


def test_long_only_lowercase_and_digits():
    """All lowercase with digits — medium."""
    assert solve("abcdef99") == "medium"


def test_exactly_eight_strong():
    """Exactly 8 chars, has digit and uppercase."""
    assert solve("Abcdef1x") == "strong"
