"""
Tests for Warmup 1: Build Prefix Sum Array
=============================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_warmup_01.py -v
"""
from ch14.practice.warmup_01_build_prefix_sum import solve


def test_basic():
    assert solve([3, 1, 4, 1, 5]) == [0, 3, 4, 8, 9, 14]


def test_single():
    assert solve([5]) == [0, 5]


def test_empty():
    assert solve([]) == [0]


def test_negatives():
    assert solve([-1, -2, -3]) == [0, -1, -3, -6]


def test_mixed():
    assert solve([1, -1, 2, -2, 3]) == [0, 1, 0, 2, 0, 3]


def test_all_zeros():
    assert solve([0, 0, 0]) == [0, 0, 0, 0]
