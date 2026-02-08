"""
Tests for Challenge 3: Stock with Transaction Fee
=====================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_challenge_03.py -v
"""
from ch23.practice.challenge_03_stock_fee import solve


def test_basic():
    assert solve([1, 3, 2, 8, 4, 9], 2) == 8


def test_basic2():
    assert solve([1, 3, 7, 5, 10, 3], 3) == 6


def test_single():
    assert solve([5], 1) == 0


def test_no_profit():
    assert solve([7, 6, 4, 3, 1], 2) == 0


def test_zero_fee():
    assert solve([1, 2, 3, 4, 5], 0) == 4
