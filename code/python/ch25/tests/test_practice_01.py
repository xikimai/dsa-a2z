"""
Tests for Practice 1: Partition Equal Subset Sum
===================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_practice_01.py -v
"""
from ch25.practice.practice_01_partition_equal_subset import solve


def test_basic_true():
    assert solve([1, 5, 11, 5]) is True


def test_basic_false():
    assert solve([1, 2, 3, 5]) is False


def test_pair():
    assert solve([1, 1]) is True


def test_odd_total():
    assert solve([1, 2, 3]) is True


def test_single():
    assert solve([1]) is False


def test_large_true():
    assert solve([1, 2, 3, 4, 5, 6, 7]) is True
