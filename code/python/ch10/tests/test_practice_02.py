"""
Tests for Practice 2: Sum of Digits
========================================
Chapter 10: The Magic of Recursion

Run with:
    python -m pytest code/python/ch10/tests/test_practice_02.py -v
"""
from ch10.practice.practice_02_sum_digits import solve


def test_five_digits():
    assert solve(12345) == 15


def test_zero():
    assert solve(0) == 0


def test_single_digit():
    assert solve(9) == 9


def test_all_nines():
    assert solve(999) == 27


def test_trailing_zeros():
    assert solve(100) == 1
