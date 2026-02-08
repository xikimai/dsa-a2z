"""
Tests for Practice 5: Best Time to Buy and Sell Stock II
===========================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_practice_05.py -v
"""
from ch23.practice.practice_05_stock_ii import solve


def test_basic():
    assert solve([7, 1, 5, 3, 6, 4]) == 7


def test_increasing():
    assert solve([1, 2, 3, 4, 5]) == 4


def test_decreasing():
    assert solve([7, 6, 4, 3, 1]) == 0


def test_single():
    assert solve([5]) == 0


def test_flat():
    assert solve([3, 3, 3]) == 0
