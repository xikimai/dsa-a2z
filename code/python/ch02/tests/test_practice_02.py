"""
Tests for Practice 02: Time Conversion
========================================
Chapter 2: Your First Programs

Run with:
    python -m pytest code/python/ch02/tests/test_practice_02.py -v
"""

from ch02.practice.practice_02_time_conversion import solve


def test_mixed_time():
    """3661 seconds is 1 hour, 1 minute, 1 second."""
    assert solve(3661) == (1, 1, 1)


def test_zero_seconds():
    """0 seconds is 0 hours, 0 minutes, 0 seconds."""
    assert solve(0) == (0, 0, 0)


def test_almost_full_day():
    """86399 seconds is 23 hours, 59 minutes, 59 seconds."""
    assert solve(86399) == (23, 59, 59)


def test_only_seconds():
    """45 seconds is 0 hours, 0 minutes, 45 seconds."""
    assert solve(45) == (0, 0, 45)


def test_exact_hour():
    """3600 seconds is exactly 1 hour."""
    assert solve(3600) == (1, 0, 0)


def test_exact_minute():
    """60 seconds is exactly 1 minute."""
    assert solve(60) == (0, 1, 0)


def test_two_hours_thirty_minutes():
    """9000 seconds is 2 hours, 30 minutes, 0 seconds."""
    assert solve(9000) == (2, 30, 0)
