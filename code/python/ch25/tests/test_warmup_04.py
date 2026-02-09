"""
Tests for Warmup 4: Coin Change II (Count Ways)
==================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_warmup_04.py -v
"""
from ch25.practice.warmup_04_coin_change_ways import solve


def test_basic():
    assert solve([1, 2, 5], 5) == 4


def test_impossible():
    assert solve([2], 3) == 0


def test_exact():
    assert solve([10], 10) == 1


def test_zero_amount():
    assert solve([1, 2], 0) == 1


def test_single_coin():
    assert solve([1], 5) == 1


def test_two_coins():
    assert solve([1, 2], 5) == 3
