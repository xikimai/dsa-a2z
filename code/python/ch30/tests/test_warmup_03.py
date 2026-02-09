"""
Tests for Warmup 3: Prefix Sum with BIT (Fenwick Tree)
======================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_warmup_03.py -v
"""
from ch30.practice.warmup_03_prefix_sum_bit import solve


def test_basic():
    assert solve([1, 2, 3, 4, 5], [[1, 3, 0], [2, 2, 5], [1, 3, 0]]) == [10, 15]


def test_with_add():
    assert solve([3, 1, 4, 1, 5], [[1, 4, 0], [2, 0, 2], [1, 4, 0]]) == [14, 16]


def test_single():
    assert solve([7], [[1, 0, 0], [2, 0, 3], [1, 0, 0]]) == [7, 10]
