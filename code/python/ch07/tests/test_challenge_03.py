"""
Tests for Challenge 3: Sum of GCD Pairs
========================================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python -m pytest code/python/ch07/tests/test_challenge_03.py -v
"""

from ch07.practice.challenge_03_gcd_pair_sum import solve


def test_basic():
    assert solve([2, 4, 6]) == 6


def test_multiples_of_three():
    assert solve([3, 6, 9]) == 9


def test_larger():
    assert solve([12, 18, 24]) == 24


def test_single():
    assert solve([7]) == 0


def test_coprimes():
    assert solve([2, 3, 5, 7]) == 6
