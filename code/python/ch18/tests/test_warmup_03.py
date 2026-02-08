"""
Tests for Warmup 3: Best Time to Buy and Sell Stock
=====================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

Run with:
    python -m pytest code/python/ch18/tests/test_warmup_03.py -v
"""
from ch18.practice.warmup_03_best_buy_sell_stock import solve


def test_basic():
    assert solve([7, 1, 5, 3, 6, 4]) == 5


def test_decreasing():
    assert solve([7, 6, 4, 3, 1]) == 0


def test_single():
    assert solve([5]) == 0


def test_two_profit():
    assert solve([2, 4]) == 2


def test_two_no_profit():
    assert solve([4, 2]) == 0


def test_same_prices():
    assert solve([3, 3, 3]) == 0


def test_buy_first_sell_last():
    assert solve([1, 2, 3, 4, 5]) == 4


def test_valley_peak():
    assert solve([10, 1, 10]) == 9
