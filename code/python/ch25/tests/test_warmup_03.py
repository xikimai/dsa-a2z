"""
Tests for Warmup 3: Coin Change (Minimum Coins)
==================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_warmup_03.py -v
"""
from ch25.practice.warmup_03_coin_change_min import solve


def test_basic():
    assert solve([1, 5, 11], 15) == 3


def test_impossible():
    assert solve([2], 3) == -1


def test_zero_amount():
    assert solve([1], 0) == 0


def test_classic():
    assert solve([1, 2, 5], 11) == 3


def test_single_coin():
    assert solve([1], 5) == 5


def test_large_coin():
    assert solve([3, 7], 14) == 2
