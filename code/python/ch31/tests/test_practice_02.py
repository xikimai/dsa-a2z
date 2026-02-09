"""
Tests for Practice 2: Burst Balloons
======================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_practice_02.py -v
"""
from ch31.practice.practice_02_burst_balloons import solve


def test_four_balloons():
    assert solve([3, 1, 5, 8]) == 167


def test_two_balloons():
    assert solve([1, 5]) == 10


def test_single_balloon():
    assert solve([7]) == 7


def test_three_balloons():
    assert solve([1, 2, 3]) == 12
