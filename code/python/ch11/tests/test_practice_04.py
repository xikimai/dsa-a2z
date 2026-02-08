"""
Tests for Practice 4: Count Subarrays with Sum K
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_practice_04.py -v
"""
from ch11.practice.practice_04_count_subarrays_sum_k import solve


def test_basic():
    assert solve([1, 1, 1], 2) == 2


def test_multiple():
    assert solve([1, 2, 3], 3) == 2


def test_no_match():
    assert solve([1], 0) == 0


def test_zero_sum():
    assert solve([1, -1, 0], 0) == 3


def test_all_zeros():
    assert solve([0, 0, 0], 0) == 6


def test_single():
    assert solve([1], 1) == 1
