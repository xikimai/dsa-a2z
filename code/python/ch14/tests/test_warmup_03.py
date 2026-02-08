"""
Tests for Warmup 3: Running Sum of Array
==========================================
Chapter 14: Prefix Sums — The Running Total Trick

Run with:
    python -m pytest code/python/ch14/tests/test_warmup_03.py -v
"""
from ch14.practice.warmup_03_running_sum import solve


def test_basic():
    assert solve([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_single():
    assert solve([5]) == [5]


def test_empty():
    assert solve([]) == []


def test_negatives():
    assert solve([-1, -2, -3]) == [-1, -3, -6]


def test_mixed():
    assert solve([3, -1, 2, -4, 5]) == [3, 2, 4, 0, 5]


def test_zeros():
    assert solve([0, 0, 0]) == [0, 0, 0]
