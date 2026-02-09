"""
Tests for Warmup 2: Range Min Query (Segment Tree)
===================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_warmup_02.py -v
"""
from ch30.practice.warmup_02_range_min import solve


def test_basic():
    assert solve([2, 5, 1, 4, 9, 3], [[1, 0, 5], [2, 2, 8], [1, 0, 5]]) == [1, 2]


def test_update_changes_min():
    assert solve([7, 3, 8, 1, 6], [[1, 1, 3], [2, 3, 2], [1, 1, 3]]) == [1, 2]


def test_single_element():
    assert solve([5], [[1, 0, 0], [2, 0, 2], [1, 0, 0]]) == [5, 2]
