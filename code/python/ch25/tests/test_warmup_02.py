"""
Tests for Warmup 2: Subset Sum
=================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

Run with:
    python -m pytest code/python/ch25/tests/test_warmup_02.py -v
"""
from ch25.practice.warmup_02_subset_sum import solve


def test_basic_true():
    assert solve([3, 34, 4, 12, 5, 2], 9) is True


def test_basic_false():
    assert solve([3, 34, 4, 12, 5, 2], 30) is False


def test_sum_eleven():
    assert solve([1, 5, 11, 5], 11) is True


def test_target_zero():
    assert solve([1, 2, 3], 0) is True


def test_single_match():
    assert solve([5], 5) is True


def test_single_no_match():
    assert solve([5], 3) is False
