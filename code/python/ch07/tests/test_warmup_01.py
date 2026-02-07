"""
Tests for Warmup 1: Count Digits
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_warmup_01.py -v
"""

from ch07.practice.warmup_01_count_digits import solve


def test_five_digits():
    assert solve(12345) == 5


def test_zero():
    assert solve(0) == 1


def test_negative():
    assert solve(-42) == 2


def test_single_digit():
    assert solve(7) == 1


def test_ten_digits():
    assert solve(1000000000) == 10
