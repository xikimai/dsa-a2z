"""
Tests for Warmup 2: Range Sum Query
======================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_warmup_02.py -v
"""
from ch14.practice.warmup_02_range_sum_query import solve


def test_basic():
    assert solve([3, 1, 4, 1, 5, 9], [[0, 5], [2, 4], [3, 3]]) == [23, 10, 1]


def test_single_element_queries():
    assert solve([10, 20, 30], [[0, 0], [1, 1], [2, 2]]) == [10, 20, 30]


def test_full_range():
    assert solve([1, 2, 3, 4, 5], [[0, 4]]) == [15]


def test_adjacent_ranges():
    assert solve([1, 2, 3, 4], [[0, 1], [2, 3]]) == [3, 7]


def test_large_values():
    assert solve([1000000000, 1000000000, 1000000000], [[0, 2]]) == [3000000000]


def test_negatives():
    assert solve([-5, 3, -2, 7, -1], [[0, 4], [1, 3]]) == [2, 8]
