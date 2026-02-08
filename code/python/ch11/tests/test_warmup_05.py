"""
Tests for Warmup 5: Array Intersection
========================================
Chapter 11: Hashing — The Secret Decoder Ring

Run with:
    python -m pytest code/python/ch11/tests/test_warmup_05.py -v
"""
from ch11.practice.warmup_05_intersection import solve


def test_basic():
    assert solve([1, 2, 2, 1], [2, 2]) == [2]


def test_multiple():
    assert solve([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]


def test_no_common():
    assert solve([1, 2, 3], [4, 5, 6]) == []


def test_empty():
    assert solve([], [1, 2]) == []


def test_all_same():
    assert solve([1, 1, 1], [1]) == [1]
