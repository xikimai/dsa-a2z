"""
Tests for Challenge 1: Best Time to Buy and Sell Stock III
=============================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_challenge_01.py -v
"""
from ch23.practice.challenge_01_stock_iii import solve


def test_basic():
    assert solve([3, 3, 5, 0, 0, 3, 1, 4]) == 6


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == 4


def test_decreasing():
    assert solve([7, 6, 4, 3, 1]) == 0


def test_single():
    assert solve([1]) == 0


def test_one_transaction_best():
    assert solve([1, 2]) == 1
