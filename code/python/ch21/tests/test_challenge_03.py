"""
Tests for Challenge 3: Add Two Numbers
========================================
Chapter 21: Linked Lists — Pointers and Connections

Run with:
    python -m pytest code/python/ch21/tests/test_challenge_03.py -v
"""
from ch21.practice.challenge_03_add_two_numbers import solve


def test_basic():
    assert solve([2, 4, 3], [5, 6, 4]) == [7, 0, 8]  # 342 + 465 = 807


def test_carry():
    assert solve([9, 9, 9], [1]) == [0, 0, 0, 1]  # 999 + 1 = 1000


def test_zeros():
    assert solve([0], [0]) == [0]


def test_different_lengths():
    assert solve([9, 9], [1]) == [0, 0, 1]  # 99 + 1 = 100


def test_single_digits():
    assert solve([5], [5]) == [0, 1]  # 5 + 5 = 10


def test_no_carry():
    assert solve([1, 2, 3], [4, 5, 6]) == [5, 7, 9]  # 321 + 654 = 975
