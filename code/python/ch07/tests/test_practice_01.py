"""
Tests for Practice 1: All Divisors (Sorted)
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_practice_01.py -v
"""

from ch07.practice.practice_01_all_divisors import solve


def test_perfect_square():
    assert solve(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]


def test_one():
    assert solve(1) == [1]


def test_prime():
    assert solve(7) == [1, 7]


def test_composite():
    assert solve(12) == [1, 2, 3, 4, 6, 12]


def test_large_prime():
    assert solve(97) == [1, 97]
