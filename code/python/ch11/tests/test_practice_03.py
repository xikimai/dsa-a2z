"""
Tests for Practice 3: Longest Subarray with Sum K
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_practice_03.py -v
"""
from ch11.practice.practice_03_longest_subarray_sum_k import solve


def test_basic():
    assert solve([1, 2, 3, 1, 1, 1, 1], 3) == 3


def test_negatives():
    assert solve([-1, 1, 1], 1) == 3


def test_no_match():
    assert solve([1, 2, 3], 10) == 0


def test_zero_sum():
    assert solve([1, -1, 1, -1, 1], 0) == 4


def test_with_zeros():
    assert solve([2, 0, 0, 3], 3) == 3


def test_single():
    assert solve([1], 1) == 1
