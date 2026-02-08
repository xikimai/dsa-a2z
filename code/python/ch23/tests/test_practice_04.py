"""
Tests for Practice 4: Best Time to Buy and Sell Stock I
==========================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_practice_04.py -v
"""
from ch23.practice.practice_04_stock_i import solve


def test_basic():
    assert solve([7, 1, 5, 3, 6, 4]) == 5


def test_decreasing():
    assert solve([7, 6, 4, 3, 1]) == 0


def test_single():
    assert solve([1]) == 0


def test_two_increasing():
    assert solve([1, 2]) == 1


def test_two_decreasing():
    assert solve([2, 1]) == 0
