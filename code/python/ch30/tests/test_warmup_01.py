"""
Tests for Warmup 1: Range Sum Query (Segment Tree)
===================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_warmup_01.py -v
"""
from ch30.practice.warmup_01_range_sum import solve


def test_basic():
    assert solve([1, 3, 5, 7, 9, 11], [[1, 1, 3], [2, 1, 10], [1, 1, 3]]) == [15, 22]


def test_full_range():
    assert solve([1, 2, 3, 4, 5], [[1, 0, 4], [2, 2, 10], [1, 0, 4]]) == [15, 22]


def test_single_element():
    assert solve([5], [[1, 0, 0], [2, 0, 3], [1, 0, 0]]) == [5, 3]


def test_no_updates():
    assert solve([1, 2, 3], [[1, 0, 2], [1, 1, 1]]) == [6, 2]
