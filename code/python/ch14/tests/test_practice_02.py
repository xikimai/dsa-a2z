"""
Tests for Practice 2: Subarray Sum Equals K (Count)
=====================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_practice_02.py -v
"""
from ch14.practice.practice_02_subarray_sum_k import solve


def test_basic():
    assert solve([1, 1, 1], 2) == 2


def test_two_ways():
    assert solve([1, 2, 3], 3) == 2


def test_no_match():
    assert solve([1], 0) == 0


def test_zeros():
    assert solve([1, -1, 0], 0) == 3


def test_all_zeros():
    assert solve([0, 0, 0], 0) == 6


def test_single_match():
    assert solve([1], 1) == 1


def test_negative_k():
    assert solve([1, -2, 3, -1], -1) == 2
