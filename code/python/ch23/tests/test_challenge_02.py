"""
Tests for Challenge 2: Stock with Cooldown
=============================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_challenge_02.py -v
"""
from ch23.practice.challenge_02_stock_cooldown import solve


def test_basic():
    assert solve([1, 2, 3, 0, 2]) == 3


def test_single():
    assert solve([1]) == 0


def test_two_elements():
    assert solve([1, 2]) == 1


def test_decreasing():
    assert solve([5, 4, 3, 2, 1]) == 0


def test_alternating():
    assert solve([1, 4, 2, 7]) == 6
