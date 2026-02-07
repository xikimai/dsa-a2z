"""
Tests for Warmup 3: Sum of Digits
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_warmup_03.py -v
"""

from ch07.practice.warmup_03_sum_of_digits import solve


def test_basic():
    assert solve(12345) == 15


def test_zero():
    assert solve(0) == 0


def test_negative():
    assert solve(-456) == 15


def test_all_nines():
    assert solve(999) == 27


def test_trailing_zeros():
    assert solve(100) == 1
