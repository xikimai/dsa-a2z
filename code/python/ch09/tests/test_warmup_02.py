"""
Tests for Warmup 2: Binary Search
========================================
Chapter 9: Finding Needles — The Power of Searching

Run with:
    python -m pytest code/python/ch09/tests/test_warmup_02.py -v
"""
from ch09.practice.warmup_02_binary_search import solve


def test_found_middle():
    assert solve([1, 3, 5, 7, 9, 11], 7) == 3


def test_not_found():
    assert solve([1, 3, 5, 7, 9, 11], 4) == -1


def test_found_first():
    assert solve([2, 4, 6, 8, 10], 2) == 0


def test_found_last():
    assert solve([2, 4, 6, 8, 10], 10) == 4


def test_empty_array():
    assert solve([], 5) == -1


def test_single_element_found():
    assert solve([1], 1) == 0
