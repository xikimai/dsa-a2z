"""
Tests for Practice 4: Prime Factorization
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_practice_04.py -v
"""

from ch07.practice.practice_04_prime_factorization import solve


def test_twelve():
    assert solve(12) == [[2, 2], [3, 1]]


def test_one():
    assert solve(1) == []


def test_prime():
    assert solve(7) == [[7, 1]]


def test_360():
    assert solve(360) == [[2, 3], [3, 2], [5, 1]]


def test_power_of_two():
    assert solve(64) == [[2, 6]]
