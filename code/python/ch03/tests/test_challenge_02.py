"""
Tests for Challenge 02: Prime Check
========================================
Chapter 3: Decisions and Loops

Run with:
    python -m pytest code/python/ch03/tests/test_challenge_02.py -v
"""

from ch03.practice.challenge_02_prime_check import solve


def test_two_is_prime():
    """2 is the smallest prime."""
    assert solve(2) is True


def test_three_is_prime():
    """3 is prime."""
    assert solve(3) is True


def test_four_not_prime():
    """4 = 2 x 2, not prime."""
    assert solve(4) is False


def test_one_not_prime():
    """1 is NOT prime (by definition)."""
    assert solve(1) is False


def test_zero_not_prime():
    """0 is not prime."""
    assert solve(0) is False


def test_seventeen_prime():
    """17 is prime."""
    assert solve(17) is True


def test_twenty_five_not_prime():
    """25 = 5 x 5, not prime."""
    assert solve(25) is False


def test_ninety_seven_prime():
    """97 is prime."""
    assert solve(97) is True


def test_negative_not_prime():
    """Negative numbers are not prime."""
    assert solve(-5) is False
