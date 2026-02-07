"""
Tests for Warmup 4: Palindrome Number
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_warmup_04.py -v
"""

from ch07.practice.warmup_04_palindrome_number import solve


def test_palindrome():
    assert solve(121) is True


def test_negative():
    assert solve(-121) is False


def test_not_palindrome():
    assert solve(10) is False


def test_zero():
    assert solve(0) is True


def test_four_digit_palindrome():
    assert solve(1001) is True


def test_large_palindrome():
    assert solve(1234321) is True
