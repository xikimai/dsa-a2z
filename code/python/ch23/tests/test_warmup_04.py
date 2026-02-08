"""
Tests for Warmup 4: House Robber
====================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_warmup_04.py -v
"""
from ch23.practice.warmup_04_house_robber import solve


def test_basic():
    assert solve([1, 2, 3, 1]) == 4


def test_five_houses():
    assert solve([2, 7, 9, 3, 1]) == 12


def test_single():
    assert solve([5]) == 5


def test_two_houses():
    assert solve([1, 2]) == 2


def test_equal():
    assert solve([2, 1, 1, 2]) == 4
