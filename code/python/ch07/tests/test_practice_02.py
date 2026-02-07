"""
Tests for Practice 2: GCD and LCM
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_practice_02.py -v
"""

from ch07.practice.practice_02_gcd_and_lcm import solve


def test_basic():
    assert solve(12, 18) == [6, 36]


def test_coprime():
    assert solve(7, 13) == [1, 91]


def test_zero_and_number():
    assert solve(0, 5) == [5, 0]


def test_larger():
    assert solve(100, 75) == [25, 300]


def test_equal():
    assert solve(6, 6) == [6, 6]


def test_one():
    assert solve(1, 1) == [1, 1]
