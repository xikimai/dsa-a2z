"""
Tests for Practice 3: Modular Exponentiation
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_practice_03.py -v
"""

from ch07.practice.practice_03_mod_exponentiation import solve


def test_small():
    assert solve(2, 10, 1000000007) == 1024


def test_medium():
    assert solve(2, 20, 1000000007) == 1048576


def test_zero_exponent():
    assert solve(123456789, 0, 1000000007) == 1


def test_large_exponent():
    assert solve(2, 100, 1000000007) == 976371285


def test_base_larger_than_mod():
    assert solve(1000000008, 1, 1000000007) == 1
