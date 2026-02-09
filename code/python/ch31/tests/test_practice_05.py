"""
Tests for Practice 5: Count Numbers with Unique Digits
========================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

Run with:
    python -m pytest code/python/ch31/tests/test_practice_05.py -v
"""
from ch31.practice.practice_05_unique_digits import solve


def test_twenty():
    assert solve(20) == 19


def test_hundred():
    assert solve(100) == 90


def test_ten():
    assert solve(10) == 10


def test_one():
    assert solve(1) == 1


def test_nine():
    assert solve(9) == 9
