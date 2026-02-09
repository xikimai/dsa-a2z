"""
Tests for Practice 1: Range Sum with Range Update (Lazy Propagation)
====================================================================
Chapter 30: Segment Trees & Range Queries

Run with:
    python -m pytest code/python/ch30/tests/test_practice_01.py -v
"""
from ch30.practice.practice_01_lazy_range_sum import solve


def test_basic():
    assert solve(5, [[1, 0, 4, 3], [2, 0, 4], [1, 1, 3, 2], [2, 1, 3]]) == [15, 15]


def test_add_then_query():
    assert solve(3, [[1, 0, 2, 5], [2, 0, 2], [1, 0, 0, 10], [2, 0, 0]]) == [15, 15]


def test_single_element():
    assert solve(1, [[1, 0, 0, 7], [2, 0, 0]]) == [7]
