"""
Tests for Challenge 1: Prime Check
========================================
Chapter 4: Functions

Run with:
    python -m pytest code/python/ch04/tests/test_challenge_01.py -v
"""

from ch04.practice.challenge_01_prime_check import solve


def test_two_is_prime():
    """2 is the smallest prime."""
    assert solve(2) is True


def test_three_is_prime():
    """3 is prime."""
    assert solve(3) is True


def test_seven_is_prime():
    """7 is prime."""
    assert solve(7) is True


def test_one_is_not_prime():
    """1 is not prime."""
    assert solve(1) is False


def test_zero_is_not_prime():
    """0 is not prime."""
    assert solve(0) is False


def test_negative_is_not_prime():
    """Negative numbers are not prime."""
    assert solve(-7) is False


def test_four_is_not_prime():
    """4 is not prime (2 * 2)."""
    assert solve(4) is False


def test_fifteen_is_not_prime():
    """15 is not prime (3 * 5)."""
    assert solve(15) is False


def test_large_prime():
    """97 is prime."""
    assert solve(97) is True


def test_large_non_prime():
    """100 is not prime."""
    assert solve(100) is False
