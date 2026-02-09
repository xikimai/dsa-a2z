"""
Tests for Practice 5: XOR on Range (Segment Tree)
==================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_practice_05.py -v
"""
from ch30.practice.practice_05_xor_range import solve


def test_basic():
    assert solve([1, 2, 3, 4, 5], [[1, 0, 4], [2, 2, 7], [1, 0, 4]]) == [1, 5]


def test_small():
    assert solve([3, 5], [[1, 0, 1], [2, 0, 6], [1, 0, 1]]) == [6, 3]


def test_single():
    assert solve([42], [[1, 0, 0]]) == [42]
