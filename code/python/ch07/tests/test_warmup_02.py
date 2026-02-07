"""
Tests for Warmup 2: Reverse a Number
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_warmup_02.py -v
"""

from ch07.practice.warmup_02_reverse_number import solve


def test_basic():
    assert solve(12345) == 54321


def test_negative():
    assert solve(-123) == -321


def test_trailing_zeros():
    assert solve(1200) == 21


def test_zero():
    assert solve(0) == 0


def test_single_digit():
    assert solve(5) == 5
