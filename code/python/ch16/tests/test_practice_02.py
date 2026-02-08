"""
Tests for Practice 2: Ship Packages Within D Days
===================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

Run with:
    python -m pytest code/python/ch16/tests/test_practice_02.py -v
"""
from ch16.practice.practice_02_ship_packages import solve


def test_basic():
    assert solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15


def test_one_day():
    assert solve([3, 2, 2, 4, 1, 4], 1) == 16


def test_many_days():
    assert solve([3, 2, 2, 4, 1, 4], 6) == 4


def test_single_package():
    assert solve([10], 1) == 10


def test_equal_weights():
    assert solve([5, 5, 5, 5], 2) == 10


def test_heavy_last():
    assert solve([1, 2, 3, 1, 1], 4) == 3


def test_three_days():
    assert solve([3, 2, 2, 4, 1, 4], 3) == 6
