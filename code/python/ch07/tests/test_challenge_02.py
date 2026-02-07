"""
Tests for Challenge 2: Sieve of Eratosthenes
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_challenge_02.py -v
"""

from ch07.practice.challenge_02_sieve import solve


def test_ten():
    assert solve(10) == [2, 3, 5, 7]


def test_one():
    assert solve(1) == []


def test_two():
    assert solve(2) == [2]


def test_thirty():
    assert solve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_zero():
    assert solve(0) == []
