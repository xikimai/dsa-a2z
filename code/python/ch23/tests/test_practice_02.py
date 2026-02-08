"""
Tests for Practice 2: House Robber II (Circular)
====================================================
Chapter 23: Dynamic Programming I — The Foundation

Run with:
    python -m pytest code/python/ch23/tests/test_practice_02.py -v
"""
from ch23.practice.practice_02_house_robber_ii import solve


def test_basic():
    assert solve([2, 3, 2]) == 3


def test_four_houses():
    assert solve([1, 2, 3, 1]) == 4


def test_three_houses():
    assert solve([1, 2, 3]) == 3


def test_single():
    assert solve([5]) == 5


def test_two():
    assert solve([1, 2]) == 2


def test_larger():
    assert solve([1, 3, 1, 3, 100]) == 103
