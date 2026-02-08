"""
Tests for Practice 5: Maximum Subarray Sum (Kadane's)
=======================================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_practice_05.py -v
"""
from ch14.practice.practice_05_max_subarray_sum import solve


def test_basic():
    assert solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_all_negative():
    assert solve([-5, -3, -1, -4]) == -1


def test_single():
    assert solve([1]) == 1


def test_all_positive():
    assert solve([5, 4, -1, 7, 8]) == 23


def test_single_negative():
    assert solve([-7]) == -7


def test_alternating():
    assert solve([2, -1, 2, -1, 2]) == 4


def test_large_dip():
    assert solve([10, -20, 30]) == 30
